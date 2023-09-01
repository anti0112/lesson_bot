"""new base 11.0

Revision ID: 08e5aed7b900
Revises: 
Create Date: 2023-09-01 14:13:39.433226

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08e5aed7b900'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('day',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('lesson_date', sa.String(), nullable=True),
    sa.Column('day_name', sa.String(), nullable=True),
    sa.Column('is_works', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('interval',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('lesson_time', sa.String(), nullable=True),
    sa.Column('is_works', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lesson',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('price', sa.DECIMAL(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('user_telegram_id', sa.Integer(), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('day_interval',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('day_id', sa.Integer(), nullable=True),
    sa.Column('interval_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['day_id'], ['day.id'], ),
    sa.ForeignKeyConstraint(['interval_id'], ['interval.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lessons_base',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('time', sa.String(), nullable=True),
    sa.Column('total_price', sa.DECIMAL(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('lesson_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lesson_id'], ['lesson.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lessons_base')
    op.drop_table('day_interval')
    op.drop_table('user')
    op.drop_table('lesson')
    op.drop_table('interval')
    op.drop_table('day')
    # ### end Alembic commands ###