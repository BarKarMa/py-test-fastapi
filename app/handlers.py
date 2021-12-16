from fastapi import APIRouter, Body, Depends
from app.forms import UserLoginForm


router = APIRouter()

@router.post('/')
def index():
  return {'status': "OK"}


@router.post('/login', name='user:login')
def login(user_form: UserLoginForm = Body(..., embed=True), database= ):
  
  return {'status': "OK"}