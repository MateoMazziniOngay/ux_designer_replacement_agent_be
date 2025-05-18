from pydantic import BaseModel

class UIRequest(BaseModel):
    requirement: str
