"""create_product_model

Revision ID: 75ee8565ad36
Revises: 01d0a415ebf9
Create Date: 2023-06-04 22:31:10.817827

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
import uuid

# revision identifiers, used by Alembic.
revision = '75ee8565ad36'
down_revision = '01d0a415ebf9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True, index=True, default=str(uuid.uuid4)),
        sa.Column('name', sa.String(length=150)),
        sa.Column('description', sa.String(length=500)),
        sa.Column('price', sa.Integer()),
        sa.Column('quantity', sa.Integer(), default=0),
        sa.Column('image', JSONB(), nullable=False, default=[]),
        sa.PrimaryKeyConstraint('id')
    )



def downgrade() -> None:
    op.drop_table('products')
