"""update_product_name_unqunique.

Revision ID: abaaccb564db
Revises: 75ee8565ad36
Create Date: 2023-06-06 21:51:53.583675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abaaccb564db'
down_revision = '75ee8565ad36'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('products', 'name', nullable=False)
    op.alter_column('products', 'description', nullable=False)
    op.alter_column('products', 'price', nullable=False)
    op.alter_column('products', 'quantity', nullable=False)
    op.alter_column('products', 'image', nullable=True)

def downgrade() -> None:
    op.alter_column('products', 'name', nullable=True)
    op.alter_column('products', 'description', nullable=True)
    op.alter_column('products', 'price', nullable=True)
    op.alter_column('products', 'quantity', nullable=True)
    op.alter_column('products', 'image', nullable=False)

