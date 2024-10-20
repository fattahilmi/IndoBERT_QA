# from typing import Union

from fastapi import *
from fastapi.templating import Jinja2Templates
from fastapi.responses import *
from fastapi.encoders import *
# from fastapi.staticfiles import StaticFiles
# from starlette.requests import Request

templates = Jinja2Templates(directory='templates')
# from forms import UserCreateQA
from lang_model import predict

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse("index.html", {'request': {}})

@app.post('/qa/')
async def qa(context: str = Form(...), question: str = Form(...)):
    temp = predict(context, question)
    temp['question'] = question
    temp['context'] = context
    # print(temp)
    results = jsonable_encoder(temp)
    return templates.TemplateResponse("index.html", {"request": results})
    
    