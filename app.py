import streamlit as st
import pandas as pd
import datetime

# --- STAGE 1: PLAN & UI DESIGN ---
# Using earthy colors (greens/beiges) as requested in the brief 
st.set_page_config(page_title="ShopImpact Dashboard", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #F1F8E9; }
    .stButton>button { background-color: #2E7D32; color: white; border-radius: 12px; font-weight: bold; }
    h1, h2, h3 { color: #1B5E20; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stMetric { background-color: #FFFFFF; padding: 15px; border-radius: 10px; border: 1px solid #C8E6C9; }
    </style>
    """, unsafe_allow_html=True)

# --- STAGE 2: DATA LOGIC ---
# Using a dictionary to store impact multipliers for specific keywords 
IMPACT_DATABASE = {
    "leather shoes": 15.2,
    "sneakers": 8.5,
    "cotton t-shirt": 6.0,
    "organic shirt": 2.1,
    "plastic bottle": 0.5,
    "beef": 27.0,
    "bicycle": 1.5
}
DEFAULT_IMPACT = 5.0  # Multiplier for items not in the list

# Initialize lists/session state as required by the rubric [cite: 7]
if 'purchase_history' not in st.session_state:
    st.session_state.purchase_history = []

# --- STAGE 3: INTERACTIVE INTERFACE ---
st.title("🌱 ShopImpact: Eco-Shopping Dashboard")
st.write("Track your purchases and celebrate sustainable habits.")

with st.sidebar:
    st.header("🛒 Log a Purchase")
    
    # REPLACED dropdown with a typeable Textbox 
    p_name = st.text_input("Product Type", placeholder="e.g., Leather Shoes")
    
    p_brand = st.text_input("Brand Name", placeholder="e.g., EcoStyle")
    p_price = st.number_input("Price ($)", min_value=0.0, format="%.2f")
    
    if st.button("Calculate My Impact"):
        if p_name:
            # logic to calculate CO2: price x multiplier 
            lookup = p_name.lower().strip()
            multiplier = IMPACT_DATABASE.get(lookup, DEFAULT_IMPACT)
            co2_val = multiplier * (p_price / 10 if p_price > 0 else 1)
            
            entry = {
                "Date": datetime.date.today().strftime("%Y-%m-%d"),
                "Product": p_name.title(),
                "Brand": p_brand,
                "Price": p_price,
                "CO2_kg": round(co2_val, 2)
            }
            st.session_state.purchase_history.append(entry)
            st.success(f"Successfully logged {p_name}!")
        else:
            st.error("Please enter a product name to continue.")

# --- STAGE 4: DASHBOARD & TURTLE GRAPHICS ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Your Monthly Impact")
    if st.session_state.purchase_history:
        df = pd.DataFrame(st.session_state.purchase_history)
        st.dataframe(df, use_container_width=True)
        
        total_co2 = df["CO2_kg"].sum()
        st.metric("Total CO2 Footprint", f"{total_co2:.2f} kg")
        
        # Badge logic based on user choices 
        if total_co2 < 20:
            st.success("🏅 Badge Earned: Eco Saver of the Month!")
        elif total_co2 < 50:
            st.info("⭐ Badge Earned: Low Impact Shopper")
    else:
        st.info("Your dashboard is empty. Use the sidebar to log your first item.")

with col2:
    st.subheader("🐢 Turtle Graphic")
    if st.session_state.purchase_history:
        # Drawing simulation for the "friendly companion" feel 
        last_impact = st.session_state.purchase_history[-1]["CO2_kg"]
        if last_impact < 5.0:
            st.markdown("**The ShopImpact Turtle drew a Leaf for you!**")
            st.image("https://img.icons8.com/color/96/leaf.png")
        else:
            st.markdown("**The ShopImpact Turtle drew a Footprint.**")
            st.image("https://img.icons8.com/color/96/footprint.png")

st.divider()
st.caption("Developed for ShopImpact Ltd. | Focus: Conscious Consumerism ")
