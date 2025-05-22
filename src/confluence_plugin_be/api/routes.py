from fastapi import APIRouter, HTTPException
from confluence_plugin_be.models.requests.ui_request_model import UIRequest
from confluence_plugin_be.models.responses.ui_response_model import UIResponse
from src.confluence_plugin_be.services.ui_generator import generate_ui_image

router = APIRouter()

@router.post("/generate-ui", response_model=UIResponse, tags=["UI Generation"], summary="Generate a UI image from a requirement")
async def generate_ui(req: UIRequest):
    try:
        print("[DEBUG] Received requirement:", req.requirement)
        image_url = generate_ui_image(req.requirement)
        return {"status": "success", "image_url": image_url}
    except Exception as e:
        print("[ERROR] Failed to generate UI image:", str(e))
        raise HTTPException(status_code=500, detail=str(e))
