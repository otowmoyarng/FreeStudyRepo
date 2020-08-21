from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates
import db
from models import User, Task

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

def admin(request: Request):
    # ユーザとタスクを取得
    # とりあえず今はadminユーザのみ取得
    user = db.session.query(User).filter(User.username == 'admin').first()
    task = db.session.query(Task).filter(Task.user_id == user.id).all()
    db.session.close()
 
    return templates.TemplateResponse('admin.html',
                                      {'request': request,
                                       'user': user,
                                       'task': task})
