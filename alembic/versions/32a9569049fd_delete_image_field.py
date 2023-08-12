"""delete image field.

Revision ID: 32a9569049fd
Revises: 10c24f101b4e
Create Date: 2023-08-12 11:32:32.997433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32a9569049fd'
down_revision = '10c24f101b4e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('products', 'image')

def downgrade() -> None:
    op.add_column('products', sa.Column('image', sa.String(), nullable=True))