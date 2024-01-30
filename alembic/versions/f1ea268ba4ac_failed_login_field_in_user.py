"""failed_login field in user.

Revision ID: f1ea268ba4ac
Revises: 427ac699e2a1
Create Date: 2023-08-12 20:06:46.800482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1ea268ba4ac'
down_revision = '427ac699e2a1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('failed_login', sa.Integer(), nullable=False, server_default='0'))

def downgrade():
    op.drop_column('users', 'failed_login')