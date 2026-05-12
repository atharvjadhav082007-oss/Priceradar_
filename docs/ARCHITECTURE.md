# Architecture Guide

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   Frontend Layer                         │
│  React.js + Tailwind CSS + Recharts                     │
│  (http://localhost:3000)                                │
└────────────────┬────────────────────────────────────────┘
                 │ HTTP/HTTPS (Axios)
┌────────────────▼────────────────────────────────────────┐
│                   API Layer (FastAPI)                    │
│  (http://localhost:8000/api)                            │
│  ├── /products (Search, Details, History)              │
│  ├── /compare (Price Comparison)                        │
│  └── /alerts (Price Alerts)                            │
└────────────────┬────────────────────────────────────────┘
                 │ PyMongo / Motor
┌────────────────▼────────────────────────────────────────┐
│              Data Access Layer                           │
│  ├── Product Service                                    │
│  ├── Comparison Service                                 │
│  └── Alert Service                                      │
└────────────────┬────────────────────────────────────────┘
                 │
┌────────────────┼────────────────────────────────────────┐
│                │      Database Layer                     │
│   ┌────────────▼──────────┐                             │
│   │    MongoDB (27017)    │                             │
│   │  ├── Products         │                             │
│   │  ├── Prices           │                             │
│   │  ├── Price History    │                             │
│   │  └── Alerts           │                             │
│   └───────────────────────┘                             │
└─────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│              Web Scraping Layer                          │
│  ├── Amazon Scraper (BeautifulSoup)                     │
│  ├── Flipkart Scraper (Selenium)                        │
│  ├── Myntra Scraper                                     │
│  ├── Ajio Scraper                                       │
│  └── Croma Scraper                                      │
└──────────────────────────────────────────────────────────┘
```

## Component Structure

### Frontend Components
```
src/
├── components/
│   ├── SearchBar
│   ├── ProductCard
│   ├── PriceComparison
│   ├── PriceChart
│   ├── AlertForm
│   └── Navigation
├── pages/
│   ├── Home
│   ├── SearchResults
│   ├── ProductDetail
│   └── Alerts
├── hooks/
│   └── useData
├── utils/
│   ├── apiClient
│   ├── productService
│   └── constants
└── styles/
    └── globals.css
```

### Backend Services
```
app/
├── api/
│   ├── products.py
│   ├── comparison.py
│   └── alerts.py
├── services/
│   ├── product_service.py
│   ├── comparison_service.py
│   └── alert_service.py
├── models/
│   └── product.py
├── schemas/
│   └── product.py
├── scrapers/
│   └── platform_scrapers.py
└── utils/
    └── helpers.py
```

## Data Models

### Product
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "category": "string",
  "image_url": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### Price Record
```json
{
  "platform": "string",
  "current_price": "float",
  "original_price": "float",
  "discount": "integer",
  "rating": "float",
  "url": "string",
  "timestamp": "datetime"
}
```

### Price Alert
```json
{
  "product_id": "string",
  "target_price": "float",
  "email": "string",
  "created_at": "datetime",
  "status": "string"
}
```

## Technology Stack Details

### Frontend
- **React 18**: UI library
- **Vite**: Build tool
- **Tailwind CSS**: Utility-first CSS framework
- **Recharts**: React charting library
- **Axios**: HTTP client
- **React Router**: Client-side routing

### Backend
- **FastAPI**: Web framework
- **Uvicorn**: ASGI server
- **Pydantic**: Data validation
- **Motor**: Async MongoDB driver
- **BeautifulSoup**: HTML parsing
- **Selenium**: Web automation
- **Aiohttp**: Async HTTP client

### Database
- **MongoDB**: NoSQL database
- Collections: products, prices, alerts, users

### DevOps
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration

## API Flow

1. User enters search query in frontend
2. Frontend sends GET request to `/api/products/search`
3. Backend receives request and triggers scrapers
4. Scrapers fetch data from e-commerce platforms
5. Data is processed and stored in MongoDB
6. Backend returns formatted response to frontend
7. Frontend displays results with price comparison
8. User can set alerts for price drops
9. Backend monitors prices and sends notifications
