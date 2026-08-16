import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import urllib.parse
from sqlalchemy import create_engine
import os

# Configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "Root@12345"
ENCODED_PASS = urllib.parse.quote_plus(DB_PASS)
DB_NAME = "ecommerce_analytics"
PROJECT_DIR = r"C:\Users\Purushottam\Data_Analytics_Project_Ecommerce"
IMG_DIR = os.path.join(PROJECT_DIR, "images")
os.makedirs(IMG_DIR, exist_ok=True)

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams["font.sans-serif"] = "DejaVu Sans"

engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{ENCODED_PASS}@{DB_HOST}/{DB_NAME}")

# 1. Monthly Revenue Trend Chart
monthly_sql = """
SELECT DATE_FORMAT(order_date, '%Y-%m') AS Month, SUM(total_revenue) AS Revenue, SUM(profit) AS Profit
FROM orders WHERE order_status = 'Delivered'
GROUP BY DATE_FORMAT(order_date, '%Y-%m') ORDER BY Month ASC;
"""
df_monthly = pd.read_sql(monthly_sql, con=engine)

plt.figure(figsize=(12, 5))
plt.plot(df_monthly['Month'], df_monthly['Revenue'], marker='o', linewidth=2.5, color='#1F4E78', label='Revenue ($)')
plt.plot(df_monthly['Month'], df_monthly['Profit'], marker='s', linewidth=2, color='#2E75B6', linestyle='--', label='Profit ($)')
plt.title('Monthly Sales Revenue & Profit Trend (2025-2026)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Month', fontsize=11, fontweight='bold')
plt.ylabel('Amount ($)', fontsize=11, fontweight='bold')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "monthly_sales_trend.png"), dpi=300)
plt.close()

# 2. Product Category Revenue Bar Chart
prod_sql = """
SELECT p.category, SUM(o.total_revenue) AS Revenue
FROM orders o JOIN products p ON o.product_id = p.product_id
WHERE o.order_status = 'Delivered'
GROUP BY p.category ORDER BY Revenue DESC;
"""
df_prod = pd.read_sql(prod_sql, con=engine)

plt.figure(figsize=(8, 5))
ax = sns.barplot(data=df_prod, x='category', y='Revenue', palette='Blues_r')
plt.title('Total Revenue by Product Category', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Category', fontsize=11, fontweight='bold')
plt.ylabel('Revenue ($)', fontsize=11, fontweight='bold')

for p in ax.patches:
    ax.annotate(f"${p.get_height():,.0f}", 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom', fontsize=10, fontweight='bold',
                xytext=(0, 5), textcoords='offset points')

plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "revenue_by_category.png"), dpi=300)
plt.close()

print(f"Data Visualizations saved to: {IMG_DIR}")
