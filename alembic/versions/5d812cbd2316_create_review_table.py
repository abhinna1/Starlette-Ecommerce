"""create review table.

Revision ID: 5d812cbd2316
Revises: 32a9569049fd
Create Date: 2023-08-12 13:05:13.037939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d812cbd2316'
down_revision = '32a9569049fd'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'review',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('description', sa.String(length=500), nullable=False),
        sa.Column('product_id', sa.UUID(), nullable=False),
        sa.Column('user_id', sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id'),
    )

def downgrade():
    op.drop_table('review')