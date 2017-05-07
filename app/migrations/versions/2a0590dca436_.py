"""add link column

Revision ID: 2a0590dca436
Revises: 81985906a09a
Create Date: 2017-05-07 15:24:29.747227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a0590dca436'
down_revision = '81985906a09a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('channels', sa.Column('link', sa.Text(), nullable=True))
    op.alter_column('channels', 'slug',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('channels', 'slug',
               existing_type=sa.TEXT(),
               nullable=False)
    op.drop_column('channels', 'link')
    # ### end Alembic commands ###
