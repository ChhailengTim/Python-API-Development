"""add foreign-key to posts table

Revision ID: 0064e609a8f7
Revises: 3ab563167bf3
Create Date: 2024-04-04 11:50:51.789928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0064e609a8f7'
down_revision: Union[str, None] = '3ab563167bf3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'post_users_fk',
        source_table='posts',
        referent_table='users',
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete='CASCADE'
    )
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', 'posts', type_='foreignkey')
    op.drop_column('posts', 'owner_id')
    pass
