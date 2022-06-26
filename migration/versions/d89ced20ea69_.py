"""empty message

Revision ID: d89ced20ea69
Revises: 4a656401f4cf
Create Date: 2022-06-26 16:40:47.267001

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd89ced20ea69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('create schema if not exists response')
    op.create_table('survey_responses',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('modified_by', sa.String(length=256), nullable=False),
    sa.Column('modified_on', sa.DateTime(timezone=True), nullable=False),
    sa.Column('full_name', sa.String(length=150), nullable=False),
    sa.Column('occupation', sa.String(length=150), nullable=False),
    sa.Column('favourite_tech', sa.String(length=150), nullable=True),
    sa.Column('skill', sa.String(length=150), nullable=True),
    sa.Column('current_competence_area', sa.String(length=256), nullable=True),
    sa.Column('linkedin_url', sa.String(length=256), nullable=True),
    sa.Column('certificates', sa.ARRAY(sa.String()), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='response'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('survey_responses', schema='response')
    op.execute('drop schema if exists response')
    # ### end Alembic commands ###