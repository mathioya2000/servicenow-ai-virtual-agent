from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.servicenow_client import search_knowledge_articles
from app.ai_engine import generate_support_response

app = FastAPI(title="ServiceNow AI Virtual Agent")

templates = Jinja2Templates(directory="templates")


class ChatInput(BaseModel):
    user_message: str


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/chat")
def chat(data: ChatInput):
    try:
        kb_articles = search_knowledge_articles(data.user_message)

        ai_response = generate_support_response(
            data.user_message,
            kb_articles
        )

        return {
            "status": "success",
            "user_message": data.user_message,
            "kb_articles_found": len(kb_articles),
            "ai_response": ai_response
        }

    except Exception as e:
        return {
            "status": "error",
            "error_type": type(e).__name__,
            "error_message": str(e)
        }