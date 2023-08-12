"""Change AuditLog created_by data type

Revision ID: bb0bf9776052
Revises: fce4b7f53951
Create Date: 2023-08-12 19:01:14.221593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb0bf9776052'
down_revision = 'fce4b7f53951'
branch_labels = None
depends_on = None


def upgrade():
    pass
    # op.execute("ALTER TABLE audit_log DROP CONSTRAINT fk_reference_audit_log;")
    # op.execute("ALTER TABLE audit_log ALTER COLUMN created_by TYPE character varying(255);")
    # op.execute("ALTER TABLE audit_log ADD CONSTRAINT fk_reference_audit_log FOREIGN KEY (created_by) REFERENCES users(id);")

def downgrade():
    pass
    # op.execute("ALTER TABLE audit_log DROP CONSTRAINT fk_reference_audit_log;")
    # op.execute("ALTER TABLE audit_log ALTER COLUMN created_by TYPE uuid USING created_by::uuid;")
    # op.execute("ALTER TABLE audit_log ADD CONSTRAINT fk_reference_audit_log FOREIGN KEY (created_by) REFERENCES users(id);")
