

# 🌍 ShopImpact — The Mindful Shopping Companion
**Student Name:** Zene Sophie Anand

**Student ID:** AN02720

**Course:** Artificial Intelligence | Python Programming

**Assessment Type:** Summative Assessment

**Project Title:** Design and Deploy an Interactive Python Application

---

## 📋 Project Overview

**ShopImpact** is an interactive web application built using **Python** and **Streamlit** that transforms expense tracking into a visual, eco-conscious experience.
Unlike standard budget trackers, ShopImpact focuses on the **environmental cost** of shopping. It uses a unique **"Virtual Turtle"** visualization engine—powered by Matplotlib—that draws specific graphics (a green leaf or a red footprint) based on the sustainability of the user's purchase. The project gamifies sustainable living through a "Trophy Case" system, encouraging users to make better choices to unlock digital rewards.

---

## ❗ Problem Statement
While many consumers want to shop sustainably, the immediate environmental impact of a purchase is often invisible.
* **Lack of Feedback:** Shoppers rarely see the CO₂ cost of "Fast Fashion" vs. "Thrift" at the moment of purchase.
* **Boring Tools:** Standard carbon calculators are often dry forms full of numbers, lacking engagement.
This project solves this by providing **instant visual feedback** via the Turtle avatar and **positive reinforcement** through gamified badges.

---

## 🎯 Project Objectives
1. **Core Python Application:** Demonstrate proficiency in lists, dictionaries, loop logic, and external libraries (Pandas, Matplotlib, NumPy).
2. **Interactive Visualization:** Move beyond standard charts by creating a custom drawing engine that renders shapes programmatically.
3. **State Management:** Utilize `st.session_state` to persist user data, history, and unlocked achievements across app reruns.
4. **UI/UX Design:** Implement custom CSS to force a cohesive "Earth & Mint" aesthetic, ensuring high contrast and accessibility.

---

## ✨ Key Features

### 🛒 Core Functionality
* **Smart Inputs:** Fields for Item Name, Category (dropdown), Price, and Brand.
* **Logic-Based Calculation:** Uses a dictionary of multipliers to convert financial cost into environmental cost ($ Price × Impact Factor = CO₂).
* **Better Alternatives:** Automatically detects high-impact categories (like Fast Fashion) and suggests greener options (like ThredUp or Depop).

### 🎮 Gamification: The Trophy Case
Instead of a generic leaderboard, users build a personal collection of achievements.
* **Unlock Logic:** Badges are awarded based on specific conditions (e.g., buying second-hand).
* **Celebration:** Uses `st.balloons()` and toast notifications to celebrate positive user behavior.

### 🎨 The "Virtual Turtle" Engine

A custom-built graphics module using **Matplotlib**:
* **Leaf Drawing:** Renders if the purchase has a low impact multiplier.
* **Footprint Drawing:** Renders if the purchase has a high impact multiplier.
* **Trophy Drawing:** Renders when a new badge is unlocked.
* *Technical Note:* This removes the need for static image files, drawing shapes mathematically using NumPy arrays (Sine/Cosine waves) in real-time.

---

## 🏆 Gamification System (Implemented Logic)
The system rewards specific sustainable actions. The logic checks every purchase against the user's history in `session_state`.
| **Badge Name** | **Icon** | **Unlock Condition** |
| --- | --- | --- |
| **Eco Starter** | 🌱 | Awarded for the first purchase with a very low impact multiplier (≤ 0.1). |
| **Thrift King** | 👑 | Awarded specifically for choosing the "Thrift/Second-hand" category. |
| **Green Investor** | 💎 | Awarded for spending over $50 on a low-impact item (proving sustainability isn't just for cheap items). |

---

## 🎨 User Interface Design
The app enforces a specific theme to ensure readability and brand identity:
* **Background:** A linear gradient from Soft Mint (`#e0f7fa`) to Beige (`#e8f5e9`).
* **Typography:** Dark Midnight Green (`#102A2E`) and Dark Teal (`#004D40`) for headers to ensure high contrast against the light background.
* **Custom Components:**
* **Dropdowns:** Styled with a Dark Teal background and White text for visibility.
* **Metrics:** "Total Spent" and "Total CO₂" use color coding (Teal numbers, Dark Gray labels) for professional clarity.



---

## 🔧 Technical Architecture

### Technologies Used
* **Python:** The backbone logic.
* **Streamlit:** The frontend framework.
* **Matplotlib & NumPy:** The geometry engine for the Turtle drawings.
* **Pandas:** Data manipulation for the history table and area charts.

### Data Structures
* **`IMPACT_MULTIPLIERS` (Dictionary):** Maps categories to CO₂ factors.
* **`session_state.purchases` (List of Dictionaries):** Stores the transaction history (`date`, `item`, `category`, `price`, `co2`).
* **`session_state.badges` (List):** Stores unique unlocked achievements.

---

## 📁 Project Structure

```text
ShopImpact/
│
├── app.py                  # The main application logic and UI
├── requirements.txt        # Dependencies (streamlit, pandas, matplotlib, numpy)
├── README.md               # Documentation
│
└── assets/                 # (Optional) Folder for screenshots if needed

```

---

## 📁 Project Development Stages

### 🧠 Stage 1: Planning & Design
The project began with a whiteboard session to define the target users (Students, Eco-conscious families) and the core "Emotion" of the app: Fun, not guilt. I sketched the initial layout to ensure the Dashboard and Feedback panels were organized.
I then created a low-fidelity wireframe to map out where the "Turtle," the inputs, and the Monthly Dashboard would sit on the screen.

### 🧮 Stage 2: Logic & Graphics
* Developed the `IMPACT_MULTIPLIERS` dictionary to drive the math.
* Built the `show_turtle_drawing()` function. Initially, this was an animation loop, but for performance and stability on the web, it was optimized to render static, transparent figures instantly.

### 🖥️ Stage 3: UI Refinement
* Implemented aggressive CSS injection to fix Streamlit's default dark/light mode conflicts.
* Ensured the "Turtle Canvas" was transparent so drawings looked native to the app background.

### 🚀 Stage 4: Deployment
* Deployed to Streamlit Cloud.
* Verified that `requirements.txt` included `matplotlib` to prevent runtime errors in the cloud environment.

---

## 🚀 Installation & Local Execution
1. **Clone or Download** the project folder.
2. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the Application:**
```bash
streamlit run app.py

```

4. **Access:** Open the local URL provided in the terminal (usually `http://localhost:8501`).

---

## 🌐 Live Web App Link
**https://idai102-1000442-zene-sophie-anand-dxqlgjrqxrw3kpekeefygd.streamlit.app/**

---

## 🌱 Ethical & Social Considerations

* **Positive Reinforcement:** The app deliberately uses "Gamification" (Badges/Trophies) rather than shame to encourage behavior change.
* **Educational Estimates:** The CO₂ values are simplified multipliers intended for awareness, teaching users *relative* impact (e.g., that leather is much higher impact than bamboo) rather than perfect scientific measurement.

---

## 📚 References

* Streamlit Documentation
* Matplotlib Plotting Guidelines
* Python Software Foundation
