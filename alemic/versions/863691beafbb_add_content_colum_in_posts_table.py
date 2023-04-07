"""add content colum in posts table

Revision ID: 863691beafbb
Revises: b6bf507584c6
Create Date: 2023-04-07 14:26:55.072839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '863691beafbb'
down_revision = 'b6bf507584c6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
