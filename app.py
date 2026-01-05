import streamlit as st
import pandas as pd
import datetime

# --- STAGE 1: PROFESSIONAL UI DESIGN ---
st.set_page_config(page_title="ShopImpact Dashboard", layout="wide")

# Custom CSS for high-visibility metrics and "earthy" professional theme
st.markdown("""
    <style>
    /* Background and global fonts */
    .main { background-color: #f8f9fa; }
    h1, h2, h3 { color: #1b5e20 !important; font-family: 'Inter', sans-serif; }
    
    /* Highlighted Metric Card */
    .metric-card {
        background-color: #ffffff;
        border: 2px solid #e0e0e0;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }
    .metric-value {
        font-size: 56px !important;
        font-weight: 800;
        color: #d32f2f;
    }
    .metric-label {
        font-size: 18px;
        color: #616161;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    /* Sidebar Styling */
    .css-1d391kg { background-color: #e8f5e9; }
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        width: 100%;
        border-radius: 8px;
        height: 3em;
        font-size: 16px;
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

# --- STAGE 3: INTERACTIVE SIDEBAR ---
st.title("🌱 ShopImpact")
st.markdown("### Transform everyday shopping into a mindful, eco-conscious experience.")

with st.sidebar:
    st.header("📝 Log Purchase")
    p_name = st.text_input("Product Type (Type here)", placeholder="e.g., Sneakers")
    p_brand = st.text_input("Brand", placeholder="e.g., EcoStyle")
    p_price = st.number_input("Price (Rs)", min_value=0.0, step=1.0)
    
    if st.button("Add to Dashboard"):
        if p_name:
            lookup = p_name.lower().strip()
            multiplier = IMPACT_DATABASE.get(lookup, DEFAULT_IMPACT)
            # CO2 Calculation logic 
            co2_val = multiplier * (p_price / 10 if p_price > 0 else 1)
            
            st.session_state.purchase_history.append({
                "Date": datetime.date.today().strftime("%Y-%m-%d"),
                "Product": p_name.title(),
                "Brand": p_brand,
                "Price": p_price,
                "CO2_kg": round(co2_val, 2)
            })
            st.toast(f"Logged {p_name}!", icon="🍃")
        else:
            st.error("Please enter a product name.")

# --- STAGE 4: MAIN DASHBOARD ---
if st.session_state.purchase_history:
    df = pd.DataFrame(st.session_state.purchase_history)
    total_co2 = df["CO2_kg"].sum()

    # SECTION: Total Impact (High Visibility)
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Cumulative CO₂ Footprint</div>
            <div class="metric-value">{total_co2:.2f} kg</div>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📑 Purchase Logs")
        st.dataframe(df, use_container_width=True, height=300)
        
        # Download Report Feature 
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Export Report (CSV)",
            data=csv,
            file_name=f"ShopImpact_Report_{datetime.date.today()}.csv",
            mime="text/csv",
        )

    with col2:
        st.subheader("🎯 Goal Progress")
        # Visual Progress Bar replaces Turtle for better visibility
        limit = 50.0
        progress = min(total_co2 / limit, 1.0)
        st.progress(progress)
        st.write(f"Monthly Limit: {total_co2:.1f} / {limit} kg")
        
        # Reward/Badge logic 
        if total_co2 < 20:
            st.success("🏆 Status: Eco Saver of the Month!")
        elif total_co2 < limit:
            st.warning("⚠️ Status: Mindful Shopper")
        else:
            st.error("🚨 Status: High Impact - Try greener alternatives!")

else:
    # Friendly empty state
    st.info("Your dashboard is empty. Use the sidebar to log your first purchase and start tracking your impact!")

st.divider()
st.caption("Developed for ShopImpact Ltd. | Conscious Shopping Dashboard Project ")
