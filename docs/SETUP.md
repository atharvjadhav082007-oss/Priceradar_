# Setup Guide

## Prerequisites
- Node.js 16+ (for frontend)
- Python 3.9+ (for backend)
- MongoDB 5+ (or Docker for MongoDB)
- Git

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/atharvjadhav082007-oss/Priceradar_.git
cd Priceradar_
```

### 2. Backend Setup

#### Create Virtual Environment
```bash
cd backend
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Configure Environment
```bash
cp .env.example .env
# Edit .env with your configuration
```

#### Start MongoDB (if not using Docker)
```bash
mongod
```

#### Run Backend Server
```bash
python main.py
```

Backend will be available at `http://localhost:8000`

### 3. Frontend Setup

#### Install Dependencies
```bash
cd ../frontend
npm install
```

#### Start Development Server
```bash
npm run dev
```

Frontend will be available at `http://localhost:3000`

## Docker Setup

### Build and Run with Docker Compose
```bash
docker-compose up -d
```

This will start:
- MongoDB on port 27017
- Backend API on port 8000
- Frontend on port 3000

## Verification

1. Visit `http://localhost:3000` in your browser
2. Check API health: `http://localhost:8000/health`
3. API documentation: `http://localhost:8000/docs`

## Troubleshooting

### Port Already in Use
If ports are already in use, modify the port mappings in:
- `docker-compose.yml`
- Frontend: `vite.config.js`
- Backend: `main.py`

### MongoDB Connection Error
Ensure MongoDB is running and the connection string in `.env` is correct.

### CORS Issues
Update `ALLOWED_ORIGINS` in `.env` to include your frontend URL.

## Development

### Frontend Development
- Hot reload enabled by default with Vite
- Tailwind CSS configured for styling
- API calls through Axios client

### Backend Development
- FastAPI auto-reloading in debug mode
- API docs available at `/docs`
- CORS middleware configured

## Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```
