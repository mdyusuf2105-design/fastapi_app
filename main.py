from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse
from routes.auth import router as auth_router
from routes.users import router as users_router
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="FastAPI Backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Backend"}

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }

@app.on_event("startup")
async def startup():
    logger.info("FastAPI application started.")

@app.on_event("shutdown")
async def shutdown():
    logger.info("FastAPI application stopped.")

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Exception: {exc}")

    return JSONResponse(
        status_code=500,
        content={
            "message": "Internal Server Error"
        }
    )

app.include_router(auth_router)
app.include_router(users_router)