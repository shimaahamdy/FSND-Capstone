"""empty message

Revision ID: 0e7411c850e3
Revises: 1b67b2c025eb
Create Date: 2021-02-20 06:32:06.399230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e7411c850e3'
down_revision = '1b67b2c025eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('moive', sa.Column('rate', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('moive', 'rate')
    # ### end Alembic commands ###