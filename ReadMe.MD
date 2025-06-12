# 📱 Indian Mobile Market Analysis — Flipkart Dataset

### Part of assessment submission | Billeasy

---

## 🔍 Assumptions Made

- The dataset `Flipkart_Mobiles.csv` represents the **Indian smartphone market**.
- The data is assumed to be **comprehensive** and reflective of real mobile listings.
- Extended price segmentation into **five distinct segments** for better inclusiveness.

---

## 🔄 Project Workflow

### 1. 🧹 Data Preprocessing (Python + Pandas)
- Cleaned and standardized mobile specifications (e.g., Memory, Storage).
- Engineered new features like `Price Segment`.
- Handled null values and removed anomalies.
- Final datasets saved in `/cleaned_data/`.

### 2. 📊 Data Visualization (Power BI)
- Built dashboards to visualize:
  - Brand-wise product distribution
  - Segment-based pricing analysis
  - Price vs Rating trends
- Dashboards embedded in the Streamlit app as PNGs and `.pbix` file.

### 3. 🧾 Data Analysis (SQL)
- Ran SQL queries on a structured version of the dataset (SQL Server | SQL).
- Key questions answered:
  - Which brand covers all price segments?
  - What are the most common specs?
  - Which brand dominates which price range?
- SQL queries saved in `SQLQuery.sql`.

### 4. 🌐 Streamlit App (Presentation Layer)
- Interactive web app integrates:
  - 📊 **Power BI Dashboards**
  - 📄 **SQL Query Visuals**
  - 📁 **Downloadable Files**:
    - Cleaned CSVs
    - SQL file
    - Jupyter Notebooks
    - Power BI File (`.pbix`)

---

## 📁 Folder Structure

├── ReadMe.MD
├── SQLQuery.sql
├── assets
│   ├── Billeasy_Side_Logo.png
│   ├── DB_O1_PriceSegment_By_Brand.png
│   ├── DB_O2_Common_Storage_Values.png
│   ├── DB_O3_AveragePrice&VariantCount_PerBrand&Model.png
│   ├── DB_O4_NO_Discount.png
│   ├── DB_O5_Brand_Dominance_per_segment.png
│   ├── DB_first_update.png
│   ├── DB_initial_import.png
│   ├── assessment_Q3.png
│   ├── assessment_Q4.png
│   ├── ml_model_performance_metrics.png
│   └── ml_model_prediction.png
├── cleaned_data
│   ├── brand_model_summary.csv
│   ├── cleaned_mobile_data.csv
│   └── price_segment_limits.csv
├── notebooks
│   ├── data_wrangling.ipynb
│   └── price_prediction_ml_model.ipynb
├── power_bi_dashboard
│   ├── assessment_Q1.1.png
│   ├── assessment_Q1.png
│   ├── assessment_Q2.1.png
│   ├── assessment_Q2.png
│   └── mobile_market_insights(FlipKart).pbix
├── raw_data
│   ├── Flipkart data
│   └── __MACOSX
├── streamlit_app.py
└── venv
    ├── Include
    ├── Lib
    ├── Scripts
    ├── etc
    ├── pyvenv.cfg
    └── share

14 directories, 26 files

👉 [Open Streamlit App](https://mobile-market-analysis-billeasy.streamlit.app/)  

---

## 📥 Downloads Available

Within the app:
- 📁 Cleaned CSV files
- 📘 Jupyter Notebooks
- 🧾 SQL query file
- 📊 Power BI (`.pbix`) file

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io)
- [Pandas](https://pandas.pydata.org)
- [Power BI](https://powerbi.microsoft.com)
- [PostgreSQL](https://www.postgresql.org/)
- [Jupyter Notebook](https://jupyter.org)


---
### 👨‍💻 By [naman.k3612@gmail.com](mailto:naman.k3612@gmail.com)
