from openai import OpenAI
import base64

client = OpenAI()

prompt = "A UI modal with two input fields"

try:
    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        n=1,
        quality="low",
        size="1024x1024"
    )

    image_b64 = response.data[0].b64_json
    with open("test_ui_modal.png", "wb") as f:
        f.write(base64.b64decode(image_b64))

    print("Image saved successfully: test_ui_modal.png")

except Exception as e:
    print("Error generating image:", e)
