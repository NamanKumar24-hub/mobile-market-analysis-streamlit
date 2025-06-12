import streamlit as st
import pandas as pd
import base64
from pathlib import Path

st.set_page_config(page_title="Mobile Market Insights | Flipkart", layout="wide")

st.title("📱 Indian Mobile Market Analysis | Billeasy")
st.markdown("By **Naman (naman.k3612@gmail.com)** | Flipkart Dataset")

st.markdown("""
This app showcases:
- 🔍 Market segmentation
- 📊 Power BI visualizations
- 🤖 Machine learning predictions
- 🧾 SQL-based insights
- 📁 Cleaned datasets

---
""")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", [
    "📊 Dashboard Overview",
    "📁 View Cleaned Data",
    "📉 ML Model Summary",
    "🧾 SQL Insight Screenshots",
    "📘 Jupyter Notebooks",
    "📤 Download Data"
])

# Reusable download link function
def file_download_link(file_path, label=None):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    file_name = Path(file_path).name
    download_label = label or f"📄 Download {file_name}"
    href = f'<a href="data:file/octet-stream;base64,{b64}" download="{file_name}">{download_label}</a>'
    return href

# ---------- PAGE 1: Power BI Dashboard ----------
if page == "📊 Dashboard Overview":
    st.subheader("📊 Power BI Insights")

    st.markdown("#### 📌 Q1: What are the different price range segments for mobiles in India?")
    st.image("power_bi_dashboard/assessment_Q1.png")

    st.markdown("#### 🥇 Q1.1: Which segment has the maximum product count?")
    st.image("power_bi_dashboard/assessment_Q1.1.png")

    st.markdown("#### 📌 Q2: Which brand provides the most product offerings?")
    st.image("power_bi_dashboard/assessment_Q2.png")

    st.markdown("#### 🥇 Q2.1: Brand with Maximum Offerings")
    st.image("power_bi_dashboard/assessment_Q2.1.png")

    st.markdown("#### 🔗 Power BI Report Link")
    st.markdown("*Note: Only accessible within organization due to enterprise account.*")
    st.markdown("[🔗 View Power BI Online](https://app.powerbi.com/links/v6JGF41z_a?...)")

    st.markdown("#### 📥 Download Power BI File")
    st.markdown(file_download_link("power_bi_dashboard/mobile_market_insights(FlipKart).pbix", "📊 Download Power BI Report (.pbix)"), unsafe_allow_html=True)

# ---------- PAGE 2: Cleaned Data ----------
elif page == "📁 View Cleaned Data":
    st.subheader("📂 Cleaned Mobile Dataset")
    df = pd.read_csv("cleaned_data/cleaned_mobile_data.csv")
    st.dataframe(df)

    st.subheader("📂 Brand-Model Summary")
    brand_df = pd.read_csv("cleaned_data/brand_model_summary.csv")
    st.dataframe(brand_df)

    st.subheader("📂 Price Segment Ranges")
    price_ranges = pd.read_csv("cleaned_data/price_segment_limits.csv")
    st.dataframe(price_ranges)

# ---------- PAGE 3: ML Model ----------
elif page == "📉 ML Model Summary":
    st.subheader("💡 Machine Learning: Price Prediction Using RandomForest")

    st.markdown("""
    - **Model**: `RandomForestRegressor`
    - **Features**: Brand, Memory, Storage, Rating
    - **Target**: Selling Price
    - **Pipeline**: Label Encoding + Train/Test Split
    """)

    st.markdown("#### 📈 Model Evaluation Metrics")
    st.image("assets/ml_model_performance_metrics.png")

    st.markdown("#### 🔍 Predicted vs Actual")
    st.image("assets/ml_model_prediction.png")

# ---------- PAGE 4: SQL Queries ----------
elif page == "🧾 SQL Insight Screenshots":
    st.subheader("🧾 SQL-Based Business Insights")

    st.markdown("#### 🛠️ Database Initialization & Update")
    st.image("assets/DB_initial_import.png")
    st.image("assets/DB_first_update.png")

    st.markdown("#### 📌 Q3: Which brand caters to all price segments?")
    st.image("assets/assessment_Q3.png")

    st.markdown("#### 📌 Q4: Most Common Specifications Offered")
    st.image("assets/assessment_Q4.png")

    st.markdown("#### 📊 Q5: Additional SQL Insights")
    st.markdown("- Price Segment by Brand")
    st.image("assets/DB_O1_PriceSegment_By_Brand.png")

    st.markdown("- Common Storage Sizes")
    st.image("assets/DB_O2_Common_Storage_Values.png")

    st.markdown("- Average Price + Variant Count")
    st.image("assets/DB_O3_AveragePrice&VariantCount_PerBrand&Model.png")

    st.markdown("- No Discount Products")
    st.image("assets/DB_O4_NO_Discount.png")

    st.markdown("- Brand Dominance per Segment")
    st.image("assets/DB_O5_Brand_Dominance_per_segment.png")

    st.markdown("#### 📥 Download SQL Queries")
    st.markdown(file_download_link("SQLQuery.sql", "🧾 Download SQL Query File (.sql)"), unsafe_allow_html=True)

# ---------- PAGE 5: Notebooks ----------
elif page == "📘 Jupyter Notebooks":
    st.subheader("📘 Jupyter Notebooks")

    st.markdown("#### 📚 Data Wrangling")
    st.markdown("Open [data_wrangling.ipynb](./data_wrangling.ipynb) in your local Jupyter environment.")
    st.markdown(file_download_link("notebooks/data_wrangling.ipynb", "📥 Download data_wrangling.ipynb"), unsafe_allow_html=True)

    st.markdown("#### 🤖 ML Model Training")
    st.markdown("Open [price_prediction_ml_model.ipynb](./price_prediction_ml_model.ipynb)")
    st.markdown(file_download_link("notebooks/price_prediction_ml_model.ipynb", "📥 Download ML Model Notebook"), unsafe_allow_html=True)

# ---------- PAGE 6: Download Center ----------
elif page == "📤 Download Data":
    st.subheader("⬇️ Download Raw Datasets")

    for file in [
        "raw_data/Flipkart data/Flipkart_mobile_brands_scraped_data.csv",
        "raw_data/Flipkart data/Flipkart_Mobiles.csv",
        "raw_data/__MACOSX/Flipkart data/._Flipkart_mobile_brands_scraped_data.csv",
        "raw_data/__MACOSX/Flipkart data/._Flipkart_Mobiles.csv"
    ]:
        st.markdown(file_download_link(file), unsafe_allow_html=True)

    st.subheader("⬇️ Download Cleaned Datasets")

    for file in [
        "cleaned_data/cleaned_mobile_data.csv",
        "cleaned_data/brand_model_summary.csv",
        "cleaned_data/price_segment_limits.csv"
    ]:
        st.markdown(file_download_link(file), unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("🛠️ Built with `Streamlit` | 📦 Project by **Naman (naman.k3612@gmail.com)**")
