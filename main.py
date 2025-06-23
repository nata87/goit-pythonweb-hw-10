from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.settings.config import engine, Base
from src.database import models  
from src.auth.routes import router as auth_router
from src.routers.contacts import router as contacts_router
from fastapi_limiter import FastAPILimiter
import redis.asyncio as redis
from src.routers.users import router as users_router


app = FastAPI(title="Contacts API HW10")
app.include_router(users_router)

models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(contacts_router)

@app.on_event("startup")
async def startup():
    r = await redis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(r)

