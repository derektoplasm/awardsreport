"""action_date_month_year and doc

Revision ID: 8bb6c0e38faa
Revises: 355fa982ae92
Create Date: 2023-10-16 13:40:11.134889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8bb6c0e38faa'
down_revision: Union[str, None] = '355fa982ae92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assistance_transactions', sa.Column('action_date_year_month', sa.String(), nullable=True))
    op.drop_column('assistance_transactions', 'action_date_month')
    op.add_column('procurement_transactions', sa.Column('action_date_year_month', sa.String(), nullable=True))
    op.drop_column('procurement_transactions', 'action_date_month')
    op.add_column('transactions', sa.Column('action_date_year_month', sa.String(), nullable=True))
    op.drop_column('transactions', 'action_date_month')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transactions', sa.Column('action_date_month', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('transactions', 'action_date_year_month')
    op.add_column('procurement_transactions', sa.Column('action_date_month', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('procurement_transactions', 'action_date_year_month')
    op.add_column('assistance_transactions', sa.Column('action_date_month', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('assistance_transactions', 'action_date_year_month')
    # ### end Alembic commands ###
