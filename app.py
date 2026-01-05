import streamlit as st
import pandas as pd
import datetime

# --- STAGE 1: PLAN & UI DESIGN ---
st.set_page_config(page_title="ShopImpact Dashboard", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #F1F8E9; }
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 8px; }
    h1, h2, h3 { color: #2E7D32; font-family: 'Helvetica'; }
    </style>
    """, unsafe_allow_html=True)

# --- STAGE 2: UPDATED DATA STRUCTURES ---
# Database for known product impact multipliers 
IMPACT_DATABASE = {
    "leather shoes": 15.2,
    "sneakers": 8.5,
    "t-shirt": 6.0,
    "shirt": 5.5,
    "water bottle": 0.5,
    "beef": 27.0,
    "tofu": 3.0,
    "jeans": 10.5
}

# Default multiplier for unknown products typed by the user 
DEFAULT_MULTIPLIER = 5.0 

# --- STAGE 3: UPDATED INTERACTIVE INTERFACE ---
st.title("🌱 ShopImpact: Your Eco-Shopping Companion")

if 'purchase_history' not in st.session_state:
    st.session_state.purchase_history = []

with st.sidebar:
    st.header("Log a Purchase")
    
    # CHANGE: User can now type the product name manually 
    p_name_input = st.text_input("Product Name", placeholder="e.g., Silk Scarf")
    p_brand = st.text_input("Brand Name", placeholder="e.g., EcoStyle")
    p_price = st.number_input("Price ($)", min_value=0.0, format="%.2f")
    
    if st.button("Calculate & Log Impact"):
        if p_name_input:
            # Clean the input to check against our database
            clean_name = p_name_input.lower().strip()
            
            # Logic: Use database multiplier if found, otherwise use default 
            multiplier = IMPACT_DATABASE.get(clean_name, DEFAULT_MULTIPLIER)
            
            # Calculation: price * multiplier 
            co2_val = multiplier * (p_price / 10 if p_price > 0 else 1)
            
            entry = {
                "Date": datetime.date.today(),
                "Product": p_name_input, # Keeps the user's original capitalization
                "Brand": p_brand,
                "Price": p_price,
                "CO2_kg": round(co2_val, 2)
            }
            st.session_state.purchase_history.append(entry)
            st.success(f"Logged {p_name_input}!")
        else:
            st.error("Please enter a product name.")

# --- STAGE 4: DASHBOARD & FEEDBACK ---
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
    else:
        st.info("Type a product name in the sidebar to begin.")

with col2:
    st.subheader("🍃 Eco-Feedback")
    if st.session_state.purchase_history:
        last_item = st.session_state.purchase_history[-1]
        
        # Turtle Simulation: Visual feedback for positive choices 
        if last_item["CO2_kg"] < 5.0:
            st.markdown("### 🐢 Positive Choice!")
            st.write("The ShopImpact Turtle drew a **Leaf** for you!")
            st.image("https://img.icons8.com/color/96/leaf.png")
        else:
            st.markdown("### 🐢 Footprint Detected")
            st.image("https://img.icons8.com/color/96/footprint.png")

st.divider()
st.caption("Developed for ShopImpact Ltd. | Focus: User-centric Python Design ")
