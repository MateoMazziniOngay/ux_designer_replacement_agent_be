import openai
import uuid
import base64
from pathlib import Path

from src.confluence_plugin_be.config import OPENAI_API_KEY

IMG_DIR = Path(__file__).resolve().parent.parent / "images"


def generate_ui_image(
    requirement: str, typography: str | None = None, palette: str | None = None
) -> str:
    """Generate a UI image given a requirement and optional style hints."""
    prompt = process_requirement(requirement, typography=typography, palette=palette)
    image_b64 = request_image(prompt)
    filename = save_image(image_b64)
    return f"/images/{filename}"


def process_requirement(
    requirement: str, *, typography: str | None = None, palette: str | None = None
) -> str:
    """Build the prompt text for the image generation request."""
    prompt_lines = [
        "You are a mobile UX/UI designer.",
        f"Requirement: {requirement}",
    ]
    if typography:
        prompt_lines.append(f"Typography: {typography}")
    if palette:
        prompt_lines.append(f"Color palette: {palette}")

    prompt_lines.append(
        "Create a UI mockup that follows these guidelines and is suitable for a Confluence page."
    )

    return "\n".join(prompt_lines)


def request_image(prompt: str) -> str:
    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="b64_json",
    )
    return response.data[0].b64_json


def save_image(b64_image: str) -> str:
    image_data = base64.b64decode(b64_image)
    filename = f"{uuid.uuid4()}.png"
    image_path = IMG_DIR / filename

    with open(image_path, "wb") as f:
        f.write(image_data)

    return filename
