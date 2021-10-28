"""Initial migration.

Revision ID: 59340c174c28
Revises: 
Create Date: 2021-10-14 14:19:33.863441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59340c174c28'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assessment',
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('module', sa.String(length=20), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('completed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_index(op.f('ix_assessment_description'), 'assessment', ['description'], unique=False)
    op.create_index(op.f('ix_assessment_module'), 'assessment', ['module'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_assessment_module'), table_name='assessment')
    op.drop_index(op.f('ix_assessment_description'), table_name='assessment')
    op.drop_table('assessment')
    # ### end Alembic commands ###
