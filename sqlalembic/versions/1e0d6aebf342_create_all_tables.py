"""create all tables

Revision ID: 1e0d6aebf342
Revises: d2719a4b379e
Create Date: 2022-05-26 13:33:15.788888

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '1e0d6aebf342'
down_revision = 'd2719a4b379e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", sa.Column("id", sa.Integer, primary_key=True),
                    sa.Column("mail", sa.String, nullable=False),
                    sa.Column("password", sa.String, nullable=False),
                    sa.Column("created_at", sa.String, nullable=False, default=str(datetime.now()))
                    )
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))
    op.add_column("posts", sa.Column("published", sa.Boolean, nullable=False, default=False))
    op.add_column("posts", sa.Column("created_at", sa.String, nullable=False, default=str(datetime.now())))
    op.add_column("posts",
                  sa.Column("owner_id", sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False))


def downgrade():
    op.drop_table("users")
    op.drop_column("posts", "content")
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    op.drop_column("posts", "owner_id")
