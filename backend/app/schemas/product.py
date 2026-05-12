from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    category: str
    image_url: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class PriceRecord(BaseModel):
    platform: str
    current_price: float
    original_price: Optional[float] = None
    discount: Optional[int] = None
    rating: Optional[float] = None
    url: str
    timestamp: datetime

class PriceHistory(BaseModel):
    product_id: str
    prices: list[PriceRecord]
    
    class Config:
        from_attributes = True

class PriceAlert(BaseModel):
    product_id: str
    target_price: float
    email: Optional[str] = None
    
    class Config:
        from_attributes = True
