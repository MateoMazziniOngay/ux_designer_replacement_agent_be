# models/response_models.py
from pydantic import BaseModel

class UIResponse(BaseModel):
    status: str
    image_url: str