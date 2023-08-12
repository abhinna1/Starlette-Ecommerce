"""again create audit_log

Revision ID: 427ac699e2a1
Revises: 593f439461a3
Create Date: 2023-08-12 19:08:41.256204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '427ac699e2a1'
down_revision = '593f439461a3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'audit_log',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('message', sa.String(length=500), nullable=False),
        sa.Column('created_by', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('audit_log')
