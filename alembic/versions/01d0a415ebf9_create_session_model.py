"""create_session_model

Revision ID: 01d0a415ebf9
Revises: 8bd48e468807
Create Date: 2023-06-04 21:25:16.655829

"""
from alembic import op
import sqlalchemy as sa
import uuid
from datetime import datetime, timedelta
import dotenv
import os

dotenv.load_dotenv()
session_life = int(os.getenv('SESSION_LIFE'))

# revision identifiers, used by Alembic.
revision = '01d0a415ebf9'
down_revision = '8bd48e468807'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'sessions',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True, index=True, default=str(uuid.uuid4)),
        sa.Column('user_id', sa.UUID(as_uuid=True), sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime(), default=datetime.utcnow),
        sa.Column('expires_at', sa.DateTime(), default=datetime.utcnow() + timedelta(days=session_life)),
        sa.Column('is_expired', sa.Boolean(), default=False),
    )


def downgrade() -> None:
    op.drop_table('sessions')

