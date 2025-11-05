"""XAI Prediction Service - FastAPI application for dropout/performance prediction"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="EduMind XAI Prediction Service",
    version="1.0.0",
    description="XAI Prediction Suite with SHAP/LIME explanations",
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
    return {"service": "XAI Prediction Service", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "xai-prediction-service"}

@app.post("/api/v1/predict")
async def predict(data: dict):
    return {
        "prediction": None,
        "explanation": None,
        "message": "XAI prediction endpoints coming soon. Will include SHAP/LIME explanations."
    }
