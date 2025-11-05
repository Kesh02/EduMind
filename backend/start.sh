#!/bin/bash

# Backend Quick Start Script

echo "Backend Quick Start"
echo "================================"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Error : Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "Error : Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Creating .env file from .env.example..."
    cp .env.example .env
    echo ".env file created. Please update it with your configuration."
fi

echo ""
echo "Starting all services with Docker Compose..."
docker-compose up --build

echo ""
echo "All services are running!"
echo ""
echo "Service URLs:"
echo "  - User Service:        http://localhost:8001"
echo "  - Course Service:      http://localhost:8002"
echo "  - Assessment Service:  http://localhost:8003"
echo "  - XAI Prediction:      http://localhost:8004"
echo "  - Learning Style:      http://localhost:8005"
echo "  - Engagement Tracker:  http://localhost:8006"
echo ""
echo "API Documentation:"
echo "  - http://localhost:8001/api/docs (User Service)"
echo "  - http://localhost:8002/api/docs (Course Service)"
echo "  - http://localhost:8003/api/docs (Assessment Service)"
echo "  - http://localhost:8004/api/docs (XAI Prediction)"
echo "  - http://localhost:8005/api/docs (Learning Style)"
echo "  - http://localhost:8006/api/docs (Engagement Tracker)"
echo ""
