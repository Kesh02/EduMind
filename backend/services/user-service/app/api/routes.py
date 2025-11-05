"""API route definitions"""
from fastapi import APIRouter, HTTPException, status
from app.core.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.get("/")
async def read_root():
    """Root endpoint - health check"""
    logger.info("Root endpoint accessed")
    return {
        "message": "Welcome to EduMind API",
        "status": "healthy",
        "version": "1.0.0"
    }


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "EduMind Backend"
    }
