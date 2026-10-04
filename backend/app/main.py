from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.analytics import router as analytics_router
from app.api.ai import router as ai_router


app = FastAPI(
    title="Business Analytics & Automation API",
    description="API for business analytics and AI-powered insights",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(analytics_router)
app.include_router(ai_router)


@app.get("/")
def root():
    return {
        "message": "Business Analytics API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }