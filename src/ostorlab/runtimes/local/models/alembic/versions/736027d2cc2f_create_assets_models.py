"""create assets models

Revision ID: 736027d2cc2f
Revises: 23afcfd1d789
Create Date: 2024-06-03 10:33:26.311585

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "736027d2cc2f"
down_revision = "23afcfd1d789"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "asset",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("type", sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_asset")),
    )
    op.create_table(
        "android_file",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("package_name", sa.String(length=255), nullable=True),
        sa.Column("path", sa.String(length=1024), nullable=True),
        sa.ForeignKeyConstraint(
            ["id"], ["asset.id"], name=op.f("fk_android_file_id_asset")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_android_file")),
    )
    op.create_table(
        "android_store",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("package_name", sa.String(length=255), nullable=True),
        sa.Column("application_name", sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(
            ["id"], ["asset.id"], name=op.f("fk_android_store_id_asset")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_android_store")),
    )
    op.create_table(
        "ios_file",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("bundle_id", sa.String(length=255), nullable=True),
        sa.Column("path", sa.String(length=1024), nullable=True),
        sa.ForeignKeyConstraint(
            ["id"], ["asset.id"], name=op.f("fk_ios_file_id_asset")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_ios_file")),
    )
    op.create_table(
        "ios_store",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("bundle_id", sa.String(length=255), nullable=True),
        sa.Column("application_name", sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(
            ["id"], ["asset.id"], name=op.f("fk_ios_store_id_asset")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_ios_store")),
    )
    op.create_table(
        "network",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("networks", sa.String(length=1024), nullable=True),
        sa.ForeignKeyConstraint(["id"], ["asset.id"], name=op.f("fk_network_id_asset")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_network")),
    )
    op.create_table(
        "urls",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("links", sa.String(length=1024), nullable=True),
        sa.ForeignKeyConstraint(["id"], ["asset.id"], name=op.f("fk_urls_id_asset")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_urls")),
    )
    with op.batch_alter_table("scan", schema=None) as batch_op:
        batch_op.add_column(sa.Column("asset_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            batch_op.f("fk_scan_asset_id_asset"), "asset", ["asset_id"], ["id"]
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("scan", schema=None) as batch_op:
        batch_op.drop_constraint(
            batch_op.f("fk_scan_asset_id_asset"), type_="foreignkey"
        )
        batch_op.drop_column("asset_id")

    op.drop_table("urls")
    op.drop_table("network")
    op.drop_table("ios_store")
    op.drop_table("ios_file")
    op.drop_table("android_store")
    op.drop_table("android_file")
    op.drop_table("asset")
    # ### end Alembic commands ###
