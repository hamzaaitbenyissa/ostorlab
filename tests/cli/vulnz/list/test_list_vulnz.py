"""Tests for vulnz list command."""
import requests_mock as rq_mock
from click.testing import CliRunner
from pytest_mock import plugin

from ostorlab.apis.runners import authenticated_runner
from ostorlab.cli import rootcli
from ostorlab.runtimes.local.models import models


def testOstorlabVulnzListCLI_whenCorrectCommandsAndOptionsProvidedAndRuntimeIsLocal_showsVulnzInfo(
    mocker, db_engine_path
):
    """Test ostorlab vulnz list command with correct commands and options.
    Should show vulnz information.
    """
    runner = CliRunner()
    mocker.patch.object(models, "ENGINE_URL", db_engine_path)
    create_scan_db = models.Scan.create("test")
    vuln_db = models.Vulnerability.create(
        title="MyVuln",
        short_description="Xss",
        description="Javascript Vuln",
        recommendation="Sanitize data",
        technical_detail="a=$input",
        risk_rating="HIGH",
        cvss_v3_vector="5:6:7",
        dna="121312",
        location={
            "domain_name": {"name": "dummy.co"},
            "metadata": [{"type": "URL", "value": "https://dummy.co/dummy"}],
        },
        scan_id=create_scan_db.id,
    )
    result = runner.invoke(
        rootcli.rootcli, ["vulnz", "list", "-s", str(vuln_db.scan_id)]
    )

    assert vuln_db.scan_id is not None
    assert result.exception is None
    assert "MyVuln" in result.output
    assert "High" in result.output
    assert "https://dummy" in result.output


def testOstorlabVulnzListCLI_ScanNotFoundAndRuntimeCloud_showsNotFoundError(
    requests_mock,
):
    """Ensure the vulnz list cli command correctly handles case where the scan is not found by the API."""
    mock_response = {
        "errors": [
            {
                "message": "Scan matching query does not exist.",
                "locations": [{"line": 2, "column": 13}],
                "path": ["scan"],
            }
        ],
    }
    runner = CliRunner()
    requests_mock.post(
        authenticated_runner.AUTHENTICATED_GRAPHQL_ENDPOINT,
        json=mock_response,
        status_code=401,
    )
    result = runner.invoke(
        rootcli.rootcli, ["vulnz", "--runtime", "cloud", "list", "--scan-id", "56835"]
    )
    assert "ERROR: scan with id 56835 does not exist." in result.output, result.output


def testOstorlabVulnzListCLI_WhenRuntimeCloudAndValiScanID_showsVulnzInfo(
    requests_mock,
):
    """Ensure the vulnz list cli command displays the vulnerabilities information correctly."""
    mock_response = {
        "data": {
            "scan": {
                "vulnerabilities": {
                    "vulnerabilities": [
                        {
                            "id": "38312829",
                            "detail": {
                                "title": "Intent Spoofing",
                                "shortDescription": "The application is vulnerable to intent spoofing which ..",
                                "cvssV3Vector": "CVSS:3.0/AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H",
                                "riskRating": "POTENTIALLY",
                            },
                        },
                        {
                            "id": "38312828",
                            "detail": {
                                "title": "Intent Spoofing",
                                "shortDescription": "The application is vulner...",
                                "cvssV3Vector": "CVSS:3.0/AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H",
                                "riskRating": "POTENTIALLY",
                            },
                        },
                    ]
                }
            }
        }
    }
    runner = CliRunner()
    requests_mock.post("https://api.ostorlab.co/apis/graphql", json=mock_response)
    result = runner.invoke(
        rootcli.rootcli, ["vulnz", "--runtime", "cloud", "list", "--scan-id", "56835"]
    )
    assert "Title" in result.output, result.output
    assert "Scan 56835: Found 2 vulnerabilities" in result.output, result.output


def testOstorlabVulnzListCLI_whenFilterByRiskRatingAndRuntimeIsLocal_showsCorrectResult(
    mocker: plugin.MockerFixture,
    db_engine_path: str,
) -> None:
    """Test ostorlab vulnz list command with filter by risk rating and runtime is local.
    Should show the correct results."""
    runner = CliRunner()
    mocker.patch.object(models, "ENGINE_URL", db_engine_path)
    create_scan_db = models.Scan.create("test")
    models.Vulnerability.create(
        title="Remote command execution",
        short_description="Remote command execution",
        description="Remote command execution",
        recommendation="Sanitize data",
        technical_detail="a=$input",
        risk_rating="HIGH",
        cvss_v3_vector="5:6:7",
        dna="121312",
        location={
            "domain_name": {"name": "dummy.co"},
            "metadata": [{"type": "URL", "value": "https://dummy.co/dummy"}],
        },
        scan_id=create_scan_db.id,
    )
    models.Vulnerability.create(
        title="List of dynamic code loading API calls",
        short_description="List of dynamic code loading API calls",
        description="List of dynamic code loading API calls",
        recommendation="Sanitize data",
        technical_detail="a=$input",
        risk_rating="INFO",
        cvss_v3_vector="5:6:7",
        dna="121312",
        location={
            "domain_name": {"name": "dummy.co"},
            "metadata": [{"type": "URL", "value": "https://dummy.co/dummy"}],
        },
        scan_id=create_scan_db.id,
    )
    models.Vulnerability.create(
        title="The application calls the registerReceiver method with the argument flags set to RECEIVER_EXPORTED",
        short_description="The application calls the registerReceiver method with the argument flags set to RECEIVER_EXPORTED",
        description="The application calls the registerReceiver method with the argument flags set to RECEIVER_EXPORTED",
        recommendation="Sanitize data",
        technical_detail="a=$input",
        risk_rating="MEDIUM",
        cvss_v3_vector="5:6:7",
        dna="121312",
        location={
            "domain_name": {"name": "dummy.co"},
            "metadata": [{"type": "URL", "value": "https://dummy.co/dummy"}],
        },
        scan_id=create_scan_db.id,
    )
    models.Vulnerability.create(
        title="Application is compiled with debug mode disabled",
        short_description="Application is compiled with debug mode disabled",
        description="Application is compiled with debug mode disabled",
        recommendation="Sanitize data",
        technical_detail="a=$input",
        risk_rating="SECURE",
        cvss_v3_vector="5:6:7",
        dna="121312",
        location={
            "domain_name": {"name": "dummy.co"},
            "metadata": [{"type": "URL", "value": "https://dummy.co/dummy"}],
        },
        scan_id=create_scan_db.id,
    )

    result_exact = runner.invoke(
        rootcli.rootcli, ["vulnz", "list", "-s", str(create_scan_db.id), "-r", "HIGH"]
    )
    result_gte = runner.invoke(
        rootcli.rootcli,
        ["vulnz", "list", "-s", str(create_scan_db.id), "-r", "MEDIUM", "-f", "gte"],
    )
    result_lte = runner.invoke(
        rootcli.rootcli,
        ["vulnz", "list", "-s", str(create_scan_db.id), "-r", "MEDIUM", "-f", "lte"],
    )

    assert result_exact.exception is None
    assert "Scan 1: Found 1 vulnerabilities." in result_exact.output
    assert (
        """┌────┬──────────────┬──────────────┬─────────────┬──────────────┬──────────────┐
    │    │              │ Vulnerable   │             │ CVSS V3      │ Short        │
    │ Id │ Title        │ target       │ Risk rating │ Vector       │ Description  │
    ╞════╪══════════════╪══════════════╪═════════════╪══════════════╪══════════════╡
    │ 1  │ Remote       │ Domain:      │ High        │ 5:6:7        │ Remote       │
    │    │ command      │ dummy.co     │             │              │ command      │
    │    │ execution    │ URL:         │             │              │ execution    │
    │    │              │ https://dum… │             │              │              │
    └────┴──────────────┴──────────────┴─────────────┴──────────────┴──────────────┘"""
        in result_exact.output
    )
    assert result_gte.exception is None
    assert (
        """┌────┬──────────────┬──────────────┬─────────────┬──────────────┬──────────────┐
    │    │              │ Vulnerable   │             │ CVSS V3      │ Short        │
    │ Id │ Title        │ target       │ Risk rating │ Vector       │ Description  │
    ╞════╪══════════════╪══════════════╪═════════════╪══════════════╪══════════════╡
    │ 1  │ Remote       │ Domain:      │ High        │ 5:6:7        │ Remote       │
    │    │ command      │ dummy.co     │             │              │ command      │
    │    │ execution    │ URL:         │             │              │ execution    │
    │    │              │ https://dum… │             │              │              │
    ├────┼──────────────┼──────────────┼─────────────┼──────────────┼──────────────┤
    │ 3  │ The          │ Domain:      │ Medium      │ 5:6:7        │ The          │
    │    │ application  │ dummy.co     │             │              │ application  │
    │    │ calls the    │ URL:         │             │              │ calls the    │
    │    │ registerRec… │ https://dum… │             │              │ registerRec… │
    │    │ method with  │              │             │              │ method with  │
    │    │ the argument │              │             │              │ the argument │
    │    │ flags set to │              │             │              │ flags set to │
    │    │ RECEIVER_EX… │              │             │              │ RECEIVER_EX… │
    └────┴──────────────┴──────────────┴─────────────┴──────────────┴──────────────┘"""
        in result_gte.output
    )
    assert result_lte.exception is None
    assert (
        """┌────┬──────────────┬──────────────┬─────────────┬──────────────┬──────────────┐
    │    │              │ Vulnerable   │             │ CVSS V3      │ Short        │
    │ Id │ Title        │ target       │ Risk rating │ Vector       │ Description  │
    ╞════╪══════════════╪══════════════╪═════════════╪══════════════╪══════════════╡
    │ 4  │ Application  │ Domain:      │ Secure      │ 5:6:7        │ Application  │
    │    │ is compiled  │ dummy.co     │             │              │ is compiled  │
    │    │ with debug   │ URL:         │             │              │ with debug   │
    │    │ mode         │ https://dum… │             │              │ mode         │
    │    │ disabled     │              │             │              │ disabled     │
    ├────┼──────────────┼──────────────┼─────────────┼──────────────┼──────────────┤
    │ 2  │ List of      │ Domain:      │ Info        │ 5:6:7        │ List of      │
    │    │ dynamic code │ dummy.co     │             │              │ dynamic code │
    │    │ loading API  │ URL:         │             │              │ loading API  │
    │    │ calls        │ https://dum… │             │              │ calls        │
    ├────┼──────────────┼──────────────┼─────────────┼──────────────┼──────────────┤
    │ 3  │ The          │ Domain:      │ Medium      │ 5:6:7        │ The          │
    │    │ application  │ dummy.co     │             │              │ application  │
    │    │ calls the    │ URL:         │             │              │ calls the    │
    │    │ registerRec… │ https://dum… │             │              │ registerRec… │
    │    │ method with  │              │             │              │ method with  │
    │    │ the argument │              │             │              │ the argument │
    │    │ flags set to │              │             │              │ flags set to │
    │    │ RECEIVER_EX… │              │             │              │ RECEIVER_EX… │
    └────┴──────────────┴──────────────┴─────────────┴──────────────┴──────────────┘"""
        in result_lte.output
    )


def testOstorlabVulnzListCLI_whenFilterByTitleAndRuntimeIsLocal_showsCorrectResult(
    mocker: plugin.MockerFixture,
    db_engine_path: str,
) -> None:
    """Test ostorlab vulnz list command with filter by title and runtime is local.
    Should show the correct result."""
    runner = CliRunner()
    mocker.patch.object(models, "ENGINE_URL", db_engine_path)
    create_scan_db = models.Scan.create("test")
    models.Vulnerability.create(
        title="Remote command execution",
        short_description="Remote command execution",
        description="Remote command execution",
        recommendation="Sanitize data",
        technical_detail="a=$input",
        risk_rating="HIGH",
        cvss_v3_vector="5:6:7",
        dna="121312",
        location={
            "domain_name": {"name": "dummy.co"},
            "metadata": [{"type": "URL", "value": "https://dummy.co/dummy"}],
        },
        scan_id=create_scan_db.id,
    )

    result = runner.invoke(
        rootcli.rootcli, ["vulnz", "list", "-s", str(create_scan_db.id), "-t", "remote"]
    )

    assert result.exception is None
    assert "Scan 1: Found 1 vulnerabilities." in result.output
    assert (
        """┌────┬──────────────┬──────────────┬─────────────┬──────────────┬──────────────┐
    │    │              │ Vulnerable   │             │ CVSS V3      │ Short        │
    │ Id │ Title        │ target       │ Risk rating │ Vector       │ Description  │
    ╞════╪══════════════╪══════════════╪═════════════╪══════════════╪══════════════╡
    │ 1  │ Remote       │ Domain:      │ High        │ 5:6:7        │ Remote       │
    │    │ command      │ dummy.co     │             │              │ command      │
    │    │ execution    │ URL:         │             │              │ execution    │
    │    │              │ https://dum… │             │              │              │
    └────┴──────────────┴──────────────┴─────────────┴──────────────┴──────────────┘"""
        in result.output
    )


def testOstorlabVulnzListCLI_whenFilterIsNotCorrectAndRuntimeIsLocal_showBadOptionUsageError(
    mocker: plugin.MockerFixture,
    db_engine_path: str,
) -> None:
    """Test ostorlab vulnz list command with wrong filter type.
    Should show BadOptionUsage error."""
    runner = CliRunner()
    mocker.patch.object(models, "ENGINE_URL", db_engine_path)
    create_scan_db = models.Scan.create("test")
    models.Vulnerability.create(
        title="Remote command execution",
        short_description="Remote command execution",
        description="Remote command execution",
        recommendation="Sanitize data",
        technical_detail="a=$input",
        risk_rating="HIGH",
        cvss_v3_vector="5:6:7",
        dna="121312",
        location={
            "domain_name": {"name": "dummy.co"},
            "metadata": [{"type": "URL", "value": "https://dummy.co/dummy"}],
        },
        scan_id=create_scan_db.id,
    )

    result = runner.invoke(
        rootcli.rootcli, ["vulnz", "list", "-s", str(create_scan_db.id), "-f", "gte"]
    )

    assert result.exception is not None
    assert (
        "Error: --filter-type / -f can only be used with risk-rating" in result.output
    )


def testOstorlabVulnzListCLI_whenFilterByRiskRatingAndRuntimeIsCloud_showsCorrectResult(
    requests_mock: rq_mock.Mocker,
) -> None:
    """Test ostorlab vulnz list command with filter by title and runtime is cloud.
    Should show the correct result."""
    mock_response = {
        "data": {
            "scan": {
                "vulnerabilities": {
                    "vulnerabilities": [
                        {
                            "id": "38312829",
                            "detail": {
                                "title": "Remote command execution",
                                "shortDescription": "Remote command execution",
                                "cvssV3Vector": "CVSS:3.0/AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H",
                                "riskRating": "HIGH",
                            },
                        },
                        {
                            "id": "38312828",
                            "detail": {
                                "title": "List of dynamic code loading API calls",
                                "shortDescription": "List of dynamic code loading API calls",
                                "cvssV3Vector": "CVSS:3.0/AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H",
                                "riskRating": "INFO",
                            },
                        },
                        {
                            "id": "38312827",
                            "detail": {
                                "title": "The application calls the registerReceiver method with the argument flags set to RECEIVER_EXPORTED",
                                "shortDescription": "The application calls the registerReceiver method with the argument flags set to RECEIVER_EXPORTED",
                                "cvssV3Vector": "CVSS:3.0/AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H",
                                "riskRating": "MEDIUM",
                            },
                        },
                        {
                            "id": "38312826",
                            "detail": {
                                "title": "Application is compiled with debug mode disabled",
                                "shortDescription": "Application is compiled with debug mode disabled",
                                "cvssV3Vector": "CVSS:3.0/AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H",
                                "riskRating": "SECURE",
                            },
                        },
                        {
                            "id": "38312825",
                            "detail": {
                                "title": "Server Side Inclusion",
                                "shortDescription": "Server Side Inclusion",
                                "cvssV3Vector": "CVSS:3.0/AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H",
                                "riskRating": "CRITICAL",
                            },
                        },
                    ]
                }
            }
        }
    }
    runner = CliRunner()
    requests_mock.post("https://api.ostorlab.co/apis/graphql", json=mock_response)

    result_exact = runner.invoke(
        rootcli.rootcli,
        [
            "vulnz",
            "--runtime",
            "cloud",
            "list",
            "--scan-id",
            "56835",
            "--risk-rating",
            "HIGH",
        ],
    )
    result_gte = runner.invoke(
        rootcli.rootcli,
        [
            "vulnz",
            "--runtime",
            "cloud",
            "list",
            "--scan-id",
            "56835",
            "--risk-rating",
            "MEDIUM",
            "--filter-type",
            "gte",
        ],
    )
    result_lte = runner.invoke(
        rootcli.rootcli,
        [
            "vulnz",
            "--runtime",
            "cloud",
            "list",
            "--scan-id",
            "56835",
            "--risk-rating",
            "MEDIUM",
            "--filter-type",
            "lte",
        ],
    )

    assert "Scan 56835: Found 1 vulnerabilities." in result_exact.output
    assert (
        """┌──────────┬─────────────┬─────────────┬────────────┬─────────────┬────────────┐
│          │             │ Vulnerable  │ Risk       │ CVSS V3     │ Short      │
│ Id       │ Title       │ target      │ Rating     │ Vector      │ Descripti… │
╞══════════╪═════════════╪═════════════╪════════════╪═════════════╪════════════╡
│ 38312829 │ Remote      │             │ High       │ CVSS:3.0/A… │ Remote     │
│          │ command     │             │            │             │ command    │
│          │ execution   │             │            │             │ execution  │
└──────────┴─────────────┴─────────────┴────────────┴─────────────┴────────────┘"""
        in result_exact.output
    )
    assert "Scan 56835: Found 3 vulnerabilities." in result_gte.output
    assert (
        """┌──────────┬─────────────┬─────────────┬────────────┬─────────────┬────────────┐
│          │             │ Vulnerable  │ Risk       │ CVSS V3     │ Short      │
│ Id       │ Title       │ target      │ Rating     │ Vector      │ Descripti… │
╞══════════╪═════════════╪═════════════╪════════════╪═════════════╪════════════╡
│ 38312829 │ Remote      │             │ High       │ CVSS:3.0/A… │ Remote     │
│          │ command     │             │            │             │ command    │
│          │ execution   │             │            │             │ execution  │
├──────────┼─────────────┼─────────────┼────────────┼─────────────┼────────────┤
│ 38312827 │ The         │             │ Medium     │ CVSS:3.0/A… │ The        │
│          │ application │             │            │             │ applicati… │
│          │ calls the   │             │            │             │ calls the  │
│          │ registerRe… │             │            │             │ registerR… │
│          │ method with │             │            │             │ method     │
│          │ the         │             │            │             │ with the   │
│          │ argument    │             │            │             │ argument   │
│          │ flags set   │             │            │             │ flags set  │
│          │ to          │             │            │             │ to         │
│          │ RECEIVER_E… │             │            │             │ RECEIVER_… │
├──────────┼─────────────┼─────────────┼────────────┼─────────────┼────────────┤
│ 38312825 │ Server Side │             │ Critical   │ CVSS:3.0/A… │ Server     │
│          │ Inclusion   │             │            │             │ Side       │
│          │             │             │            │             │ Inclusion  │
└──────────┴─────────────┴─────────────┴────────────┴─────────────┴────────────┘"""
        in result_gte.output
    )
    assert "Scan 56835: Found 3 vulnerabilities." in result_lte.output
    assert (
        """┌──────────┬─────────────┬─────────────┬────────────┬─────────────┬────────────┐
│          │             │ Vulnerable  │ Risk       │ CVSS V3     │ Short      │
│ Id       │ Title       │ target      │ Rating     │ Vector      │ Descripti… │
╞══════════╪═════════════╪═════════════╪════════════╪═════════════╪════════════╡
│ 38312828 │ List of     │             │ Info       │ CVSS:3.0/A… │ List of    │
│          │ dynamic     │             │            │             │ dynamic    │
│          │ code        │             │            │             │ code       │
│          │ loading API │             │            │             │ loading    │
│          │ calls       │             │            │             │ API calls  │
├──────────┼─────────────┼─────────────┼────────────┼─────────────┼────────────┤
│ 38312827 │ The         │             │ Medium     │ CVSS:3.0/A… │ The        │
│          │ application │             │            │             │ applicati… │
│          │ calls the   │             │            │             │ calls the  │
│          │ registerRe… │             │            │             │ registerR… │
│          │ method with │             │            │             │ method     │
│          │ the         │             │            │             │ with the   │
│          │ argument    │             │            │             │ argument   │
│          │ flags set   │             │            │             │ flags set  │
│          │ to          │             │            │             │ to         │
│          │ RECEIVER_E… │             │            │             │ RECEIVER_… │
├──────────┼─────────────┼─────────────┼────────────┼─────────────┼────────────┤
│ 38312826 │ Application │             │ Secure     │ CVSS:3.0/A… │ Applicati… │
│          │ is compiled │             │            │             │ is         │
│          │ with debug  │             │            │             │ compiled   │
│          │ mode        │             │            │             │ with debug │
│          │ disabled    │             │            │             │ mode       │
│          │             │             │            │             │ disabled   │
└──────────┴─────────────┴─────────────┴────────────┴─────────────┴────────────┘"""
        in result_lte.output
    )


def testOstorlabVulnzListCLI_whenFilterByTitleAndRuntimeIsCloud_showsCorrectResult(
    requests_mock: rq_mock.Mocker,
) -> None:
    """Test ostorlab vulnz list command with filter by title and runtime is cloud.
    Should show the correct result."""
    mock_response = {
        "data": {
            "scan": {
                "vulnerabilities": {
                    "vulnerabilities": [
                        {
                            "id": "38312829",
                            "detail": {
                                "title": "Remote command execution",
                                "shortDescription": "Remote command execution",
                                "cvssV3Vector": "CVSS:3.0/AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H",
                                "riskRating": "HIGH",
                            },
                        },
                        {
                            "id": "38312828",
                            "detail": {
                                "title": "List of dynamic code loading API calls",
                                "shortDescription": "List of dynamic code loading API calls",
                                "cvssV3Vector": "CVSS:3.0/AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H",
                                "riskRating": "INFO",
                            },
                        },
                    ]
                }
            }
        }
    }
    runner = CliRunner()
    requests_mock.post("https://api.ostorlab.co/apis/graphql", json=mock_response)

    result = runner.invoke(
        rootcli.rootcli,
        [
            "vulnz",
            "--runtime",
            "cloud",
            "list",
            "--scan-id",
            "56835",
            "--title",
            "command execu",
        ],
    )

    assert "Scan 56835: Found 1 vulnerabilities." in result.output
    assert (
        """┌──────────┬─────────────┬─────────────┬────────────┬─────────────┬────────────┐
│          │             │ Vulnerable  │ Risk       │ CVSS V3     │ Short      │
│ Id       │ Title       │ target      │ Rating     │ Vector      │ Descripti… │
╞══════════╪═════════════╪═════════════╪════════════╪═════════════╪════════════╡
│ 38312829 │ Remote      │             │ High       │ CVSS:3.0/A… │ Remote     │
│          │ command     │             │            │             │ command    │
│          │ execution   │             │            │             │ execution  │
└──────────┴─────────────┴─────────────┴────────────┴─────────────┴────────────┘"""
        in result.output
    )
