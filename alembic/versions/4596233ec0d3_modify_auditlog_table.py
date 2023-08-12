"""Modify AuditLog table

Revision ID: 4596233ec0d3
Revises: a9d56b86b38e
Create Date: 2023-08-12 18:39:49.404688

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4596233ec0d3'
down_revision = 'a9d56b86b38e'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('audit_log_created_by_fkey', 'audit_log', type_='foreignkey')
    op.drop_column('audit_log', 'created_by')

    op.add_column('audit_log', sa.Column('created_by', sa.String(length=255), nullable=False))
    op.add_column('audit_log', sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()))

def downgrade():
    op.drop_column('audit_log', 'created_by')
    op.drop_column('audit_log', 'created_at')
    op.add_column('audit_log', sa.Column('created_by', sa.UUID(), sa.ForeignKey('users.id'), nullable=False))
    op.create_foreign_key('audit_log_created_by_fkey', 'audit_log', 'users', ['created_by'], ['id'])