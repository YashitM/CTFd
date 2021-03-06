"""Adding max_attempts to Challenges

Revision ID: d6514ec92738
Revises: a4e30c94c360
Create Date: 2017-03-09 01:20:31.423407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6514ec92738'
down_revision = 'a4e30c94c360'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('challenges', sa.Column('max_attempts', sa.Integer(), nullable=True, default=0))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('challenges', 'max_attempts')
    # ### end Alembic commands ###
