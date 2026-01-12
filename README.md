# IDAI102-1000442-ZENE-SOPHIE-ANAND

---

# 🌱 ShopImpact: Conscious Shopping Dashboard

**ShopImpact** is a high-visibility, professional data dashboard designed to help consumers bridge the gap between financial spending and environmental responsibility. By calculating the estimated  footprint of everyday purchases, it transforms a standard shopping list into a powerful tool for environmental mindfulness.

---

## 📖 Table of Contents

* [Core Concept](https://www.google.com/search?q=%23-core-concept)
* [Key Features](https://www.google.com/search?q=%23-key-features)
* [Technical Architecture](https://www.google.com/search?q=%23-technical-architecture)
* [Installation Guide](https://www.google.com/search?q=%23-installation-guide)
* [How the Impact is Calculated](https://www.google.com/search?q=%23-how-the-impact-is-calculated)
* [Usage Instructions](https://www.google.com/search?q=%23-usage-instructions)
* [Roadmap](https://www.google.com/search?q=%23-roadmap)

---

## 🎯 Core Concept

The fashion and retail industries are major contributors to global carbon emissions. **ShopImpact** addresses this by providing "at-a-glance" ecological feedback. Built with an "earthy" professional aesthetic, the dashboard provides immediate psychological rewards (status badges) for low-impact spending, encouraging users to stay within a sustainable monthly "carbon budget."

---

## ✨ Key Features

### 1. High-Visibility Impact Metrics

The dashboard features a custom-coded CSS "Metric Card" that highlights the total cumulative  footprint in high-contrast red, ensuring the user's primary impact is never overlooked.

### 2. Intelligent Data Logging

A streamlined sidebar allows for rapid data entry, including:

* **Product Categorization:** Automatically matches inputs against a curated database.
* **Price-Weighted Impact:** Adjusts carbon cost based on the scale of the purchase.
* **Brand Tracking:** Keep a record of which brands you frequent most.

### 3. Gamified Sustainability

Includes a **Goal Progress** engine that monitors a monthly 50kg  limit. Users are assigned dynamic statuses based on their performance:

* 🏆 **Eco Saver:** Under 20kg.
* ⚠️ **Mindful Shopper:** Approaching the limit.
* 🚨 **High Impact:** Exceeding sustainable thresholds.

### 4. Data Portability

Integrated CSV export functionality allows users to download their history for personal record-keeping or detailed analysis in Excel/PowerBI.

---

## 🛠 Technical Architecture

The application is built using a modern Python stack optimized for data transparency:

* **Frontend:** Streamlit (Custom CSS injection for professional branding).
* **Data Processing:** Pandas (Vectorized calculations and dataframe management).
* **State Management:** `st.session_state` for real-time history updates without database overhead.

---

## 🚀 Installation Guide

### Prerequisites

* Python 3.9 or higher
* Pip (Python package manager)

### Step-by-Step Setup

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/shop-impact-dashboard.git
cd shop-impact-dashboard

```


2. **Install Dependencies**
```bash
pip install streamlit pandas

```


3. **Launch the Dashboard**
```bash
streamlit run app.py

```



---

## 📊 How the Impact is Calculated

The dashboard utilizes a "Multiplier-Price" logic to estimate emissions. Each product category is assigned a carbon intensity factor based on average production emissions.

The formula used is:


| Product Type | Multiplier (kg ) | Notes |
| --- | --- | --- |
| **Beef** | 27.0 | High methane and land use impact |
| **Leather Shoes** | 15.2 | Significant tanning and livestock footprint |
| **Cotton T-shirt** | 6.0 | Conventional water and pesticide use |
| **Organic Shirt** | 2.1 | Reduced chemical and water footprint |

---

## 🕹 Usage Instructions

1. **Enter Details:** Use the left sidebar to type in your product (e.g., "Sneakers").
2. **Assign Brand & Price:** Input the purchase price to scale the impact calculation.
3. **Log it:** Click "Add to Dashboard." The main view will update instantly.
4. **Monitor Goals:** Check the "Goal Progress" bar on the right to see how much of your monthly 50kg limit remains.
5. **Export:** At the end of the month, click "Export Report" to save your progress.

---

## 🗺 Roadmap

* [ ] **Global Search:** Integrate an API to pull real-time carbon data for specific brands.
* [ ] **Historical Trends:** Add line charts showing CO2 trends over 6–12 months.
* [ ] **Multi-Currency Support:** Add automated currency conversion for global users.
* [ ] **User Auth:** Allow users to create accounts and save data to a cloud database (Firebase/Supabase).

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👥 Contact

**Project Lead:** Your Name / ShopImpact Ltd.

**Project Link:** [(https://idai102-1000442-zene-sophie-anand-dxqlgjrqxrw3kpekeefygd.streamlit.app/](https://idai102-1000442-zene-sophie-anand-dxqlgjrqxrw3kpekeefygd.streamlit.app/)

---
