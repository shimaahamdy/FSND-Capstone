"""empty message

Revision ID: 1b67b2c025eb
Revises: 
Create Date: 2021-02-20 06:09:30.706606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b67b2c025eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('moive', 'rate')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('moive', sa.Column('rate', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###