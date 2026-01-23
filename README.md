# 🌿 ShopImpact: Mindful Shopping Companion

ShopImpact is an interactive, colorful web application built with Python and Streamlit. It transforms everyday shopping logging into a mindful, eco-conscious experience. By estimating the CO₂ footprint of planned purchases and visualizing the data with playful "Turtle" graphics, ShopImpact nudges users toward greener habits.

## 🚀 Features

### Compulsory Features
* **Real-time Tracking:** Input product type, brand, and price to see instant results.
* **CO₂ Estimation:** Logic-based calculation utilizing multipliers (e.g., Fast Fashion = High Impact, Second-hand = Low Impact).
* **Interactive Dashboard:** Live visualization of total spend vs. environmental cost.
* **Smart Suggestions:** Automatically suggests ethical alternatives for high-impact items.
* **Gamification:** Awards badges like "Eco Saver" based on shopping behavior.
* **Turtle Graphics:** A custom "Virtual Turtle" engine that draws leaves (good choices) or footprints (heavy impact) directly in the browser.

### Creative & Optional Features
* **Eco Tips & Quotes:** Randomly generated educational snippets to inspire the user.
* **Earthy UI Design:** A custom styling palette (Beiges, Greens, Blues) to evoke nature.
* **State Persistence:** Keeps track of your session data dynamically.

---

## 🛠️ Installation & Setup

### Prerequisites
You need Python installed on your system.

1.  **Clone the Repository** (or save the files provided):
    ```bash
    git clone [https://github.com/yourusername/ShopImpact.git](https://github.com/yourusername/ShopImpact.git)
    cd ShopImpact
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**:
    ```bash
    streamlit run app.py
    ```

4.  **View**: The app will automatically open in your web browser at `http://localhost:8501`.

---

## 📂 Project Structure

ShopImpact/
│
├── app.py              # Main application logic and UI
├── requirements.txt    # List of python libraries required
└── README.md           # Documentation
---

## 🧠 Logic & Calculations

### 1. CO₂ Calculation
The app uses a **Price × Multiplier** approach to estimate impact.
* *Formula:* `Price ($) × Impact Factor = Estimated CO₂ (kg)`
* *Example:* * Sustainable Clothing ($50) × 0.1 = **5 kg CO₂**
    * Fast Fashion ($50) × 0.5 = **25 kg CO₂**

### 2. The "Virtual Turtle"
Standard Python `turtle` graphics do not work in web browsers (headless environments). To solve this, **ShopImpact uses Matplotlib** to simulate turtle drawings.
* It calculates geometry coordinates for leaves and footprints.
* It renders them as plots that look like line drawings.
* This ensures the app works perfectly on Streamlit Cloud without crashing.

### 3. Badge System
Badges are awarded based on the **Average CO₂ per Item**:
* **< 10kg avg:** "Eco Saver of the Month" (Green Leaf)
* **10kg - 30kg avg:** "Conscious Consumer" (Gold Badge)
* **> 30kg avg:** "High Impact Shopper" (Red Footprint)

---

## 🎨 Visual Style
The app uses a custom CSS injection to override Streamlit's defaults:
* **Background:** Cream/Off-white (#Fdfcf5)
* **Accents:** Earthy Green (#2A9D8F) and Burnt Orange (#E76F51)
* **Fonts:** Clean, sans-serif fonts for readability.

---

## 🧪 Testing
We have tested the app with the following scenarios:
1.  **Scenario A (Eco):** $20 Thrift store purchase -> Result: Draws a leaf, low CO2, suggests nothing.
2.  **Scenario B (High Impact):** $100 Leather shoes -> Result: Draws a footprint, high CO2, suggests "Pineapple Leather".
3.  **Dashboard:** Updates instantly after every "Calculate" click.

Enjoy your journey to sustainable shopping! 🌍
