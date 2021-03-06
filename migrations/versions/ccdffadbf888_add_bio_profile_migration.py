"""add bio & profile migration

Revision ID: ccdffadbf888
Revises: 57b9fd5942f2
Create Date: 2021-04-21 08:08:54.530764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccdffadbf888'
down_revision = '57b9fd5942f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
