"""convert cartitem quantity to string

Revision ID: 980600c99d47
Revises: 7e89fc0fca38
Create Date: 2023-07-25 10:43:12.050489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '980600c99d47'
down_revision = '7e89fc0fca38'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        table_name='cart_items',
        column_name='quantity',
        nullable=False,
        type_=sa.String()
    )


def downgrade() -> None:
    op.alter_column(
        table_name='cart_items',
        column_name='quantity',
        nullable=False,
        type_=sa.UUID()
    )
