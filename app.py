import streamlit as st
import pandas as pd
import datetime

# --- STAGE 1: PLAN & UI DESIGN ---
st.set_page_config(page_title="ShopImpact Dashboard", layout="wide")

# Enhanced CSS for better visibility of the CO2 Metric
st.markdown("""
    <style>
    .main { background-color: #F1F8E9; }
    .stButton>button { background-color: #2E7D32; color: white; border-radius: 12px; width: 100%; height: 3em; font-size: 18px; }
    h1, h2, h3 { color: #1B5E20; font-family: 'Helvetica Neue', sans-serif; }
    
    /* Highlighted Box for Total CO2 */
    [data-testid="stMetricValue"] {
        font-size: 48px !important;
        color: #D32F2F !important;
    }
    .metric-container {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        border: 2px solid #C8E6C9;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- STAGE 2: DATA LOGIC ---
IMPACT_DATABASE = {
    "leather shoes": 15.2,
    "sneakers": 8.5,
    "cotton t-shirt": 6.0,
    "organic shirt": 2.1,
    "plastic bottle": 0.5,
    "beef": 27.0
}
DEFAULT_IMPACT = 5.0 

if 'purchase_history' not in st.session_state:
    st.session_state.purchase_history = []

# --- STAGE 3: INTERACTIVE INTERFACE ---
st.title("🌱 ShopImpact: Eco-Shopping Dashboard")
st.markdown("### *Your Friendly Companion for Sustainable Habits*")

with st.sidebar:
    st.header("🛒 Log a Purchase")
    # Requirement: Typeable Textbox 
    p_name = st.text_input("Product Type", placeholder="e.g., Leather Shoes")
    p_brand = st.text_input("Brand Name", placeholder="e.g., EcoStyle")
    p_price = st.number_input("Price ($)", min_value=0.0, format="%.2f")
    
    if st.button("Calculate My Impact"):
        if p_name:
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
            st.toast(f"Logged {p_name}!", icon='✅')
        else:
            st.error("Please enter a product name.")

# --- STAGE 4: DASHBOARD & VISIBILITY ---
if st.session_state.purchase_history:
    df = pd.DataFrame(st.session_state.purchase_history)
    total_co2 = df["CO2_kg"].sum()

    # High-Visibility Metric Section
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    st.metric(label="🌍 TOTAL CO2 FOOTPRINT", value=f"{total_co2:.2f} kg")
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📊 Purchase History")
        st.dataframe(df, use_container_width=True)
        
        # Download Feature 
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Detailed Impact Report",
            data=csv,
            file_name=f"ShopImpact_Report_{datetime.date.today()}.csv",
            mime="text/csv",
        )

    with col2:
        st.subheader("🐢 Turtle Feedback")
        # Visual Reward System 
        if total_co2 < 20:
            st.success("🏆 Badge: Eco Saver!")
        
        last_impact = st.session_state.purchase_history[-1]["CO2_kg"]
        if last_impact < 5.0:
            st.markdown("**Choice Impact: Low**")
            st.image("https://img.icons8.com/color/96/leaf.png", caption="Turtle drew a Leaf!")
        else:
            st.markdown("**Choice Impact: High**")
            st.image("https://img.icons8.com/color/96/footprint.png", caption="Turtle drew a Footprint.")
else:
    st.info("Your dashboard is waiting! Type a product name in the sidebar to calculate your impact.")

st.divider()
st.caption("Developed for ShopImpact Ltd. | Python Summative Assessment ")
