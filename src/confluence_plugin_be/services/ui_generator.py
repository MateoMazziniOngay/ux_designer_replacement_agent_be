import openai
import uuid
import base64
import os
from pathlib import Path
from src.confluence_plugin_be.config import OPENAI_API_KEY

IMG_DIR = Path(__file__).resolve().parent.parent / "images"
IMG_DIR.mkdir(parents=True, exist_ok=True)

BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL", "http://localhost:8000")


def generate_ui_image(requirement: str) -> str:
    prompt = process_requirement(requirement)
    image_b64 = request_image(prompt)
    filename = save_image(image_b64)
    return f"{BACKEND_BASE_URL}/images/{filename}"

def process_requirement(requirement: str) -> str:
    # TO DO:    Need to change this, create some prompt engeneering or something xd
    #           I was thinking of something like the folder structure of Diore and Sofi previous project
    #           where they had multiple prompt templates, so maybe we could select them by parameters and 
    #           enhance them with the requirement input to make them more specific.
    prompt_with_requirement = """You are a minimalistic mobile UX/UI designer. 
                                Now you are working a new feature based 
                                on the following requirement: """ + requirement + """
                                Create a UI image for this requirement.
                                The image should be minimalistic,
                                modern and easy to use.
                                The image should be the size of a mobile screen.
                                The background is always white.
                                """
    return prompt_with_requirement

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
