from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9ef3f87cf7c6'
down_revision = '2d2427a755d9'
branch_labels = None
depends_on = None


def upgrade():
    # Check if the column exists before adding it
    connection = op.get_bind()
    inspector = sa.inspect(connection)
    columns = inspector.get_columns('posts')
    column_names = [column['name'] for column in columns]
    if 'content' not in column_names:
        op.add_column('posts', sa.Column(
            'content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
