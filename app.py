import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(
    page_title="ShopImpact",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS STYLING ---
st.markdown("""
    <style>
    /* FORCE LIGHT THEME BACKGROUND */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom right, #e0f7fa, #e8f5e9);
        color: #000000 !important;
    }
    [data-testid="stSidebar"] {
        background-color: #ffffff;
    }

    /* FORCE ALL STANDARD TEXT TO BLACK */
    h1, h2, h3, h4, h5, h6, p, div, span, label, li {
        color: #000000 !important;
        font-family: 'Verdana', sans-serif;
    }
    
    /* Specific Headers */
    h1 { font-family: 'Comic Sans MS', sans-serif; text-shadow: 1px 1px #80cbc4; color: #004D40 !important; }
    
    /* === DROPDOWN (SELECTBOX) STYLING === */
    /* This targets the box where "Fast Fashion", "Sustainable Wear" etc appear */
    
    /* The main box background */
    div[data-baseweb="select"] > div {
        background-color: #004D40 !important; /* Dark Teal Background */
        border-color: #004D40 !important;
    }
    
    /* The Text inside the box (Selection) - FORCE WHITE */
    div[data-baseweb="select"] span {
        color: #ffffff !important; 
        -webkit-text-fill-color: #ffffff !important;
    }
    
    /* The Dropdown Icon */
    div[data-baseweb="select"] svg {
        fill: #ffffff !important;
    }

    /* The Dropdown Options List (When you click it) */
    ul[data-testid="stSelectboxVirtualDropdown"] li {
        background-color: #004D40 !important;
        color: #ffffff !important;
    }
    
    /* === END DROPDOWN STYLING === */

    /* Input Labels (The text "Category", "Price" etc) */
    .stSelectbox label, .stNumberInput label, .stTextInput label, .stSlider label {
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 16px !important;
    }

    /* Metrics */
    div[data-testid="stMetricValue"] { 
        color: #004d40 !important; /* Dark Teal Numbers */
        font-size: 2.4rem;
        font-weight: 900; 
    }
    div[data-testid="stMetricLabel"] { 
        color: #263238 !important; /* Dark Slate Gray Labels */
        font-weight: 900; 
        font-size: 1.2rem; 
    }

    /* Buttons */
    .stButton>button {
        background-color: #fdd835; 
        color: #000000 !important; 
        border: 2px solid #f9a825;
        font-weight: 900; 
        font-size: 18px;
    }

    /* Cards */
    .badge-card {
        background-color: #ffffff; border-left: 10px solid; padding: 15px; 
        border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.2); 
        text-align: center; margin-bottom: 10px; color: #000000 !important;
    }
    .badge-green { border-color: #2e7d32; }
    .badge-gold { border-color: #ff8f00; }
    .badge-red { border-color: #c62828; }

    .trophy-item {
        background-color: #fff9c4; border: 2px solid #fbc02d; border-radius: 10px;
        padding: 10px; text-align: center; font-weight: bold; color: #000000 !important;
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

if 'purchases' not in st.session_state:
    st.session_state.purchases = []
if 'total_co2' not in st.session_state:
    st.session_state.total_co2 = 0.0
if 'display_trigger' not in st.session_state:
    st.session_state.display_trigger = None
if 'badges' not in st.session_state:
    st.session_state.badges = []

# --- STATIC TURTLE ENGINE (No Loop Animation) ---
def show_turtle_drawing(drawing_type):
    """
    Displays a static drawing instantly using Matplotlib.
    """
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#e0f7fa') 
    
    t = np.linspace(0, 2*np.pi, 100)
    
    if drawing_type == "leaf":
        x = 16 * np.sin(t)**3
        y = (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)) * 1.2
        color, fill, msg, icon = '#1b5e20', '#a5d6a7', "Eco Hero!", "🌿"
    elif drawing_type == "footprint":
        x = 0.5 * np.cos(t)
        y = 1.0 * np.sin(t)
        color, fill, msg, icon = '#b71c1c', '#ef9a9a', "High Impact", "👣"
    else: # Badge
        x = np.cos(t * 5) * 5
        y = np.sin(t * 5) * 5
        color, fill, msg, icon = '#ff6f00', '#fff59d', "Badge Unlocked!", "🏆"

    # Draw Instantly
    ax.fill(x, y, color=fill, alpha=0.6)
    ax.plot(x, y, color=color, linewidth=3)
    ax.text(0, 0, f"{icon}\n{msg}", ha='center', va='center', fontsize=14, fontweight='bold', color='#000000')
    
    return fig

# --- SIDEBAR ---
with st.sidebar:
    st.header("🏆 Your Trophy Case")
    st.markdown("Collect badges by making eco-friendly choices!")
    if st.session_state.badges:
        cols = st.columns(2)
        for i, badge in enumerate(st.session_state.badges):
            with cols[i % 2]:
                st.markdown(f"""
                <div class="trophy-item">
                    <div style="font-size:30px;">{badge['icon']}</div>
                    {badge['name']}
                </div>""", unsafe_allow_html=True)
    else:
        st.info("No badges yet.")
    
    st.markdown("---")
    if st.button("Reset Everything"):
        st.session_state.purchases = []
        st.session_state.total_co2 = 0.0
        st.session_state.badges = []
        st.rerun()

# --- MAIN APP ---
st.title("🐢 ShopImpact")
st.markdown("### *Making Sustainability Fun & Visual*")

# --- STATS ---
if st.session_state.purchases:
    col_a, col_b, col_c = st.columns(3)
    df = pd.DataFrame(st.session_state.purchases)
    avg_co2 = df['co2'].mean()
    
    with col_a: st.metric("💸 Total Spent", f"${df['price'].sum():.2f}")
    with col_b: st.metric("☁️ Total CO₂", f"{st.session_state.total_co2:.1f} kg")
    with col_c:
        if avg_co2 < 5: b_class, b_name, b_icon = "badge-green", "Eco Warrior", "🌿"
        elif avg_co2 < 15: b_class, b_name, b_icon = "badge-gold", "Conscious Buyer", "⭐"
        else: b_class, b_name, b_icon = "badge-red", "High Footprint", "👣"
        st.markdown(f"""
        <div class="badge-card {b_class}">
            <h3 style="color:#000; margin:0;">{b_icon} Level</h3>
            <p style="font-weight:bold; font-size:18px; margin:0;">{b_name}</p>
        </div>""", unsafe_allow_html=True)
else:
    st.info("👋 Welcome! Start adding items below.")

st.markdown("---")

c1, c2 = st.columns([1, 1])

# --- ADD ITEM ---
with c1:
    st.subheader("📝 Add Item")
    with st.container():
        item_name = st.text_input("Item Name", placeholder="e.g. Vintage Jacket")
        category = st.selectbox("Category", list(IMPACT_MULTIPLIERS.keys()))
        price = st.number_input("Price (rs)", min_value=1.0, value=20.0)
        brand = st.text_input("Brand", "Generic")
        
        if st.button("🚀 Calculate Impact"):
            # New Animation: Spinner
            with st.spinner("🐢 Turtle is calculating..."):
                time.sleep(0.8) 
                
            co2_val = price * IMPACT_MULTIPLIERS[category]
            multiplier = IMPACT_MULTIPLIERS[category]
            
            st.session_state.purchases.append({
                "date": datetime.now().strftime("%H:%M"),
                "item": item_name if item_name else "Unknown",
                "category": category,
                "price": price, 
                "co2": co2_val
            })
            st.session_state.total_co2 += co2_val
            
            # Logic
            new_badge = None
            if multiplier <= 0.1 and not any(b['name'] == 'Eco Starter' for b in st.session_state.badges):
                new_badge = {"name": "Eco Starter", "icon": "🌱"}
            if category == "Thrift/Second-hand" and not any(b['name'] == 'Thrift King' for b in st.session_state.badges):
                new_badge = {"name": "Thrift King", "icon": "👑"}
            if price > 50 and multiplier <= 0.1 and not any(b['name'] == 'Green Investor' for b in st.session_state.badges):
                new_badge = {"name": "Green Investor", "icon": "💎"}

            if new_badge:
                st.session_state.badges.append(new_badge)
                st.balloons() 
                st.toast(f"Unlocked: {new_badge['name']}!", icon=new_badge['icon'])
                st.session_state.display_trigger = "badge" 
            elif multiplier < 0.2:
                st.session_state.display_trigger = "leaf"
            else:
                st.session_state.display_trigger = "footprint"
            
            st.rerun()

    # Recommendations
    st.markdown("<br>", unsafe_allow_html=True)
    if st.session_state.display_trigger == "footprint" and category in GREEN_ALTERNATIVES:
        last_co2 = st.session_state.purchases[-1]['co2'] if st.session_state.purchases else 0
        st.error(f"🛑 High Impact Detected! ({last_co2:.1f}kg CO₂)")
        st.markdown(f"""
        <div style="background-color: #fffde7; padding: 15px; border-radius: 10px; border: 2px solid #fbc02d;">
            <p style="color: #000; font-weight: 800; margin: 0;">✅ Try these instead:</p>
            <p style="color: #000; margin-top: 5px;">{', '.join(GREEN_ALTERNATIVES[category])}</p>
        </div>""", unsafe_allow_html=True)
    
    st.markdown(f"<div style='background-color:#e1f5fe; padding:15px; border-radius:10px; border:2px dashed #0288d1; color:#000;'><b>Tip:</b> {random.choice(ECO_TIPS)}</div>", unsafe_allow_html=True)

# --- VISUALS ---
with c2:
    st.subheader("🎨 Turtle Canvas")
    if st.session_state.display_trigger:
        # Show Static Drawing
        fig = show_turtle_drawing(st.session_state.display_trigger)
        st.pyplot(fig, use_container_width=False)
        if st.session_state.display_trigger == "leaf":
            st.balloons()
        else:
            st.markdown("""
            <div style="text-align:center; padding: 50px; border: 3px dashed #00695c; border-radius: 20px;">
                <h1 style="font-size: 50px;">🐢</h1>
                <p style="font-weight:bold; color:black;">Waiting to draw!</p>
            </div>""", unsafe_allow_html=True)
st.markdown("---")
st.subheader("📊 Visual Analytics")
if st.session_state.purchases:
    chart_data = pd.DataFrame(st.session_state.purchases)
    t1, t2 = st.tabs(["📉 Trend", "📋 History"])
    with t1: st.area_chart(chart_data.reset_index(), x='index', y='co2', color="#004d40")
    with t2: st.dataframe(chart_data[['date', 'item', 'category', 'price', 'co2']], use_container_width=True)

st.markdown("---")
st.subheader("💌 Feedback")
st.markdown('<p style="font-weight:bold; color:#000;">Help us make ShopImpact better.</p>', unsafe_allow_html=True)
with st.form("feed"):
    c_f1, c_f2 = st.columns(2)
    with c_f1: 
        st.text_input("Name")
        st.slider("Rate (1-5)", 1, 5, 5)
    with c_f2: st.text_area("Comments")
    if st.form_submit_button("Submit"):
        st.success("Thanks for the feedback!")
