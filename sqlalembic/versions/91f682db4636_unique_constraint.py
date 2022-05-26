"""unique constraint

Revision ID: 91f682db4636
Revises: 1e0d6aebf342
Create Date: 2022-05-26 13:49:32.036854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91f682db4636'
down_revision = '1e0d6aebf342'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("users", "mail")
    op.add_column("users", sa.Column("mail", sa.String, nullable=False, unique=True))
    pass


def downgrade():
    pass
