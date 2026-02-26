"""Adding a new address column in users table.

Revision ID: 797123c666ac
Revises: 
Create Date: 2026-02-26 21:16:40.820019

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '797123c666ac'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # add a new address column in users table.
    op.add_column("users", sa.Column("address", sa.String()))


def downgrade() -> None:
    # Revert the upgrade in case anything goes wrong.
    op.drop_column("users", "address")
