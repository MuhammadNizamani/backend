"""create posts table

Revision ID: b6bf507584c6
Revises: 
Create Date: 2023-04-06 17:59:13.259879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6bf507584c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column(
        'id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
