"""audit_log created_by nullable.

Revision ID: fce4b7f53951
Revises: 4596233ec0d3
Create Date: 2023-08-12 18:41:48.230057

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fce4b7f53951'
down_revision = '4596233ec0d3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('audit_log', 'created_by', nullable=True)


def downgrade() -> None:
    op.alter_column('audit_log', 'created_by', nullable=False)