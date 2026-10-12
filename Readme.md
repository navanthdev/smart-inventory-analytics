# Smart Inventory & Sales Analytics

## Project Overview
A data analytics project that transforms retail transaction data into actionable business insights using Python, MySQL, and Power BI. The project focuses on sales performance, product revenue, customer behavior, and country-wise sales analysis.

## Business Problem
Retail businesses need to understand which products generate the most revenue, how sales change over time, which countries contribute most to sales, and which customers generate the highest recorded revenue.

This project analyzes historical retail transactions to support data-driven business decisions.

## Dataset
- **Dataset:** UCI Online Retail
- **Original file:** `Online Retail.xlsx`
- **Cleaned transaction rows:** 536,641
- **Distinct invoices:** 25,900

The dataset contains invoice numbers, product codes, product descriptions, quantities, invoice dates, unit prices, customer IDs, and countries.

## Technologies Used
- **Python:** Data processing, cleaning, and exploratory data analysis (EDA)
- **pandas:** Data manipulation and analysis
- **Matplotlib:** Data visualization and trend analysis
- **Seaborn:** Statistical data visualization and distribution analysis
- **MySQL:** Relational data storage and SQL-based analysis
- **Power BI:** Interactive dashboards and business reporting
- **DAX:** Customer revenue measures and segmentation

## Data Processing
- Inspected data types and missing values.
- Removed exact duplicate records.
- Calculated transaction revenue from quantity and unit price.
- Examined missing customer IDs, returns, negative quantities, and unusual price values.
- Loaded the cleaned transaction dataset into MySQL.

## SQL Analysis
- Total recorded revenue and invoice counts
- Monthly revenue trends
- Top-performing products by revenue
- Country-wise revenue comparisons
- Customer-level revenue analysis

## Power BI Dashboard
### Sales & Revenue Analysis
- Total recorded revenue
- Distinct invoice count
- Unique customer count
- Net recorded quantity
- Monthly revenue trend
- Top 10 products by revenue
- Top 10 countries by revenue
- Top 10 customers by recorded revenue
- Date and country slicers

### Customer Insights
- Unique customers by country
- Customer revenue segments: High Value, Medium Value, Low Value, and Zero or Negative

## Data Validation
The loaded MySQL table was verified against the cleaned dataset.

| Metric | Verified value |
|---|---:|
| Transaction rows | 536,641 |
| Distinct invoices | 25,900 |
| Total recorded revenue | 9,726,006.95 |

## Limitations
This project uses historical transaction data. It does not currently contain actual stock-on-hand quantities, reorder thresholds, or live inventory updates. Therefore, it supports sales and customer analytics rather than real-time inventory management.

## Future Improvements
- Develop a FastAPI service to expose selected analytics.
- Automate data ingestion and refresh workflows.
- Add inventory-on-hand and reorder-point data.
- Introduce scheduled Power BI refresh and additional business KPIs.

## Project Outcome
Built an end-to-end retail analytics workflow that combines Python data preparation, MySQL storage and analysis, and Power BI reporting to explore historical sales and customer performance.