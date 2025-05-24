
# from openai import OpenAI
# import uuid
# import base64
# import os
# from pathlib import Path
# from confluence_plugin_be.models.requests.ui_request_model import UIType
# from src.confluence_plugin_be.config import OPENAI_API_KEY

# IMG_DIR = Path(__file__).resolve().parent.parent / "images"
# IMG_DIR.mkdir(parents=True, exist_ok=True)

# PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "ui_prompt_template.md"

# BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL", "http://localhost:8000")

# client = OpenAI()


# def generate_ui_image(requirement: str, ui_type: UIType) -> str:
#     prompt = load_prompt_template(requirement, ui_type)
#     print("[DEBUG] Generated prompt:", prompt)
#     image_b64 = request_image(prompt)
#     filename = save_image(image_b64)
#     return f"{BACKEND_BASE_URL}/images/{filename}"

# def load_prompt_template(requirement: str, ui_type: UIType) -> str:
#     filename = f"{ui_type.value}_ui_prompt.md"
#     path = Path(__file__).resolve().parent.parent / "prompts" / filename
#     template = path.read_text()
#     return template.replace("{{requirement}}", requirement)

# def request_image(prompt: str) -> str:
#     response = client.responses.create(
#         model="gpt-4.1-mini",
#         input=prompt,
#         tools=[{"type": "image_generation"}],
#     )
#     return response.data[0].b64_json

# def save_image(b64_image: str) -> str:
#     image_data = base64.b64decode(b64_image)
#     filename = f"{uuid.uuid4()}.png"
#     image_path = IMG_DIR / filename

#     with open(image_path, "wb") as f:
#         f.write(image_data)

#     return filename
