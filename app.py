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

# --- HIGH CONTRAST & VIBRANT CSS ---
st.markdown("""
    <style>
    /* Main Background - Soft Mint */
    .stApp {
        background: linear-gradient(to bottom right, #e0f7fa, #e8f5e9);
    }
    
    /* GLOBAL TEXT COLOR - Dark Midnight Green */
    html, body, [class*="css"] {
        color: #102A2E; 
        font-family: 'Verdana', sans-serif;
    }

    /* HEADERS - Very Dark Teal */
    h1 {
        color: #004D40 !important;
        font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif;
        text-shadow: 1px 1px #80cbc4;
    }
    h2, h3, h4 {
        color: #00695c !important;
        font-weight: 800;
    }

    /* INPUT LABELS - Make them bold and dark */
    .stSelectbox label, .stNumberInput label, .stTextInput label, .stTextArea label, .stSlider label {
        color: #00251a !important;
        font-size: 16px !important;
        font-weight: bold !important;
    }

    /* METRICS - Dark Burnt Orange */
    div[data-testid="stMetricValue"] {
        font-size: 2.2rem;
        color: #bf360c !important; 
        font-weight: 900;
    }
    div[data-testid="stMetricLabel"] {
        color: #37474f !important;
        font-weight: bold;
    }

    /* BUTTONS - High Contrast Yellow */
    .stButton>button {
        background-color: #fdd835;
        color: #000000;
        border-radius: 20px;
        border: 2px solid #f9a825;
        font-weight: 900;
        font-size: 18px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ffeb3b;
        transform: scale(1.05);
        border-color: #000;
    }

    /* BADGE CARDS - Darker Text */
    .badge-card {
        background-color: #ffffff;
        border-left: 10px solid;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        text-align: center;
        margin-bottom: 10px;
        color: #212121;
    }
    .badge-green { border-color: #2e7d32; }
    .badge-gold { border-color: #ff8f00; }
    .badge-red { border-color: #c62828; }

    /* TROPHY CASE STYLE */
    .trophy-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
    }
    .trophy-item {
        background-color: #fff9c4; /* Light Yellow */
        border: 2px solid #fbc02d;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        font-weight: bold;
        color: #f57f17;
    }
    
    /* TIP BOX - High Visibility */
    .tip-box {
        background-color: #e1f5fe;
        border: 2px dashed #01579b;
        border-radius: 15px;
        padding: 15px;
        color: #0d47a1;
        font-weight: 600;
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
if 'badges' not in st.session_state:
    st.session_state.badges = []

# --- ANIMATED TURTLE ENGINE ---
def animate_turtle(drawing_type):
    """
    Simulates a turtle drawing animation using Matplotlib and Streamlit empty placeholder.
    """
    placeholder = st.empty()
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#e0f7fa') 
    
    t = np.linspace(0, 2*np.pi, 100)
    
    # Define shapes
    if drawing_type == "leaf":
        x_data = 16 * np.sin(t)**3
        y_data = (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)) * 1.2
        color = '#1b5e20' # Darker Green
        fill_color = '#a5d6a7'
        msg = "Eco Hero!"
        icon = "🌿"
        
    elif drawing_type == "footprint":
        x_data = 0.5 * np.cos(t)
        y_data = 1.0 * np.sin(t)
        color = '#b71c1c' # Darker Red
        fill_color = '#ef9a9a'
        msg = "High Impact"
        icon = "👣"
        
    else: # Badge
        x_data = np.cos(t * 5) * 5
        y_data = np.sin(t * 5) * 5
        color = '#ff6f00' # Dark Amber
        fill_color = '#fff59d'
        msg = "Badge Unlocked!"
        icon = "🏆"

    # ANIMATION LOOP
    for i in range(1, 101, 5):
        ax.clear()
        ax.set_aspect('equal')
        ax.axis('off')
        ax.plot(x_data[:i], y_data[:i], color=color, linewidth=3)
        ax.scatter(x_data[i-1], y_data[i-1], color=color, s=120, marker='o') 
        placeholder.pyplot(fig, use_container_width=False)
        time.sleep(0.01) 

    # Final filled state
    ax.clear()
    ax.axis('off')
    ax.fill(x_data, y_data, color=fill_color, alpha=0.6)
    ax.plot(x_data, y_data, color=color, linewidth=3)
    ax.text(0, 0, f"{icon}\n{msg}", ha='center', va='center', fontsize=14, fontweight='bold', color='#263238')
    placeholder.pyplot(fig, use_container_width=False)

# --- SIDEBAR TROPHY CASE ---
with st.sidebar:
    st.header("🏆 Your Trophy Case")
    st.markdown("Collect badges by making eco-friendly choices!")
    
    if len(st.session_state.badges) > 0:
        # Display badges in a grid
        cols = st.columns(2)
        for i, badge in enumerate(st.session_state.badges):
            with cols[i % 2]:
                st.markdown(f"""
                <div class="trophy-item">
                    <div style="font-size:30px;">{badge['icon']}</div>
                    {badge['name']}
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("No badges yet. Start shopping sustainably!")
        
    st.markdown("---")
    st.write("**Reset App:**")
    # This block below must be indented correctly
    if st.button("Reset Everything"):
        st.session_state.purchases = []
        st.session_state.total_co2 = 0.0
        st.session_state.badges = []
        st.rerun()

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
        # Dynamic Level Badge
        if avg_co2 < 5:
            b_class, b_name, b_icon = "badge-green", "Eco Warrior", "🌿"
        elif avg_co2 < 15:
            b_class, b_name, b_icon = "badge-gold", "Conscious Buyer", "⭐"
        else:
            b_class, b_name, b_icon = "badge-red", "High Footprint", "👣"
            
        st.markdown(f"""
        <div class="badge-card {b_class}">
            <h3 style="color:#000; margin:0;">{b_icon} Level</h3>
            <p style="font-weight:bold; font-size:18px; margin:0;">{b_name}</p>
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
            co2_val = price * IMPACT_MULTIPLIERS[prod]
            multiplier = IMPACT_MULTIPLIERS[prod]
            
            # Record Purchase
            st.session_state.purchases.append({
                "date": datetime.now().strftime("%H:%M"),
                "product": prod, "price": price, "co2": co2_val
            })
            st.session_state.total_co2 += co2_val
            
            # --- BADGE UNLOCK LOGIC ---
            new_badge = None
            
            # Badge 1: First Eco Choice
            if multiplier <= 0.1:
                if not any(b['name'] == 'Eco Starter' for b in st.session_state.badges):
                    new_badge = {"name": "Eco Starter", "icon": "🌱"}
            
            # Badge 2: Thrift King
            if prod == "Thrift/Second-hand":
                if not any(b['name'] == 'Thrift King' for b in st.session_state.badges):
                    new_badge = {"name": "Thrift King", "icon": "👑"}
            
            # Badge 3: Green Investor
            if price > 50 and multiplier <= 0.1:
                if not any(b['name'] == 'Green Investor' for b in st.session_state.badges):
                    new_badge = {"name": "Green Investor", "icon": "💎"}

            if new_badge:
                st.session_state.badges.append(new_badge)
                st.balloons() # CELEBRATION!
                st.toast(f"🎉 New Badge Unlocked: {new_badge['name']}!", icon=new_badge['icon'])
                st.session_state.animation_trigger = "badge" 
            
            elif multiplier < 0.2:
                st.session_state.animation_trigger = "leaf"
            else:
                st.session_state.animation_trigger = "footprint"
            
            time.sleep(0.5) 
            st.rerun()

    # --- RECOMMENDATIONS & TIPS ---
    st.markdown("<br>", unsafe_allow_html=True)
    if st.session_state.animation_trigger == "footprint" and prod in GREEN_ALTERNATIVES:
        last_co2 = st.session_state.purchases[-1]['co2'] if st.session_state.purchases else 0
        st.error(f"🛑 High Impact Detected! ({last_co2:.1f}kg CO₂)")
        
        # --- DARKER TEXT BOX ---
        st.markdown(f"""
        <div style="background-color: #fffde7; padding: 15px; border-radius: 10px; border: 2px solid #fbc02d; margin-top: 10px;">
            <p style="color: #004d40; font-weight: 800; font-size: 18px; margin: 0;">
                ✅ Try these greener options instead:
            </p>
            <p style="color: #000000; font-weight: bold; font-size: 16px; margin-top: 5px;">
                {', '.join(GREEN_ALTERNATIVES[prod])}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
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
        <div style="text-align:center; padding: 50px; border: 3px dashed #00695c; border-radius: 20px; background-color: rgba(255,255,255,0.5);">
            <h1 style="font-size: 50px;">🐢</h1>
            <p style="font-weight:bold; font-size:18px;">I'm waiting to draw your impact!</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
# --- CHARTS ---
st.subheader("📊 Visual Analytics")
if st.session_state.purchases:
    chart_data = pd.DataFrame(st.session_state.purchases)
    
    tab1, tab2 = st.tabs(["📉 CO₂ Trend", "📋 Purchase History"])
    
    with tab1:
        st.area_chart(chart_data.reset_index(), x='index', y='co2', color="#004d40")
        
    with tab2:
        st.dataframe(chart_data, use_container_width=True)

st.markdown("---")

# --- FEEDBACK FORM ---
st.subheader("💌 We value your feedback!")
st.write("Help us make ShopImpact better for everyone.")

with st.form("feedback_form"):
    c_feed1, c_feed2 = st.columns(2)
    with c_feed1:
        name = st.text_input("Name (Optional)")
        rating = st.slider("Rate your experience (1-5)", 1, 5, 5)
    with c_feed2:
        comments = st.text_area("Any suggestions or features you'd like?")
        
    submit_feedback = st.form_submit_button("Submit Feedback")
    
    if submit_feedback:
        st.success("✅ Thank you for your feedback! We are listening.")
        st.toast("Feedback received!", icon="📩")
        
        
    


