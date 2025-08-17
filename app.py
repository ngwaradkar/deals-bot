import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="90%+ Deals Finder", layout="wide")
st.title("🔥 90%+ Discount Deals (Pincode: 412114)")
st.caption("Sources: Swiggy Instamart, Blinkit, Zepto")

data_path = Path("data/deals.json")
if not data_path.exists():
    st.error("No data found. Run scraper.py first.")
else:
    deals = json.loads(data_path.read_text(encoding="utf-8"))
    if not deals:
        st.warning("No 90%+ deals right now.")
    else:
        for d in deals:
            st.markdown(
                f"**{d['product']}** — ₹{d['price']} (MRP ₹{d['mrp']}) • "
                f"**{d['discount']}% off** • _{d['platform']}_"
            )
