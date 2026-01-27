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

# --- CSS STYLING ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background: linear-gradient(to bottom right, #e0f7fa, #e8f5e9); }
    
    /* Text Colors */
    html, body, [class*="css"] { color: #102A2E; font-family: 'Verdana', sans-serif; }
    h1 { color: #004D40 !important; font-family: 'Comic Sans MS', sans-serif; text-shadow: 1px 1px #80cbc4; }
    h2, h3, h4 { color: #00695c !important; font-weight: 800; }
    
    /* Inputs */
    .stSelectbox label, .stNumberInput label, .stTextInput label, .stTextArea label, .stSlider label {
        color: #00251a !important; font-size: 16px !important; font-weight: bold !important;
    }

    /* Metrics (Numbers = Green, Labels = Blue) */
    div[data-testid="stMetricValue"] { font-size: 2.4rem; color: #1b5e20 !important; font-weight: 900; }
    div[data-testid="stMetricLabel"] { color: #0d47a1 !important; font-weight: bold; font-size: 1.2rem; }

    /* Buttons */
    .stButton>button {
        background-color: #fdd835; color: #000000; border-radius: 20px; border: 2px solid #f9a825;
        font-weight: 900; font-size: 18px; transition: all 0.3s ease;
    }
    .stButton>button:hover { background-color: #ffeb3b; transform: scale(1.05); border-color: #000; }

    /* Cards & Boxes */
    .badge-card {
        background-color: #ffffff; border-left: 10px solid; padding: 15px; border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2); text-align: center; margin-bottom: 10px; color: #212121;
    }
    .badge-green { border-color: #2e7d32; }
    .badge-gold { border-color: #ff8f00; }
