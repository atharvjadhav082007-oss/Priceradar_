from datetime import datetime
from typing import Optional

class Product:
    def __init__(
        self,
        id: str,
        name: str,
        description: Optional[str],
        category: str,
        image_url: Optional[str],
        created_at: datetime,
        updated_at: datetime
    ):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.image_url = image_url
        self.created_at = created_at
        self.updated_at = updated_at

class PriceRecord:
    def __init__(
        self,
        platform: str,
        current_price: float,
        original_price: Optional[float],
        discount: Optional[int],
        rating: Optional[float],
        url: str,
        timestamp: datetime
    ):
        self.platform = platform
        self.current_price = current_price
        self.original_price = original_price
        self.discount = discount
        self.rating = rating
        self.url = url
        self.timestamp = timestamp

class PriceAlert:
    def __init__(
        self,
        product_id: str,
        target_price: float,
        email: Optional[str],
        created_at: datetime
    ):
        self.product_id = product_id
        self.target_price = target_price
        self.email = email
        self.created_at = created_at
