# API Documentation

## Base URL
```
http://localhost:8000/api
```

## Endpoints

### Products

#### Search Products
```
GET /products/search?q=laptop&platforms=amazon,flipkart&limit=10
```

**Query Parameters:**
- `q` (required): Search query string
- `platforms` (optional): Comma-separated platform names
- `limit` (optional): Number of results (default: 10, max: 100)

**Response:**
```json
{
  "query": "laptop",
  "platforms": ["amazon", "flipkart"],
  "results": [],
  "total": 0
}
```

#### Get Product Details
```
GET /products/{product_id}
```

**Response:**
```json
{
  "id": "product_123",
  "name": "Product Name",
  "details": {}
}
```

#### Get Price History
```
GET /products/{product_id}/prices?days=30
```

**Query Parameters:**
- `days` (optional): Number of days of history (default: 30, max: 365)

**Response:**
```json
{
  "product_id": "product_123",
  "prices": [],
  "total_records": 0
}
```

### Price Comparison

#### Compare Prices
```
GET /compare/{product_id}
```

**Response:**
```json
{
  "product_id": "product_123",
  "comparisons": [],
  "best_deal": null,
  "cheapest": null
}
```

#### Get Best Deals
```
GET /best-deals?limit=10
```

**Response:**
```json
{
  "deals": [],
  "count": 0
}
```

### Alerts

#### Create Alert
```
POST /alerts
```

**Request Body:**
```json
{
  "product_id": "product_123",
  "target_price": 25000,
  "email": "user@example.com"
}
```

**Response:**
```json
{
  "alert_id": "alert_123",
  "product_id": "product_123",
  "target_price": 25000,
  "email": "user@example.com",
  "status": "active"
}
```

#### Get Alerts
```
GET /alerts
```

**Response:**
```json
{
  "alerts": [],
  "count": 0
}
```

#### Delete Alert
```
DELETE /alerts/{alert_id}
```

**Response:**
```json
{
  "message": "Alert deleted successfully"
}
```

## Health Check

```
GET /health
```

**Response:**
```json
{
  "status": "healthy"
}
```
