"""adding few last colmun to the posts table

Revision ID: 64ad3bcf2e13
Revises: c5bdc5bd9e47
Create Date: 2023-04-07 15:21:16.899039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64ad3bcf2e13'
down_revision = 'c5bdc5bd9e47'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
