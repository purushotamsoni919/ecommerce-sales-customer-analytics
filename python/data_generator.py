import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Output directory
DATA_DIR = r"C:\Users\Purushottam\Data_Analytics_Project_Ecommerce\data"
os.makedirs(DATA_DIR, exist_ok=True)

# 1. Customers Dataset
cities = ["Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Pune"]
states = ["Maharashtra", "Delhi", "Karnataka", "Telangana", "Gujarat", "Tamil Nadu", "West Bengal", "Maharashtra"]
city_state_map = dict(zip(cities, states))

segment = ["Consumer", "Corporate", "Home Office"]
segment_weights = [0.55, 0.30, 0.15]

first_names = ["Aarav", "Ananya", "Rohan", "Priya", "Vikram", "Neha", "Rahul", "Sneha", "Karan", "Pooja", 
               "Amit", "Divya", "Siddharth", "Meera", "Aditya", "Riya", "Nikhil", "Tanvi", "Varun", "Isha"]
last_names = ["Sharma", "Verma", "Patel", "Rao", "Gupta", "Nair", "Deshmukh", "Chowdhury", "Reddy", "Joshi"]

customers = []
for i in range(1, 201):
    c_id = f"CUST-{1000 + i}"
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    city = random.choice(cities)
    state = city_state_map[city]
    seg = np.random.choice(segment, p=segment_weights)
    signup_date = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 365))
    customers.append({
        "customer_id": c_id,
        "customer_name": name,
        "city": city,
        "state": state,
        "segment": seg,
        "signup_date": signup_date.strftime("%Y-%m-%d")
    })

df_customers = pd.DataFrame(customers)
df_customers.to_csv(os.path.join(DATA_DIR, "raw_customers.csv"), index=False)

# 2. Products Dataset
products = [
    {"product_id": "PROD-101", "product_name": "Wireless Noise-Canceling Headphones", "category": "Electronics", "unit_price": 149.99, "cost_price": 85.00},
    {"product_id": "PROD-102", "product_name": "Ergonomic Mechanical Keyboard", "category": "Electronics", "unit_price": 89.50, "cost_price": 45.00},
    {"product_id": "PROD-103", "product_name": "UltraWide Gaming Monitor 27-inch", "category": "Electronics", "unit_price": 329.00, "cost_price": 210.00},
    {"product_id": "PROD-104", "product_name": "Precision Optical Wireless Mouse", "category": "Electronics", "unit_price": 39.99, "cost_price": 18.00},
    {"product_id": "PROD-105", "product_name": "Adjustable Aluminium Laptop Stand", "category": "Accessories", "unit_price": 45.00, "cost_price": 20.00},
    {"product_id": "PROD-106", "product_name": "USB-C Multi-Port Hub", "category": "Accessories", "unit_price": 29.99, "cost_price": 12.50},
    {"product_id": "PROD-107", "product_name": "Smart Fitness Tracker Band", "category": "Wearables", "unit_price": 59.90, "cost_price": 28.00},
    {"product_id": "PROD-108", "product_name": "HD Webcam with Dual Microphone", "category": "Electronics", "unit_price": 64.99, "cost_price": 30.00},
    {"product_id": "PROD-109", "product_name": "Leather Executive Desk Mat", "category": "Office", "unit_price": 24.50, "cost_price": 9.00},
    {"product_id": "PROD-110", "product_name": "Ergonomic Mesh Office Chair", "category": "Office", "unit_price": 199.00, "cost_price": 110.00}
]

df_products = pd.DataFrame(products)
df_products.to_csv(os.path.join(DATA_DIR, "raw_products.csv"), index=False)

# 3. Orders Dataset (1,200 orders across 2025-2026)
orders = []
start_date = datetime(2025, 1, 1)
end_date = datetime(2026, 7, 31)
date_span = (end_date - start_date).days

payment_methods = ["Credit Card", "UPI", "Net Banking", "Debit Card"]
payment_weights = [0.40, 0.35, 0.15, 0.10]

order_statuses = ["Delivered", "Delivered", "Delivered", "Delivered", "Shipped", "Cancelled", "Returned"]
status_weights = [0.75, 0.10, 0.05, 0.04, 0.03, 0.02, 0.01] # Most delivered

for i in range(1, 1201):
    order_id = f"ORD-{10000 + i}"
    cust = random.choice(customers)
    prod = random.choice(products)
    
    order_date = start_date + timedelta(days=random.randint(0, date_span))
    qty = np.random.choice([1, 2, 3, 4, 5], p=[0.50, 0.30, 0.12, 0.05, 0.03])
    unit_price = prod["unit_price"]
    discount = round(np.random.choice([0.0, 0.05, 0.10, 0.15, 0.20], p=[0.40, 0.25, 0.20, 0.10, 0.05]), 2)
    
    total_revenue = round(qty * unit_price * (1 - discount), 2)
    profit = round(total_revenue - (qty * prod["cost_price"]), 2)
    
    pay_method = np.random.choice(payment_methods, p=payment_weights)
    status = np.random.choice(order_statuses)
    
    orders.append({
        "order_id": order_id,
        "order_date": order_date.strftime("%Y-%m-%d"),
        "customer_id": cust["customer_id"],
        "product_id": prod["product_id"],
        "quantity": qty,
        "unit_price": unit_price,
        "discount": discount,
        "total_revenue": total_revenue,
        "profit": profit,
        "payment_method": pay_method,
        "order_status": status
    })

df_orders = pd.DataFrame(orders)
df_orders.to_csv(os.path.join(DATA_DIR, "raw_orders.csv"), index=False)

print(f"Generated successfully: {len(df_customers)} customers, {len(df_products)} products, and {len(df_orders)} orders.")
