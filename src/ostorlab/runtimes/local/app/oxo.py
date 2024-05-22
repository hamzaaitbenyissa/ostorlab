from typing import Optional, List

import graphene
import graphql
from graphene_file_upload import scalars

from ostorlab.runtimes.local.models import models
from ostorlab.runtimes.local.app import import_utils, common
from ostorlab.runtimes.local.app import types
from graphql.execution import base as graphql_base

CASE_SQL = """CASE risk_rating
           WHEN 'critical' THEN 0
           WHEN 'high' THEN 1
           WHEN 'medium' THEN 2
           WHEN 'low' THEN 3
           WHEN 'potentially' THEN 4
           WHEN 'hardening' THEN 5
           WHEN 'secure' THEN 6
           WHEN 'important' THEN 7
           WHEN 'info' THEN 8
           end """


class Query(graphene.ObjectType):
    scans = graphene.Field(
        types.ScansType,
        scan_ids=graphene.List(graphene.Int, required=False),
        order_by=types.ScanOrderByEnum(required=False),
        sort=common.SortEnum(required=False),
        description="List of scans.",
    )
    scan = graphene.Field(types.ScanType, id=graphene.Int())

    vulnerabilities = graphene.Field(
        types.VulnerabilitiesType,
        vulnerability_ids=graphene.List(graphene.Int, required=False),
        order_by=types.VulnerabilityOrderByEnum(required=False),
        sort=common.SortEnum(required=False),
        description="List of vulnerabilities.",
    )
    vulnerability = graphene.Field(types.VulnerabilityType, id=graphene.Int())

    def resolve_scans(
        self,
        info: graphql_base.ResolveInfo,
        scan_ids: Optional[List[int]] = None,
        order_by: Optional[types.ScanOrderByEnum] = None,
        sort: Optional[common.SortEnum] = None,
    ) -> Optional[types.ScansType]:
        with models.Database() as session:
            scans = session.query(models.Scan)

            # Filtering
            if scan_ids is not None:
                scans = scans.filter(models.Scan.id.in_(scan_ids))

            # Ordering
            order_by_filter = None
            if order_by == types.ScanOrderByEnum.ScanId:
                order_by_filter = models.Scan.id
            elif order_by == types.ScanOrderByEnum.Title:
                order_by_filter = models.Scan.title
            elif order_by == types.ScanOrderByEnum.CreatedTime:
                order_by_filter = models.Scan.created_time
            elif order_by == types.ScanOrderByEnum.Progress:
                order_by_filter = models.Scan.progress

            if order_by_filter is not None and sort == types.common.Desc:
                scans = scans.order_by(order_by_filter.desc())
            elif order_by_filter is not None:
                scans = scans.order_by(order_by_filter)
            else:
                scans = scans.order_by(models.Scan.id.desc())

            return types.ScansType(scans=scans.all())

    def resolve_scan(self, info: graphql_base.ResolveInfo, id: int):
        with models.Database() as session:
            scan = session.query(models.Scan).filter_by(id=id).first()
            if scan is None:
                raise graphql.GraphQLError("Scan not found")
            return types.ScanType(
                id=scan.id,
                title=scan.title,
                asset=scan.asset,
                progress=scan.progress,
            )

    def resolve_vulnerabilities(
        self,
        info: graphql_base.ResolveInfo,
        vulnerability_ids: Optional[List[int]] = None,
        order_by: Optional[types.VulnerabilityOrderByEnum] = None,
        sort: Optional[common.SortEnum] = None,
    ) -> Optional[types.VulnerabilitiesType]:
        with models.Database() as session:
            vulnerabilities = session.query(models.Vulnerability)

            # Filtering
            if vulnerability_ids is not None:
                vulnerabilities = vulnerabilities.filter(
                    models.Vulnerability.id.in_(vulnerability_ids)
                )

            # Ordering
            order_by_filter = None
            if order_by == types.VulnerabilityOrderByEnum.VulnerabilityId:
                order_by_filter = models.Vulnerability.id
            elif order_by == types.VulnerabilityOrderByEnum.Title:
                order_by_filter = models.Vulnerability.title
            elif order_by == types.VulnerabilityOrderByEnum.RiskRating:
                vulnerabilities = vulnerabilities.extra(
                    select={"risk_rating_index": CASE_SQL}
                )
                order_by_filter = "risk_rating_index"

            if order_by_filter is not None and sort == common.SortEnum.Desc:
                vulnerabilities = vulnerabilities.order_by(order_by_filter.desc())
            elif order_by_filter is not None:
                vulnerabilities = vulnerabilities.order_by(order_by_filter)
            else:
                vulnerabilities = vulnerabilities.order_by(
                    models.Vulnerability.id.desc()
                )

            return types.VulnerabilitiesType(vulnerabilities=vulnerabilities.all())

    def resolve_vulnerability(
        self, info: graphql_base.ResolveInfo, id: int
    ):
        with models.Database() as session:
            vulnerability = (
                session.query(models.Vulnerability)
                .filter_by(id=id)
                .first()
            )
            if vulnerability is None:
                raise graphql.GraphQLError("Vulnerability not found")
            return types.VulnerabilityType(
                id=vulnerability.id,
                technical_detail=vulnerability.technical_detail,
                risk_rating=vulnerability.risk_rating.name,
                cvss_v3_vector=vulnerability.cvss_v3_vector,
                dna=vulnerability.dna,
                title=vulnerability.title,
                short_description=vulnerability.short_description,
                description=vulnerability.description,
                recommendation=vulnerability.recommendation,
                references=vulnerability.references,
                location=vulnerability.location,
            )


class ImportScanMutation(graphene.Mutation):
    class Arguments:
        scan_id = graphene.Int(required=False)
        file = scalars.Upload(required=True)

    message = graphene.String()

    @staticmethod
    def mutate(
        root,
        info: graphql_base.ResolveInfo,
        file: scalars.Upload,
        scan_id: Optional[int] = None,
    ):
        with models.Database() as session:
            scan = session.query(models.Scan).filter_by(id=scan_id).first()
            import_utils.import_scan(session, file.read(), scan)
            return ImportScanMutation(message="Scan imported successfully")


class Mutations(graphene.ObjectType):
    import_scan = ImportScanMutation.Field(description="Import scan from file")
