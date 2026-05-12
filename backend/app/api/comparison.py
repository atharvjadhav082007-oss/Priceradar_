from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter(prefix="/api", tags=["comparison"])

@router.get("/compare/{product_id}")
async def compare_prices(product_id: str):
    """Compare product prices across all platforms"""
    try:
        # Implementation will be added
        return {
            "product_id": product_id,
            "comparisons": [],
            "best_deal": None,
            "cheapest": None
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/best-deals")
async def get_best_deals(limit: int = 10):
    """Get current best deals"""
    try:
        # Implementation will be added
        return {"deals": [], "count": 0}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
