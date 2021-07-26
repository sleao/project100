import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from lib.manager import setup

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
manager = setup()


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    status = manager.get_status()
    return templates.TemplateResponse(
        "index.html", {"request": request, "status": status}
    )


@app.get("/run", tags=["API"])
def run():
    manager.run_all()
    return "Updated"


@app.get("/avail", tags=["API"])
def get_avail():
    avails = manager.get_avails()
    return avails


@app.get("/status", tags=["API"])
def get_status():
    status = manager.get_status()
    return status


if __name__ == "__main__":
    import uvicorn

    PORT = os.getenv("PORT", "8000")
    uvicorn.run("main:app", reload=True, port=int(PORT), host="0.0.0.0")
