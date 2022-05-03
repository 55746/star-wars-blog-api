"""empty message

Revision ID: 64e8ccc4389f
Revises: 8c389981a08a
Create Date: 2022-05-03 15:48:09.039870

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '64e8ccc4389f'
down_revision = '8c389981a08a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('charachters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('charachter_name', sa.String(length=120), nullable=False),
    sa.Column('home_planet', sa.String(length=120), nullable=False),
    sa.Column('persons_age', sa.Integer(), nullable=False),
    sa.Column('persons_species', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id', 'home_planet', 'persons_age', 'persons_species'),
    sa.UniqueConstraint('charachter_name'),
    sa.UniqueConstraint('charachter_name')
    )
    op.create_table('favourites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('planets', sa.Column('rotation_speed', sa.String(length=120), nullable=True))
    op.alter_column('planets', 'planet_name',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('planets', 'planet_name',
               existing_type=mysql.VARCHAR(length=120),
               nullable=False)
    op.drop_column('planets', 'rotation_speed')
    op.drop_table('favourites')
    op.drop_table('charachters')
    # ### end Alembic commands ###
