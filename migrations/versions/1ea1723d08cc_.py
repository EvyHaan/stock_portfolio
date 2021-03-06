"""empty message

Revision ID: 1ea1723d08cc
Revises: 4835f228861e
Create Date: 2019-03-06 17:04:45.023825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ea1723d08cc'
down_revision = '4835f228861e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_portfolios_name', table_name='portfolios')
    op.create_index(op.f('ix_portfolios_name'), 'portfolios', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_portfolios_name'), table_name='portfolios')
    op.create_index('ix_portfolios_name', 'portfolios', ['name'], unique=False)
    # ### end Alembic commands ###
