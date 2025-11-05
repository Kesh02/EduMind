"""Course Service - FastAPI application"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="EduMind Course Service",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"service": "Course Service", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "course-service"}

@app.get("/api/v1/courses")
async def get_courses():
    return {"courses": [], "message": "Course endpoints coming soon"}
