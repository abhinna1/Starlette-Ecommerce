"""change product image type to string.

Revision ID: 10c24f101b4e
Revises: 980600c99d47
Create Date: 2023-08-12 11:28:56.154031

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision = '10c24f101b4e'
down_revision = '980600c99d47'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('products', 'image', type_=sa.String(), nullable=True)

def downgrade() -> None:
    op.alter_column('products', 'image', type_=JSONB(), nullable=True)