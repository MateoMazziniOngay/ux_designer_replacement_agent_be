# 🧠 Confluence Plugin Backend – FastAPI UI Generator

This project is a backend service built with **FastAPI** to generate UI images from natural language requirements. It follows a clean and scalable structure using modern Python practices and is managed using **PDM**.

## ✅ What This Backend Does

- Accepts a text-based requirement via an HTTP POST request.
- Generates a UI image using OpenAI's API.
- Returns a URL to the generated image saved under `src/confluence_plugin_be/images/`.
- Provides a `/docs` page for testing via Swagger UI.



## 🗂️ Project Structure & Responsibility
```
confluence-plugin-be/
├── src/
│ └── confluence_plugin_be/
│   ├── api/
│   │   └── routes.py         # API endpoints (e.g., /generate-ui)
│   ├── models/
│   │   ├── requests/
│   │   │   └── ui_request_model.py   # Request validation schema
│   │   └── responses/
│   │       └── ui_response_model.py  # Response schema
│   ├── services/
│   │   └── ui_generator.py   # Calls OpenAI API and saves images
│   ├── config.py             # Loads secrets like OPENAI_API_KEY
│   └── main.py               # App entry point
├── tests/                    # currently empty
├── .env # Stores API keys (not committed)
├── pyproject.toml # PDM config and dependencies
└── README.md
```


## 🔄 Request Flow

```text
POST /generate-ui
     │
     ▼
api/routes.py                      → Accepts the request and calls the service
models/requests/ui_request_model.py→ Validates the request body using Pydantic
services/ui_generator.py           → Calls OpenAI to create an image and save it
config.py                          → Loads the OpenAI API key from .env
images/                            → Stores the generated image files

```

Example Response
```text
{
  "status": "success",
  "image_url": "/images/<generated-filename>.png"
}
```


## 🔐 Environment Setup
Create a .env file in the root directory:
```text
OPENAI_API_KEY=your-openai-api-key-here
```

## 🚀 Running the Project
Install dependencies:
```
pdm install
```
Run the API server:
```
pdm run uvicorn src.confluence_plugin_be.main:app --reload
```
Test it via Swagger UI:
```
http://127.0.0.1:8000/docs
```

## 📌 Notes for Devs
- Use pdm add package_name to manage dependencies.
- Avoid hardcoding secrets — use config.py and .env.
- Keep logic separated: routing, validation, and business logic belong in their own modules.

## 🔜 Next steps
- Improve prompt generation for the OpenAI requests.
- Add automated tests for API routes and image saving.
