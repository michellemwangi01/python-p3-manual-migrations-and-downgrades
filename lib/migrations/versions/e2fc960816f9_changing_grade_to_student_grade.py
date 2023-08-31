"""changing grade to student_grade

Revision ID: e2fc960816f9
Revises: 791279dd0760
Create Date: 2023-08-31 09:49:27.061955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2fc960816f9'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'grade', new_column_name='student_grade')


def downgrade() -> None:
    op.alter_column('students', 'student_grade', new_column_name='grade')

