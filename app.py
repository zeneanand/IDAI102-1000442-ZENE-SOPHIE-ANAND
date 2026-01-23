import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import datetime

# --- CONFIGURATION & STYLING ---
st.set_page_config(
    page_title="ShopImpact",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- VIBRANT CSS STYLING ---
st.markdown("""
    <style>
    /* Main Background - Soft Mint */
    .stApp {
        background: linear-gradient(to bottom right, #e0f7fa, #e8f5e9);
    }
    
    /* Headers - Ocean Blue */
    h1 {
        color: #006064;
        font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif; /* Playful font */
        text-shadow: 2px 2px #b2dfdb;
    }
    h2, h3 {
        color: #00796b;
    }

    /* Custom Cards for Metrics */
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #ef6c00; /* Vibrant Orange */
    }

    /* Buttons - Sunny Yellow & Rounded */
    .stButton>button {
        background-color: #fdd835;
        color: #3e2723;
        border-radius: 20px;
        border: 2px solid #fbc02d;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ffeb3b;
        transform: scale(1.05);
    }

    /* Badge Cards */
    .badge-card {
        background-color: #ffffff;
        border-left: 10px solid;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 10px;
    }
    .badge-green { border-color: #4caf50; color: #2e7d32; }
    .badge-gold { border-color: #ffb300; color: #ef6c00; }
    .badge-red { border-color: #c62828; color: #c62828; }

    /* Tip Box */
    .tip-box {
        background-color: #e1f5fe;
        border: 2px dashed #0288d1;
        border-radius: 15px;
        padding: 15px;
        color: #01579b;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA & LOGIC ---

IMPACT_MULTIPLIERS = {
    "Fast Fashion": 0.5, "Sustainable Wear": 0.1, "Gadgets/Tech": 0.3,
    "Leather": 0.8, "Thrift/Second-hand": 0.05, "Local Food": 0.1,
    "Imported Food": 0.4, "Plastic Goods": 0.6, "Bamboo/Wood": 0.15
}

GREEN_ALTERNATIVES = {
    "Fast Fashion": ["ThredUp", "Depop", "Local Thrift", "Patagonia"],
    "Gadgets/Tech": ["BackMarket (Refurbished)", "Repair Cafés"],
    "Leather": ["Piñatex (Pineapple)", "Mushroom Leather", "Cork"],
    "Imported Food": ["Farmers Market", "Seasonal Veggies"],
    "Plastic Goods": ["Glass Jars", "Bamboo", "Stainless Steel"],
}

ECO_TIPS = [
    "🐢 Fun Fact: Sea turtles mistake plastic bags for jellyfish!",
    "💡 Tip: LED bulbs use 75% less energy than incandescent ones.",
    "👕 Hack: Extending a garment's life by 9 months reduces carbon waste by 20-30%.",
    "💧 Fact: A dripping tap can waste 5,500 liters of water a year."
]

# Initialize Session State
if 'purchases' not in st.session_state:
    st.session_state.purchases = []
if 'total_co2' not in st.session_state:
    st.session_state.total_co2 = 0.0
if 'animation_trigger' not in st.session_state:
    st.session_state.animation_trigger = None

# --- ANIMATED TURTLE ENGINE ---
def animate_turtle(drawing_type):
    """
    Simulates a turtle drawing animation using Matplotlib and Streamlit empty placeholder.
    """
    placeholder = st.empty()
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#e0f7fa') # Match background
    
    t = np.linspace(0, 2*np.pi, 100)
    
    # Define shapes
    if drawing_type == "leaf":
        x_data = 16 * np.sin(t)**3
        y_data = (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)) * 1.2
        color = '#43a047' # Green
        fill_color = '#a5d6a7'
        msg = "Eco Hero!"
        icon = "🌿"
        
    elif drawing_type == "footprint":
        # Ellipse approximation
        x_data = 0.5 * np.cos(t)
        y_data = 1.0 * np.sin(t)
        color = '#d32f2f' # Red
        fill_color = '#ef9a9a'
        msg = "High Impact"
        icon = "👣"
        
    else: # Badge
        x_data = np.cos(t * 5) * 5
        y_data = np.sin(t * 5) * 5
        color = '#fbc02d' # Gold
        fill_color = '#fff59d'
        msg = "Badge Earned"
        icon = "⭐"

    # ANIMATION LOOP
    # We draw the line in segments to look like a turtle moving
    for i in range(1, 101, 5):
        ax.clear()
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Draw the partial line
        ax.plot(x_data[:i], y_data[:i], color=color, linewidth=3)
        
        # Draw the "Turtle" head at the current point
        ax.scatter(x_data[i-1], y_data[i-1], color=color, s=100, marker='o') 
        
        # Render frame
        placeholder.pyplot(fig, use_container_width=False)
        time.sleep(0.01) # Speed of drawing

    # Final filled state
    ax.clear()
    ax.axis('off')
    ax.fill(x_data, y_data, color=fill_color, alpha=0.6)
    ax.plot(x_data, y_data, color=color, linewidth=3)
    ax.text(0, 0, f"{icon}\n{msg}", ha='center', va='center', fontsize=12, fontweight='bold', color='#37474f')
    placeholder.pyplot(fig, use_container_width=False)

# --- MAIN APP LAYOUT ---

st.title("🐢 ShopImpact")
st.markdown("### *Making Sustainability Fun & Visual*")

# --- TOP STATS ROW ---
if st.session_state.purchases:
    col_a, col_b, col_c = st.columns(3)
    df = pd.DataFrame(st.session_state.purchases)
    avg_co2 = df['co2'].mean()
    
    with col_a:
        st.metric("💸 Total Spent", f"${df['price'].sum():.2f}")
    with col_b:
        st.metric("☁️ Total CO₂", f"{st.session_state.total_co2:.1f} kg")
    with col_c:
        # Dynamic Badge Logic
        if avg_co2 < 5:
            b_class, b_name, b_icon = "badge-green", "Eco Warrior", "🌿"
        elif avg_co2 < 15:
            b_class, b_name, b_icon = "badge-gold", "Conscious Buyer", "⭐"
        else:
            b_class, b_name, b_icon = "badge-red", "High Footprint", "👣"
            
        st.markdown(f"""
        <div class="badge-card {b_class}">
            <h3>{b_icon} Level</h3>
            {b_name}
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("👋 Welcome! Start adding items below to unlock your dashboard.")

st.markdown("---")

# --- MAIN INTERFACE ---
c1, c2 = st.columns([1, 1])

with c1:
    st.subheader("📝 Add Item")
    with st.container():
        prod = st.selectbox("Product", list(IMPACT_MULTIPLIERS.keys()))
        price = st.number_input("Price ($)", min_value=1.0, value=20.0)
        brand = st.text_input("Brand", "Generic")
        
        if st.button("🚀 Calculate Impact"):
            co2 = price * IMPACT_MULTIPLIERS[prod]
            st.session_state.purchases.append({
                "date": datetime.now().strftime("%H:%M"),
                "product": prod, "price": price, "co2": co2
            })
            st.session_state.total_co2 += co2
            
            # Set trigger for animation
            if IMPACT_MULTIPLIERS[prod] < 0.2:
                st.session_state.animation_trigger = "leaf"
            else:
                st.session_state.animation_trigger = "footprint"
            st.rerun()

    # --- RECOMMENDATIONS & TIPS ---
    st.markdown("<br>", unsafe_allow_html=True)
    if st.session_state.animation_trigger == "footprint" and prod in GREEN_ALTERNATIVES:
        st.error(f"🛑 High Impact Detected! ({co2:.1f}kg CO₂)")
        st.markdown(f"**Try these instead:** {', '.join(GREEN_ALTERNATIVES[prod])}")
    
    st.markdown(f"""
    <div class="tip-box">
        {random.choice(ECO_TIPS)}
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.subheader("🎨 Turtle Canvas")
    
    # ANIMATION LOGIC
    if st.session_state.animation_trigger:
        animate_turtle(st.session_state.animation_trigger)
        st.session_state.animation_trigger = None # Reset
    else:
        # Static placeholder when idle
        st.markdown("""
        <div style="text-align:center; padding: 50px; border: 2px dashed #b2dfdb; border-radius: 20px;">
            <h1 style="font-size: 50px;">🐢</h1>
            <p>I'm waiting to draw your impact!</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
# --- CHARTS ---
st.subheader("📊 Visual Analytics")
if st.session_state.purchases:
    chart_data = pd.DataFrame(st.session_state.purchases)
    
    tab1, tab2 = st.tabs(["📉 CO₂ Trend", "📋 Purchase History"])
    
    with tab1:
        st.area_chart(chart_data.reset_index(), x='index', y='co2', color="#009688")
        
    with tab2:
        st.dataframe(chart_data, use_container_width=True)

