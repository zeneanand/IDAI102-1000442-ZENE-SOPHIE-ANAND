# 🐢 ShopImpact: The Colorful Eco-Tracker

ShopImpact is a vibrant, interactive Python web app designed to make sustainable shopping fun. It combines **real-time data analytics** with **playful "Turtle" animations** to visualize the environmental cost of your purchases.

## 🌟 Key Features
* **🎨 Colorful & Interactive:** A bright, nature-inspired UI (Mint, Ocean Blue, Sun Yellow).
* **🐢 Animated Turtle Graphics:** Watch a virtual turtle draw a "Leaf" (good choice) or "Footprint" (high impact) in real-time.
* **📊 Live Dashboard:** Instant updates on spending and Carbon Footprint.
* **🏆 Badges & Gamification:** Earn "Eco Warrior" status by making green choices.
* **💡 Smart Suggestions:** Get alerts and greener brand alternatives for high-impact items.

---

## 📸 App Screenshots & Design

### 1. The Interface
*(Replace this line with a screenshot of your running app showing the dashboard)*
![Dashboard Screenshot](insert_your_screenshot_here.png)

### 2. Design Wireframes / Sketches
*Below are the initial rough sketches used to design the UI layout and Turtle area.*

**(Instructions: Draw a simple box on paper. Put inputs on left, a turtle on right. Take a photo and link it here)**
![Wireframe Sketch](insert_your_sketch_photo_here.jpg)

---

## 🚀 How to Run

1.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Launch the App:**
    ```bash
    streamlit run app.py
    ```

3.  **Enjoy:** Open the link (usually `localhost:8501`) in your browser.

---

## 🐢 "Turtle" Graphics Logic
Because standard Python `turtle` crashes in web browsers, this app uses a custom **Matplotlib Animation Engine**.
* It calculates geometry for leaves and footprints.
* It uses `time.sleep()` and iterative plotting to simulate the "drawing" motion of a turtle stroke-by-stroke.

---

## 🛠️ Tech Stack
* **Python** (Logic)
* **Streamlit** (Frontend & Interactivity)
* **Matplotlib** (Animation & Graphics)
* **Pandas** (Data Management)

Made with 💚 for a greener planet.
