            import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# --- CONFIGURATION & STYLING ---
st.set_page_config(
    page_title="ShopImpact",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Earthy Tones and "Friendly" UI
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #Fdfcf5; /* Cream/Beige */
    }
    /* Headers */
    h1, h2, h3 {
        color: #264653; /* Dark Blue-Green */
        font-family: 'Helvetica Neue', sans-serif;
    }
    /* Metrics */
    div[data-testid="stMetricValue"] {
        color: #2A9D8F; /* Earthy Green */
    }
    /* Buttons */
    .stButton>button {
        background-color: #E9C46A; /* Earthy Yellow */
        color: #264653;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #F4A261; /* Burnt Orange */
    }
    /* Custom Badge Box */
    .badge-box {
        padding: 20px;
        background-color: #2A9D8F;
        color: white;
        border-radius: 15px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA & LOGIC ---

# Impact Logic: Multiplier represents kg CO2e per $ spent (Simplified estimation)
IMPACT_MULTIPLIERS = {
    "Fast Fashion Clothing": 0.5,
    "Sustainable Clothing": 0.1,
    "Electronics": 0.3,
    "Leather Goods": 0.8,
    "Second-hand/Thrift": 0.05,
    "Local Produce": 0.1,
    "Imported Processed Food": 0.4,
    "Plastic Home Goods": 0.6,
    "Bamboo/Wooden Goods": 0.15
}

GREEN_ALTERNATIVES = {
    "Fast Fashion Clothing": ["Patagonia", "ThredUp", "Local Thrift Stores", "Organic Cotton Brands"],
    "Electronics": ["Back Market (Refurbished)", "Fairphone", "Keep current device longer"],
    "Leather Goods": ["Pinatex (Pineapple Leather)", "Cork Leather", "Recycled Canvas"],
    "Imported Processed Food": ["Local Farmers Market", "Seasonal Veggies", "Bulk Stores"],
    "Plastic Home Goods": ["Glass Containers", "Bamboo Utensils", "Stainless Steel"],
}

ECO_TIPS = [
    "Did you know bamboo grows 10x faster than trees and absorbs more CO2?",
    "Buying second-hand reduces a product's carbon footprint by up to 80%.",
    "Washing clothes in cold water saves 90% of the energy used by washing machines.",
    "Every $1 spent on local produce keeps money in your community and cuts transport emissions."
]

QUOTES = [
    "“The greatest threat to our planet is the belief that someone else will save it.” – Robert Swan",
    "“Buy less, choose well, make it last.” – Vivienne Westwood",
    "“Sustainability is not a goal to be reached but a way of thinking.”"
]

# Initialize Session State
if 'purchases' not in st.session_state:
    st.session_state.purchases = []
if 'total_co2' not in st.session_state:
    st.session_state.total_co2 = 0.0
if 'last_action' not in st.session_state:
    st.session_state.last_action = None

# --- VIRTUAL TURTLE ENGINE (Matplotlib) ---
def draw_virtual_turtle(drawing_type):
    """
    Simulates a turtle drawing using Matplotlib to ensure it works on web browsers.
    """
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Set canvas color to transparent/beige
    fig.patch.set_facecolor('#Fdfcf5')
    
    t = np.linspace(0, 2*np.pi, 100)
    
    if drawing_type == "leaf":
        # Draw a Leaf
        x = 16 * np.sin(t)**3
        y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t) 
        # Modify heart shape to look more leaf-like by stretching
        y = y * 1.2
        ax.fill(x, y, color='#2A9D8F', alpha=0.6)
        ax.plot(x, y, color='#264653', linewidth=2)
        ax.text(0, -5, "Eco Choice!", ha='center', color='white', fontweight='bold')
        
    elif drawing_type == "footprint":
        # Draw a Footprint (High Carbon)
        # Main foot
        ellipse = plt.Circle((0, 0), 0.5, color='#E76F51', alpha=0.7)
        ax.add_patch(ellipse)
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 2)
        # Toes
        for i in range(5):
            toe = plt.Circle(((-0.3 + i*0.15), 0.7 + abs(i-2)*0.05), 0.08, color='#E76F51')
            ax.add_patch(toe)
        ax.text(0, -0.8, "High Impact", ha='center', color='#264653', fontweight='bold')
        
    elif drawing_type == "badge":
        # Draw a Star Badge
        x = np.cos(t * 5) * 5
        y = np.sin(t * 5) * 5
        ax.fill(x, y, color='#E9C46A', alpha=0.8)
        ax.plot(x, y, color='#F4A261', linewidth=3)
        ax.text(0, 0, "ECO\nSAVER", ha='center', va='center', color='#264653', fontweight='bold')

    return fig

# --- MAIN APP LAYOUT ---

st.title("🌿 ShopImpact")
st.markdown("### Your Mindful Shopping Companion")
st.markdown("---")

# Layout: 2 Columns (Input vs Visualization)
col1, col2 = st.columns([1, 1.5])

# --- LEFT COLUMN: INPUTS ---
with col1:
    st.subheader("🛒 Log a Purchase")
    with st.form("purchase_form"):
        product_type = st.selectbox("Product Type", options=list(IMPACT_MULTIPLIERS.keys()))
        brand = st.text_input("Brand Name", placeholder="e.g., Zara, ThriftShop, Apple")
        price = st.number_input("Price ($)", min_value=0.0, step=1.0)
        
        submitted = st.form_submit_button("Calculate Impact")

    if submitted and price > 0:
        multiplier = IMPACT_MULTIPLIERS[product_type]
        co2_impact = price * multiplier
        
        # Save to state
        new_purchase = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "product": product_type,
            "brand": brand,
            "price": price,
            "co2": co2_impact
        }
        st.session_state.purchases.append(new_purchase)
        st.session_state.total_co2 += co2_impact
        
        # Determine Visual Feedback
        if multiplier < 0.2:
            st.session_state.last_action = "leaf"
            st.success(f"Great choice! {random.choice(ECO_TIPS)}")
        else:
            st.session_state.last_action = "footprint"
            st.warning(f"Note: This has a higher footprint. {random.choice(QUOTES)}")

# --- RIGHT COLUMN: VISUALS & TURTLE ---
with col2:
    st.subheader("🎨 Live Impact Visualization")
    
    # 1. Suggestions Logic
    if submitted:
        if product_type in GREEN_ALTERNATIVES and IMPACT_MULTIPLIERS[product_type] > 0.3:
            st.info(f"💡 **Better Alternatives for next time:** Try brands like {', '.join(GREEN_ALTERNATIVES[product_type])}")

    # 2. The "Turtle" Drawing Area
    if st.session_state.last_action:
        st.markdown(f"**Drawing your impact...**")
        fig = draw_virtual_turtle(st.session_state.last_action)
        st.pyplot(fig, use_container_width=False)
    else:
        # Default empty state
        st.markdown("*Log a purchase to see the Eco-Turtle draw!*")
        st.markdown("🐢")

# --- DASHBOARD SECTION ---
st.markdown("---")
st.subheader("📊 Monthly Impact Dashboard")

if len(st.session_state.purchases) > 0:
    df = pd.DataFrame(st.session_state.purchases)
    
    # Metrics Row
    m1, m2, m3 = st.columns(3)
    total_spend = df['price'].sum()
    total_impact = df['co2'].sum()
    
    m1.metric("Total Spent", f"${total_spend:.2f}")
    m2.metric("Est. CO₂ Footprint", f"{total_impact:.2f} kg")
    
    # Badge Logic
    badge_level = "None"
    if total_impact / len(df) < 10: # Average impact low
        badge_level = "Eco Saver of the Month"
        badge_color = "leaf"
    elif total_impact / len(df) < 30:
        badge_level = "Conscious Consumer"
        badge_color = "badge"
    else:
        badge_level = "High Impact Shopper"
        badge_color = "footprint"
        
    with m3:
        st.markdown(f"""
        <div class="badge-box">
            Current Status:<br>{badge_level}
        </div>
        """, unsafe_allow_html=True)

    # Charts
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Spending vs. CO₂ Impact")
        st.bar_chart(df[['price', 'co2']])
    
    with c2:
        st.markdown("#### Recent History")
        st.dataframe(df.sort_values(by="date", ascending=False), height=200)

else:
    st.info("Start logging purchases to see your dashboard update in real-time!")

# --- SIDEBAR EXTRAS ---
with st.sidebar:
    st.header("⚙️ Settings")
    st.write("Toggle settings to customize your experience.")
    
    dark_mode = st.checkbox("Dark Mode Support (System Default)")
    if st.button("Reset All Data"):
        st.session_state.purchases = []
        st.session_state.total_co2 = 0.0
        st.session_state.last_action = None
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 🌍 Daily Inspiration")
    st.markdown(f"*{random.choice(QUOTES)}*")

            
