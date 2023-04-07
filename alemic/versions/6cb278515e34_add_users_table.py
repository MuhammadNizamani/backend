"""add users table

Revision ID: 6cb278515e34
Revises: 863691beafbb
Create Date: 2023-04-07 14:45:11.749356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cb278515e34'
down_revision = '863691beafbb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint("email"))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
