"""Add git_url to Member

Revision ID: 2dcec11d4b2f
Revises: 
Create Date: 2024-06-26 20:15:00.854159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dcec11d4b2f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('member', schema=None) as batch_op:
        batch_op.add_column(sa.Column('git_url', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('member', schema=None) as batch_op:
        batch_op.drop_column('git_url')

    # ### end Alembic commands ###
