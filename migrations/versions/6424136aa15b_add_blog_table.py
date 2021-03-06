"""add blog table

Revision ID: 6424136aa15b
Revises: 4d07a90e887f
Create Date: 2020-10-17 18:36:17.522078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6424136aa15b'
down_revision = '4d07a90e887f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('body', sa.String(length=5000), nullable=False),
    sa.Column('published_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('body'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogs')
    # ### end Alembic commands ###
