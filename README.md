# 🧠 Confluence Plugin Backend – FastAPI UI Generator

This project is a backend service built with **FastAPI** to generate UI images from natural language requirements. It follows a clean and scalable structure using modern Python practices and is managed using **PDM**.

## ✅ What This Backend Does

- Accepts a text-based requirement via an HTTP POST request.
- (Eventually) generates a UI image using OpenAI's API (currently mocked).
- Returns a URL to the generated UI image stored in a `images/` folder.
- Provides a `/docs` page for testing via Swagger UI.



## 🗂️ Project Structure & Responsibility
```
confluence-plugin-be/
├── src/
│ └── confluence_plugin_be/
│ ├── main.py # App entry point (FastAPI instance)
│ ├── api/
│ │ └── routes.py # API endpoints (e.g., /generate-ui)
│ ├── models/
│ │ └── request_models.py# Request validation schemas
│ ├── services/
│ │ └── ui_generator.py # Business logic (OpenAI integration)
│ ├── images/ # Folder for returned/generated images
│ └── config.py # Loads secrets like OPENAI_API_KEY
├── tests/
│ └── test_routes.py # (To be implemented)
├── .env # Stores API keys (not committed)
├── pyproject.toml # PDM config and dependencies
└── README.md
```


## 🔄 Request Flow

```text
POST /generate-ui
     │
     ▼
api/routes.py           → Accepts the request and calls the service
models/request_models.py→ Validates the request body using Pydantic
services/ui_generator.py→ Generates or returns a UI image path (mock)
config.py               → Loads the OpenAI API key from .env
images/                 → Contains mock_ui.png (or future generated files)

```

Example Response
```text
{
  "status": "success",
  "image_url": "/images/mock_ui.png"
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
- Replace mock logic with actual image generation using OpenAI API.
- Save generated images dynamically in images/.
