"""recreate_audit log.

Revision ID: 2d8691005252
Revises: bb0bf9776052
Create Date: 2023-08-12 19:03:55.315352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d8691005252'
down_revision = 'bb0bf9776052'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('audit_log')
    op.create_table(
        'audit_log',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('message', sa.String(length=500), nullable=False),
        sa.Column('created_by', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('audit_log')