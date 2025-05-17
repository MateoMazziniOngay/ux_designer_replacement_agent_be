from fastapi import APIRouter
from src.confluence_plugin_be.models.request_models import RequirementInput
from src.confluence_plugin_be.services.ui_generator import generate_ui_mock

router = APIRouter()

@router.post("/generate-ui")
async def generate_ui(req: RequirementInput):
    image_url = generate_ui_mock(req.text)
    return {"status": "success", "image_url": image_url}
