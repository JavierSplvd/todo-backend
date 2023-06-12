from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    id: str | None
    title: str
    done: bool
    updated_at: datetime | None
    created_at: datetime | None
