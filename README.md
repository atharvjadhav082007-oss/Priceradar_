# Price Radar System

A smart web application designed to compare product prices across multiple online shopping platforms and help users find the best deals.

## Features

- **Real-time Price Comparison**: Search for products and compare prices across Amazon, Flipkart, Myntra, Ajio, and Croma
- **Price History Tracking**: View price trends over time with interactive charts and graphs
- **Price Drop Alerts**: Set target prices and receive notifications when prices drop
- **Product Reviews**: Access aggregated reviews and ratings from multiple platforms
- **Deal Notifications**: Get notified about special offers and discounts

## Tech Stack

### Frontend
- React.js
- Tailwind CSS
- Recharts (for price trend visualization)
- Axios (for API calls)

### Backend
- FastAPI
- MongoDB
- BeautifulSoup (for web scraping)
- Selenium (for dynamic content scraping)

## Project Structure

```
priceradar/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── utils/
│   │   ├── styles/
│   │   ├── App.jsx
│   │   └── index.jsx
│   ├── package.json
│   └── tailwind.config.js
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── services/
│   │   ├── scrapers/
│   │   ├── schemas/
│   │   ├── utils/
│   │   ├── __init__.py
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   ├── .env
│   └── main.py
├── docs/
├── .gitignore
├── docker-compose.yml
└── README.md
```

## Installation

### Prerequisites
- Node.js (v16+)
- Python (v3.9+)
- MongoDB

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python main.py
```

## API Endpoints

### Products
- `GET /api/products/search` - Search for products
- `GET /api/products/{id}` - Get product details
- `GET /api/products/{id}/prices` - Get price history

### Price Comparison
- `GET /api/compare/{product_id}` - Compare prices across platforms
- `POST /api/alerts` - Create price drop alert
- `GET /api/alerts` - Get user alerts

### Scrapers
- `POST /api/scrapers/amazon` - Scrape Amazon
- `POST /api/scrapers/flipkart` - Scrape Flipkart
- `POST /api/scrapers/myntra` - Scrape Myntra
- `POST /api/scrapers/ajio` - Scrape Ajio
- `POST /api/scrapers/croma` - Scrape Croma

## Environment Variables

Create a `.env` file in the backend directory:

```
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=priceradar
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_ORIGINS=http://localhost:3000
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request.

## License

This project is licensed under the MIT License.

## Author

ASEP GROUP 4

## Contact

GitHub: [atharvjadhav082007-oss](https://github.com/atharvjadhav082007-oss)
