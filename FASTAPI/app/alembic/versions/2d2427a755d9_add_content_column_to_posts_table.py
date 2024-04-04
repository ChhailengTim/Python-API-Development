"""add content column to posts table

Revision ID: 2d2427a755d9
Revises: 2022d70cf4fc
Create Date: 2024-04-04 11:23:02.970331

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d2427a755d9'
down_revision: Union[str, None] = '2022d70cf4fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
