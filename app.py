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
# The error happened in this block below. 
# It is now fixed with proper closing quotes.
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

    /* METRIC
