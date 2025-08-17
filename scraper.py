import json
import os

# Example deals data (replace this with your scraping logic)
deals = [
    {"item": "Coke 1L", "price": 10, "discount": "95%"},
    {"item": "Pepsi 1L", "price": 12, "discount": "92%"},
]

os.makedirs("data", exist_ok=True)
with open("data/deals.json", "w") as f:
    json.dump(deals, f, indent=2)
