"""empty message

Revision ID: e3a1cc1a2634
Revises: ad682e54bef2
Create Date: 2021-04-17 11:56:39.922113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3a1cc1a2634'
down_revision = 'ad682e54bef2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'description',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('products', 'image_path',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('products', 'price',
               existing_type=sa.REAL(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'price',
               existing_type=sa.REAL(),
               nullable=True)
    op.alter_column('products', 'image_path',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('products', 'description',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###
