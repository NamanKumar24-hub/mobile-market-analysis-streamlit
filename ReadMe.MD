## Assumptions Made:-
---
- Using the 'Flipkart_Mobiles' CSV file for Analysis 
- Data provided caters to the Indian Mobile Market and is comprehensive of the same. 
- Have extended the price segments up to 5 segments, to be more inclusive of the data.


# Project Workflow:-
---

1. Data Preprocessing (Python & Pandas):
- Raw data is cleaned, transformed, and enriched using Python. Key transformations include memory/storage standardization, price segmentation, and null handling.

2. Data Visualization (Power BI):
- The cleansed dataset is loaded into Power BI to create dynamic dashboards with filters and visual insights — including brand coverage, segment distribution, and price-performance comparisons.

3. Data Analysis (SQL):
- Key business questions are answered via SQL queries executed on a structured version of the dataset (SQLite/PostgreSQL), providing deeper insights like most common specs, pricing trends, and rating correlations.

4. Presentation Layer (Streamlit):
- A simple and clean web interface integrates:

- The live Power BI dashboard (via embed link)

- Key takeaways and insights from SQL

- Download option for clean CSV or summary PDF

