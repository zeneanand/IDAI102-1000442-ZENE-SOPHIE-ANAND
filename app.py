import streamlit as st
import pandas as pd
import datetime

# --- STAGE 1: PLAN & UI DESIGN ---
# Setting earthy colors and inviting interface 
st.set_page_config(page_title="ShopImpact Dashboard", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #F1F8E9; }
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 8px; }
    h1, h2, h3 { color: #2E7D32; font-family: 'Helvetica'; }
    .big-font { font-size:20px !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- STAGE 2: DATA STRUCTURES & LOGIC ---
# Using dictionaries for multipliers and suggestions 
IMPACT_FACTORS = {
    "Leather Shoes": 15.2,
    "Synthetic Sneakers": 8.5,
    "Cotton T-Shirt": 6.0,
    "Organic Cotton Shirt": 2.1,
    "Plastic Water Bottle": 0.5,
    "Reusable Bottle": 0.05,
    "Beef (1kg)": 27.0,
    "Tofu (1kg)": 3.0
}

ETHICAL_ALTERNATIVES = {
    "Leather Shoes": "Consider Vegan Leather or Pinatex (Pineapple fiber).",
    "Cotton T-Shirt": "Look for GOTS-certified Organic Cotton.",
    "Plastic Water Bottle": "Switch to a Stainless Steel refillable bottle.",
    "Beef (1kg)": "Try plant-based proteins to reduce footprint by 90%."
}

# Initialize session state for tracking purchases 
if 'purchase_history' not in st.session_state:
    st.session_state.purchase_history = []

# --- STAGE 3: INTERACTIVE INTERFACE ---
st.title("🌱 ShopImpact: Your Eco-Shopping Companion")
st.write("Transform your everyday shopping into a mindful experience. ")

with st.sidebar:
    st.header("Log a Purchase")
    p_type = st.selectbox("Product Type", list(IMPACT_FACTORS.keys()))
    p_brand = st.text_input("Brand Name", placeholder="e.g., EcoStyle")
    p_price = st.number_input("Price ($)", min_value=0.0, format="%.2f")
    
    if st.button("Calculate & Log Impact"):
        # Calculate impact: price * multiplier 
        co2_val = IMPACT_FACTORS[p_type] * (p_price / 10 if p_price > 0 else 1)
        
        entry = {
            "Date": datetime.date.today(),
            "Product": p_type,
            "Brand": p_brand,
            "Price": p_price,
            "CO2_kg": round(co2_val, 2)
        }
        st.session_state.purchase_history.append(entry)
        st.success("Purchase logged successfully!")

# --- STAGE 4: DASHBOARD & TURTLE GRAPHICS ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Your Monthly Dashboard")
    if st.session_state.purchase_history:
        df = pd.DataFrame(st.session_state.purchase_history)
        st.dataframe(df, use_container_width=True)
        
        total_co2 = df["CO2_kg"].sum()
        st.metric("Total CO2 Footprint", f"{total_co2:.2f} kg CO2e")
        
        # Badge Logic 
        if total_co2 < 15:
            st.success("🏅 Badge Earned: Eco Saver of the Month!")
        elif total_co2 < 40:
            st.info("⭐ Badge Earned: Low Impact Shopper")
    else:
        st.info("No purchases logged yet. Start by adding one in the sidebar!")

with col2:
    st.subheader("🍃 Eco-Feedback")
    if st.session_state.purchase_history:
        last_item = st.session_state.purchase_history[-1]
        
        # Display ethical alternative nudge 
        if last_item["Product"] in ETHICAL_ALTERNATIVES:
            st.warning(f"**Greener Choice:** {ETHICAL_ALTERNATIVES[last_item['Product']]}")
        
        # Simulation of Turtle Graphics 
        # Since standard Turtle doesn't run in Cloud, we use visual indicators
        if last_item["CO2_kg"] < 5.0:
            st.markdown("### 🐢 Positive Choice Badge!")
            st.write("The ShopImpact Turtle drew a **Leaf** for you!")
            st.image("https://img.icons8.com/color/96/leaf.png") # Visual feedback 
        else:
            st.markdown("### 🐢 Footprint Detected")
            st.write("Your choice left a mark. Try a greener alternative next time!")
            st.image("https://img.icons8.com/color/96/footprint.png")

# --- STAGE 5: TESTING & DEPLOYMENT ---
st.divider()
st.caption("Developed for ShopImpact Ltd. | Focus: Real-world usability & ethical design. ")
