"""create posts table

Revision ID: d2719a4b379e
Revises: 
Create Date: 2022-05-26 12:43:28.870786

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd2719a4b379e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer, primary_key=True, nullable=False),
                    sa.Column("title", sa.String, nullable=False))


def downgrade():
    op.drop_table("posts")
    pass
