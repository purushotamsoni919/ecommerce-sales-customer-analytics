USE ecommerce_analytics;

-- ====================================================================
-- QUERY 1: EXECUTIVE KPI OVERVIEW
-- Calculate Total Revenue, Total Profit, Total Orders, Average Order Value (AOV), and Overall Profit Margin
-- ====================================================================
SELECT 
    COUNT(DISTINCT order_id) AS Total_Orders,
    COUNT(DISTINCT customer_id) AS Unique_Customers,
    SUM(quantity) AS Total_Units_Sold,
    ROUND(SUM(total_revenue), 2) AS Total_Revenue,
    ROUND(SUM(profit), 2) AS Total_Profit,
    ROUND(AVG(total_revenue), 2) AS Average_Order_Value,
    ROUND((SUM(profit) / SUM(total_revenue)) * 100, 2) AS Profit_Margin_Percentage
FROM orders
WHERE order_status = 'Delivered';

-- ====================================================================
-- QUERY 2: MONTHLY REVENUE & PROFIT TREND
-- Group by Year and Month to track growth trajectory
-- ====================================================================
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS Order_Month,
    COUNT(order_id) AS Monthly_Orders,
    ROUND(SUM(total_revenue), 2) AS Monthly_Revenue,
    ROUND(SUM(profit), 2) AS Monthly_Profit,
    ROUND((SUM(profit) / SUM(total_revenue)) * 100, 2) AS Monthly_Profit_Margin_Pct
FROM orders
WHERE order_status = 'Delivered'
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY Order_Month ASC;

-- ====================================================================
-- QUERY 3: TOP 5 BEST-SELLING PRODUCTS BY REVENUE
-- Join orders with products table
-- ====================================================================
SELECT 
    p.product_name,
    p.category,
    SUM(o.quantity) AS Total_Quantity_Sold,
    ROUND(SUM(o.total_revenue), 2) AS Total_Revenue_Generated,
    ROUND(SUM(o.profit), 2) AS Total_Profit_Generated
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.order_status = 'Delivered'
GROUP BY p.product_name, p.category
ORDER BY Total_Revenue_Generated DESC
LIMIT 5;

-- ====================================================================
-- QUERY 4: REGIONAL SALES PERFORMANCE BY STATE & CITY
-- Join orders with customers table
-- ====================================================================
SELECT 
    c.state,
    c.city,
    COUNT(o.order_id) AS Total_Orders,
    ROUND(SUM(o.total_revenue), 2) AS Regional_Revenue,
    ROUND(SUM(o.profit), 2) AS Regional_Profit
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_status = 'Delivered'
GROUP BY c.state, c.city
ORDER BY Regional_Revenue DESC;

-- ====================================================================
-- QUERY 5: CUSTOMER RFM SEGMENTATION (RECENCY, FREQUENCY, MONETARY)
-- Identify Top VIP Customers
-- ====================================================================
SELECT 
    c.customer_id,
    c.customer_name,
    c.segment,
    MAX(o.order_date) AS Last_Order_Date,
    DATEDIFF('2026-08-01', MAX(o.order_date)) AS Recency_Days,
    COUNT(o.order_id) AS Frequency_Orders,
    ROUND(SUM(o.total_revenue), 2) AS Monetary_Total_Spend
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_status = 'Delivered'
GROUP BY c.customer_id, c.customer_name, c.segment
ORDER BY Monetary_Total_Spend DESC
LIMIT 10;
