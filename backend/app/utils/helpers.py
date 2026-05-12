import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class Logger:
    """Logging utility"""
    
    @staticmethod
    def log_search(query: str, platform: str):
        logger.info(f"Search - Query: {query}, Platform: {platform}")
    
    @staticmethod
    def log_price_update(product_id: str, price: float, platform: str):
        logger.info(f"Price Update - Product: {product_id}, Price: {price}, Platform: {platform}")

class DateUtils:
    """Date and time utilities"""
    
    @staticmethod
    def get_date_range(days: int):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        return start_date, end_date
    
    @staticmethod
    def format_timestamp(dt: datetime) -> str:
        return dt.isoformat()

class PriceUtils:
    """Price calculation utilities"""
    
    @staticmethod
    def calculate_discount(original_price: float, current_price: float) -> int:
        if original_price == 0:
            return 0
        discount = ((original_price - current_price) / original_price) * 100
        return round(discount)
    
    @staticmethod
    def format_price(price: float) -> str:
        return f"₹{price:,.2f}"
