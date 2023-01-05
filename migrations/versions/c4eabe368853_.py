"""empty message

Revision ID: c4eabe368853
Revises: 88510cea1e11
Create Date: 2023-01-04 17:20:12.021877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4eabe368853'
down_revision = '88510cea1e11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('planet', 'description',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('planet', 'is_rocky',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('planet', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('planet', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('planet', 'is_rocky',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('planet', 'description',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###
