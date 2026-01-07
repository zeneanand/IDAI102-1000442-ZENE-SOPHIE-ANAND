# IDAI102-1000442-ZENE-SOPHIE-ANAND

---

# 🌱 ShopImpact Dashboard

**Transform everyday shopping into a mindful, eco-conscious experience.**

ShopImpact is a high-visibility, professional data dashboard built with Streamlit. It allows users to track the environmental cost (CO₂ footprint) of their purchases in real-time, helping consumers make more sustainable shopping decisions.

---

## 🚀 Features

* **Real-time Impact Tracking:** Instantly calculate the carbon footprint of purchases based on product categories.
* **Professional UI:** Features a custom "earthy" theme with high-visibility metric cards and clean typography.
* **Smart Logging:** Sidebar interface to input product type, brand, and price.
* **Goal Progress:** A visual progress bar that monitors your monthly CO₂ limit (set at 50kg).
* **Dynamic Badges:** Earn statuses like "Eco Saver" or "Mindful Shopper" based on your spending habits.
* **Data Portability:** Export your entire purchase history as a CSV report for external analysis.

---

## 🛠️ Technical Stack

* **Frontend/Backend:** [Streamlit](https://streamlit.io/)
* **Data Handling:** [Pandas](https://pandas.pydata.org/)
* **Styling:** Custom CSS Injection (HTML/CSS)
* **Language:** Python 3.x

---

## 📦 Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/shopimpact-dashboard.git
cd shopimpact-dashboard

```


2. **Install dependencies:**
Ensure you have Python installed, then run:
```bash
pip install streamlit pandas

```


3. **Run the application:**
```bash
streamlit run your_filename.py

```



---

## 📊 How the CO₂ Logic Works

The application uses a weighted multiplier system based on the `IMPACT_DATABASE`. The calculation follows this logic:

**Sample Multipliers:**

* **Beef:** 27.0 (High Impact)
* **Leather Shoes:** 15.2
* **Cotton T-Shirt:** 6.0
* **Organic Shirt:** 2.1 (Low Impact)

---

## 📋 Dashboard Roadmap

* [x] Basic purchase logging and CO₂ calculation.
* [x] CSV Export functionality.
* [x] Progress bar and gamified status badges.
* [ ] **Phase 2:** Integration with a real-time carbon API for more accurate data.
* [ ] **Phase 3:** User authentication to save history across sessions.
* [ ] **Phase 4:** Data visualization (Pie charts for category spending).

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for more accurate carbon multipliers or UI improvements, please feel free to fork the repo and submit a pull request.

**Developed for ShopImpact Ltd. | Conscious Shopping Dashboard Project**

---
