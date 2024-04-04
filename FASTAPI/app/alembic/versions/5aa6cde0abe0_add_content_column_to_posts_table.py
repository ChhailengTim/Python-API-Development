"""add content column to posts table

Revision ID: 5aa6cde0abe0
Revises: 9ef3f87cf7c6
Create Date: 2024-04-04 11:38:14.342212

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5aa6cde0abe0'
down_revision: Union[str, None] = '9ef3f87cf7c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
