import streamlit as st
import pandas as pd
import datetime

# --- STAGE 1: PLAN & UI DESIGN ---
# Setting earthy colors as per the brief 
st.set_page_config(page_title="ShopImpact Dashboard", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #F1F8E9; }
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 8px; }
    h1, h2, h3 { color: #2E7D32; font-family: 'Helvetica'; }
    </style>
    """, unsafe_allow_html=True)

# --- STAGE 2: DATA LOGIC ---
# Multipliers used to calculate footprint (Price * Multiplier) 
IMPACT_DATABASE = {
    "leather shoes": 15.2,
    "sneakers": 8.5,
    "cotton t-shirt": 6.0,
    "plastic bottle": 0.5,
    "beef": 27.0
}
DEFAULT_IMPACT = 5.0 # Used if the typed product isn't in the database

if 'purchase_history' not in st.session_state:
    st.session_state.purchase_history = []

# --- STAGE 3: INTERACTIVE INTERFACE ---
st.title("🌱 ShopImpact: Conscious Shopping Dashboard")

with st.sidebar:
    st.header("Log a Purchase")
    
    # CHANGED: Use text_input instead of selectbox so it is typeable
    p_name = st.text_input("Product Type", placeholder="e.g., Leather Shoes")
    
    p_brand = st.text_input("Brand Name", placeholder="e.g., EcoBrand")
    p_price = st.number_input("Price ($)", min_value=0.0, format="%.2f")
    
    if st.button("Calculate & Log Impact"):
        if p_name:
            # Logic: Assign multiplier based on text input [cite: 2, 7]
            lookup = p_name.lower().strip()
            multiplier = IMPACT_DATABASE.get(lookup, DEFAULT_IMPACT)
            co2_val = multiplier * (p_price / 10 if p_price > 0 else 1)
            
            entry = {
                "Date": datetime.date.today(),
                "Product": p_name,
                "Brand": p_brand,
                "Price": p_price,
                "CO2_kg": round(co2_val, 2)
            }
            st.session_state.purchase_history.append(entry)
            st.success(f"Successfully logged {p_name}!")
        else:
            st.error("Please enter a product name.")

# --- STAGE 4: DASHBOARD & TURTLE GRAPHICS ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Your Monthly Dashboard")
    if st.session_state.purchase_history:
        df = pd.DataFrame(st.session_state.purchase_history)
        st.dataframe(df, use_container_width=True)
        
        total_co2 = df["CO2_kg"].sum()
        st.metric("Total CO2 Footprint", f"{total_co2:.2f} kg CO2e")
        
        # Awarding Fun Badges based on footprint [cite: 2, 7]
        if total_co2 < 20:
            st.success("🏅 Badge: Eco Saver of the Month!")
    else:
        st.info("Start by typing a product name in the sidebar.")

with col2:
    st.subheader("🍃 Eco-Feedback")
    if st.session_state.purchase_history:
        # Turtle Graphic simulation: Draw a leaf for low impact choices 
        last_impact = st.session_state.purchase_history[-1]["CO2_kg"]
        if last_impact < 5.0:
            st.markdown("### 🐢 Turtle Badge: Leaf Drawn!")
            st.image("https://img.icons8.com/color/96/leaf.png")
        else:
            st.markdown("### 🐢 Turtle Badge: Footprint Drawn")
            st.image("https://img.icons8.com/color/96/footprint.png")

st.divider()
st.caption("Developed for ShopImpact Ltd. | Python Summative Assessment")
