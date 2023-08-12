"""drop audit_log

Revision ID: 593f439461a3
Revises: 2d8691005252
Create Date: 2023-08-12 19:07:56.488429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '593f439461a3'
down_revision = '2d8691005252'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table('audit_log')


def downgrade() -> None:
    op.create_table(
        'audit_log',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('message', sa.String(length=500), nullable=False),
        sa.Column('created_by', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.PrimaryKeyConstraint('id')
    )
