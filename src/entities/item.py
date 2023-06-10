from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    id: str | None
    name: str
    updated_at: datetime | None
    created_at: datetime | None
