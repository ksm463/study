from fastapi import FastAPI, Request
from todo import todo_router, templates, todo_list

app = FastAPI()


@app.get("/")
async def welcome(request: Request):
    return templates.TemplateResponse(
        "todo.html",
        {
            "request": request,
            "todos": todo_list
        })

app.include_router(todo_router)
