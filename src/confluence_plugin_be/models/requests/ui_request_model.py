from typing import Optional
from pydantic import BaseModel


class UIRequest(BaseModel):
    requirement: str
    typography: Optional[str] = None
    palette: Optional[str] = None
