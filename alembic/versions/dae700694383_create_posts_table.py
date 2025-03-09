"""create posts table

Revision ID: dae700694383
Revises: 
Create Date: 2025-03-09 08:38:39.500794

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dae700694383'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True), 
                    sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
    pass
