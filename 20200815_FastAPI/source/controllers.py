from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

# FastAPIの宣言
app = FastAPI(
    title='FastAPIでつくるtoDoアプリケーション',
    description='FastAPIチュートリアル：FastAPI(とstarlette)でシンプルなtoDoアプリを作りましょう．',
    version='0.9 beta'
)

# テンプレートの宣言
# templates = Jinja2Templates(directory='templates')
templates = Jinja2Templates(directory='C:\\Users\\UT\\Documents\\FreeStudyRepo\\20200815_FastAPI\\source\\templates')
jinja_env = templates.env

def index(request : Request):
    # return {'request' : 'request'}
    return templates.TemplateResponse('index.html',
                                      {'request' : request})

def admin(request : Request):
    return {'request' : 'request', 'username' : 'admin'}
    # return templates.TemplateResponse('admin.html',
    #                                   {'request' : request,
    #                                     'username' : 'admin'
    #                                   })
