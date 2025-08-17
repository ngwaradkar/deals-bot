import json
from pathlib import Path

def fetch_deals():
    # Dummy deals for now
    deals = [
        {"product": "XYZ Chips 100g", "price": 10, "mrp": 120, "discount": 92, "platform": "Blinkit"},
        {"product": "ABC Shampoo 100ml", "price": 15, "mrp": 180, "discount": 91, "platform": "Instamart"},
    ]
    Path("data").mkdir(exist_ok=True)
    Path("data/deals.json").write_text(json.dumps(deals, indent=2), encoding="utf-8")

if __name__ == "__main__":
    fetch_deals()
