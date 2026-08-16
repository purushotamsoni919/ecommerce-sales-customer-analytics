# 📊 Power BI Connection & Dashboard Setup Guide

This guide details how to connect **Power BI Desktop** to your MySQL database and Excel report to build an interactive Data Analytics Dashboard.

---

## Method 1: Direct MySQL Database Connection (Recommended)

1. Open **Power BI Desktop**.
2. On the **Home** tab, click **Get Data** > **MySQL database**.
3. In the MySQL database dialog box:
   - **Server**: `localhost` or `127.0.0.1`
   - **Database**: `ecommerce_analytics`
   - **Data Connectivity mode**: Select **Import**.
4. Click **OK**.
5. When prompted for credentials:
   - Select **Database** on the left menu.
   - **User name**: `root`
   - **Password**: `Root@12345`
6. Select all 3 tables: `customers`, `products`, `orders`.
7. Click **Load** (or **Transform Data** to inspect in Power Query).

> 💡 *Note: Power BI will automatically detect the foreign key relationships between `orders.customer_id` -> `customers.customer_id` and `orders.product_id` -> `products.product_id`!*

---

## Method 2: Excel Workbook Connection

1. In Power BI Desktop, click **Get Data** > **Excel workbook**.
2. Browse to:
   `C:\Users\Purushottam\Data_Analytics_Project_Ecommerce\excel\Ecommerce_Sales_Analytics_Report.xlsx`
3. Select the sheets: `Executive Summary`, `Monthly Trend`, `Product Performance`, `Regional Breakdown`.
4. Click **Load**.

---

## Recommended Power BI Visualizations to Build:

1. **Card Visuals (Top KPIs)**:
   - Total Revenue (`SUM(orders[total_revenue])`)
   - Total Orders (`COUNT(orders[order_id])`)
   - Total Profit (`SUM(orders[profit])`)
   - Profit Margin (`[Total Profit] / [Total Revenue]`)

2. **Line & Clustered Column Chart**:
   - **Axis**: `order_date` (Month)
   - **Values**: `total_revenue` and `profit`

3. **Donut Chart**:
   - **Legend**: `payment_method`
   - **Values**: `total_revenue`

4. **Map / Bar Chart**:
   - **Category**: `customers[state]`
   - **Values**: `total_revenue`
