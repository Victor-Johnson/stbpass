from fastapi import FastAPI
from stbpass.routers.house import router as house_router

app = FastAPI()

app.include(house_router,prefix="/houses")
