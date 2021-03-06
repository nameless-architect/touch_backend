"""add messages table

Revision ID: 62c7ef52c713
Revises: 632ca08f46b0
Create Date: 2021-02-20 22:45:53.586755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62c7ef52c713'
down_revision = '632ca08f46b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('from_uuid', sa.String(length=50), nullable=True),
    sa.Column('to_uuid', sa.String(length=50), nullable=True),
    sa.Column('content', sa.String(length=2255), nullable=True),
    sa.Column('content_type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
