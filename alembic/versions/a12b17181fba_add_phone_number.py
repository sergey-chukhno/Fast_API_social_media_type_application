"""add phone number

Revision ID: a12b17181fba
Revises: b34e25003948
Create Date: 2025-03-09 10:37:18.284058

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a12b17181fba'
down_revision: Union[str, None] = 'b34e25003948'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
