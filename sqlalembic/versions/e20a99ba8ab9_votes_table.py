"""votes table

Revision ID: e20a99ba8ab9
Revises: 91f682db4636
Create Date: 2022-05-26 14:15:45.800427

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e20a99ba8ab9'
down_revision = '91f682db4636'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("votes",
                    sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
                    sa.Column("posts_id", sa.Integer, sa.ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
                    )


def downgrade():
    op.drop_table("votes")
