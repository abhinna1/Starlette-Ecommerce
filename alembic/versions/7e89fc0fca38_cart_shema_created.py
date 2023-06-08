"""cart shema created.

Revision ID: 7e89fc0fca38
Revises: abaaccb564db
Create Date: 2023-06-07 20:23:29.986538

"""
from alembic import op
import sqlalchemy as sa
from commons.ENUMS import CartStatusEnum
import uuid

# revision identifiers, used by Alembic.
revision = '7e89fc0fca38'
down_revision = 'abaaccb564db'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # create the cart model.
    op.create_table(
        'carts',
        sa.Column('id', sa.UUID, primary_key=True, index=True, unique=True, nullable=False, default=uuid.uuid4),
        sa.Column('user_id', sa.UUID, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('ordered_at', sa.DateTime, nullable=True),
        sa.Column('status', sa.Enum(CartStatusEnum), default=CartStatusEnum.ACTIVE),
    )

    # create the cartItem model.
    op.create_table(
        'cart_items',
        sa.Column('id', sa.UUID, primary_key=True, index=True, unique=True, nullable=False, default=uuid.uuid4),
        sa.Column('cart_id', sa.UUID, sa.ForeignKey('carts.id'), nullable=False),
        sa.Column('product_id', sa.UUID, sa.ForeignKey('products.id'), nullable=False),
        sa.Column('quantity', sa.Integer, nullable=False),
    )

def downgrade() -> None:
    op.drop_table('carts')
    op.drop_column('cart_items')
