from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from src.settings.config import engine, get_db, settings
from src.database import models
from src.auth.routes import router as auth_router
from src.routers.contacts import router as contacts_router
from fastapi_limiter import FastAPILimiter
import redis.asyncio as redis
from src.routers.users import router as users_router


models.Base.metadata.create_all(bind=engine, checkfirst=True)

app = FastAPI(title="Contacts API HW10")
app.include_router(auth_router)
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(contacts_router, prefix="/contacts", tags=["contacts"])

models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    r = await redis.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
        encoding="utf-8",
        decode_responses=True,
    )
    await FastAPILimiter.init(r)


@app.get("/", name="API root")
def get_index():
    return {"message": "Welcome to contacts API NATA"}


@app.get("/health", name="Service availability")
def get_health_status(db=Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1+1")).fetchone()
        if result is None:
            raise Exception
        return {"message": "API Nata is ready to work"}
    except Exception as e:
        raise HTTPException(status_code=503, detail="Database is not available")