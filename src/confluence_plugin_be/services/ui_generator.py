from src.confluence_plugin_be.config import OPENAI_API_KEY

def generate_ui_mock(requirement: str) -> str:
    print(f"[DEBUG] Using OpenAI key: {OPENAI_API_KEY[:5]}********")
    return "/static/mock_ui.png"
#    print(f"Generating UI for: {requirement}")
#    return "/static/mock_ui.png"
