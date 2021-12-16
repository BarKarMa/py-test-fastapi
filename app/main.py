from fastapi import FastAPI, applications
import fastapi
from app.handlers import router


def get_application() -> FastAPI:
  application = FastAPI()
  application.include_router(router)
  return application


app = get_application()

