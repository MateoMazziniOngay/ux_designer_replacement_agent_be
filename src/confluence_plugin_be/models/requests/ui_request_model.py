from pydantic import BaseModel
from enum import Enum

class UIType(str, Enum):
    web = "web"
    mobile = "mobile"

class UIRequest(BaseModel):
    requirement: str
    ui_type: UIType = UIType.web
