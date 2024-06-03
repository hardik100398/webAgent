from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.utils.playwright_bot import execute_browser_action
import openai

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")



@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/execute")
async def execute_action(command: str = Form(...)):
    try:
        result = await execute_browser_action(command)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
