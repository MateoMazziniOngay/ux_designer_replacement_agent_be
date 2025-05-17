from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .api.routes import router

app = FastAPI(title="Confluence Plugin Backend")

@app.get("/")
def root():
    return {"message": "FastAPI backend is up"}

app.include_router(router)
app.mount("/static", StaticFiles(directory="src/confluence_plugin_be/static"), name="static")

