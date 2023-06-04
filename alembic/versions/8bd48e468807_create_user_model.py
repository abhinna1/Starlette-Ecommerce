"""create_user_model

Revision ID: 8bd48e468807
Revises: 
Create Date: 2023-06-04 21:23:19.183970

"""
from alembic import op
import sqlalchemy as sa
from commons.ENUMS import UserEnum
import uuid

# revision identifiers, used by Alembic.
revision = '8bd48e468807'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True, index=True, default=str(uuid.uuid4)),
        sa.Column('username', sa.String(), unique=True),
        sa.Column('email', sa.String(), unique=True),
        sa.Column('password', sa.String()),
        sa.Column('role', sa.Enum(UserEnum), server_default=UserEnum.USER.value),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('users')
