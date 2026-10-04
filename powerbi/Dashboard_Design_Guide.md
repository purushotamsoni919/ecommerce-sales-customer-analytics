# 🎨 Executive Performance Dashboard Design Blueprint

This blueprint shows you step-by-step how to replicate the **Meta Ad Performance Dashboard layout** (from your reference screenshot) for your **TechTrend E-Commerce Analytics Project**.

---

## 🎨 Step 1: Apply the Matching Modern Theme (1-Click)

We created a custom theme file that matches the soft-blue background, rounded corners, card drop shadows, and vibrant color palette:
[`Modern_Meta_Dashboard_Theme.json`](file:///D:/New%20folder/PK/DATA%20ANALYST/Data_Analytics_Project_Ecommerce/powerbi/Modern_Meta_Dashboard_Theme.json)

1. In **Power BI Desktop**, go to the **View** tab on the top ribbon.
2. In the **Themes** dropdown gallery, click **Browse for themes...** at the bottom.
3. Select:
   `D:\New folder\PK\DATA ANALYST\Data_Analytics_Project_Ecommerce\powerbi\Modern_Meta_Dashboard_Theme.json`
4. Click **Open**. Your canvas will instantly update with the exact background color (`#EDF2F9`), rounded card corners, and modern color palette!

---

## 📐 Step 2: The Right-Hand Blue Filter Sidebar

In your reference image, there is a full-height vibrant Blue sidebar on the right side:

1. Click **Insert** tab > **Shapes** > select **Rectangle**.
2. Position it along the right edge:
   - Width: ~18% to 20% of canvas width.
   - Height: 100% of canvas height (top to bottom).
3. In the **Format Shape** pane on the right:
   - **Fill color**: `#1877F2` (Royal Blue) or `#0066FF`.
   - **Border**: Off.
   - **Rounded corners**: 12px (or leave straight on the right edge).
4. Add a **Text Box** inside the top of the sidebar:
   - Text: `🛍️ TechTrend Retail` (White font, Bold, 16pt).
5. Add **Slicers** inside the blue sidebar:
   - **Slicer 1**: Drag `customers[segment]` (Consumer, Corporate, Home Office).
   - **Slicer 2**: Drag `orders[order_status]` (Delivered, Shipped, Cancelled, Returned).
   - **Slicer 3**: Drag `orders[payment_method]` (Credit Card, UPI, Net Banking, Debit Card).
   - *Format each slicer:* In **Visual > Values**, set Font color to White and Background to transparent or dark navy `#0A3F8A` with rounded corners.

---

## 💳 Step 3: The 12 Top KPI Cards (2 Rows of 6)

In your reference image, there are 12 vibrant colored KPI cards organized in two horizontal rows.
Create each card using the **Card** (or **New Card**) visual:

### Row 1 (Gross Financials & Volume):
| # | Card Title & Field | Value | Recommended Card Fill Color | Font Color |
| :-: | :--- | :--- | :--- | :--- |
| **1** | `Total Revenue` | **$212.2K** | Navy / Indigo `#242D75` | White |
| **2** | `Total Profit` | **$88.4K** | Royal Blue `#3F51B5` | White |
| **3** | `Total Orders` | **1,200** | Teal / Cyan `#009688` | White |
| **4** | `Units Sold` | **2,190** | Emerald Green `#00C853` | White |
| **5** | `Delivered Rev` | **$111.1K** | Rose Pink / Magenta `#E91E63` | White |
| **6** | `Delivered Profit` | **$46.7K** | Purple `#7B3FF2` | White |

### Row 2 (Unit Economics & Performance Ratios):
| # | Card Title & Field | Value | Recommended Card Fill Color | Font Color |
| :-: | :--- | :--- | :--- | :--- |
| **7** | `Profit Margin %` | **41.65%** | Navy / Indigo `#242D75` | White |
| **8** | `Realized Margin %` | **42.05%** | Royal Blue `#3F51B5` | White |
| **9** | `Average Order Value` | **$176.80** | Teal / Cyan `#009688` | White |
| **10** | `Fulfillment Success %` | **56.33%** | Emerald Green `#00C853` | White |
| **11** | `Fulfillment Loss` | **$70.7K** | Rose Pink / Magenta `#E91E63` | White |
| **12** | `Cancellation Rate %` | **15.58%** | Purple `#7B3FF2` | White |

*Tip for colored cards:* Select the Card > Go to **Format visual** > **General** > **Effects** > Set **Background** color to the hex code above, and set **Rounded corners** to `10px`. In **Callout value**, set font color to `White`.

---

## 📊 Step 4: The 7 Core Analytical Visuals

Below the 12 KPI cards, arrange the 7 charts on white containers:

### 1. Sales by Customer Segment (Middle-Left Donut Chart)
- **Visual**: **Donut chart**
- **Legend**: `customers[segment]` (Consumer, Corporate, Home Office)
- **Values**: `[Total Revenue]`
- *Matches:* "Impressions by Gender" from your reference.

### 2. Revenue by Product Category (Middle-Center Bar Chart)
- **Visual**: **Clustered column chart**
- **X-axis**: `products[category]` (Electronics, Office, Accessories, Wearables)
- **Y-axis**: `[Total Revenue]`
- *Format:* Soft purple/lavender bars `#B39DDB`.
- *Matches:* "Impressions by Age" from your reference.

### 3. Monthly Revenue by Category (Middle-Right Stacked Column)
- **Visual**: **Stacked column chart**
- **X-axis**: `orders[order_date]` (Month)
- **Y-axis**: `[Total Revenue]`
- **Legend**: `products[category]`
- *Matches:* "Weekly Impressions Trend" from your reference.

### 4. Monthly Profit Growth Trajectory (Line Chart)
- **Visual**: **Line chart**
- **X-axis**: `orders[order_date]` (Month)
- **Y-axis**: `[Total Profit]`
- *Format:* Dark violet line `#6A1B9A` with light pink area fill underneath.
- *Matches:* "Daily Impressions Trend" from your reference.

### 5. Revenue by Region / State (Bottom-Left Map or Bar)
- **Visual**: **Filled map** or **Horizontal Clustered Bar chart**
- **Location / Y-axis**: `customers[state]`
- **Bubble size / X-axis**: `[Total Revenue]`
- *Matches:* "Impressions by Country" from your reference.

### 6. Order Status Monthly Distribution (Bottom-Center Matrix)
- **Visual**: **Matrix**
- **Rows**: `orders[order_status]`
- **Columns**: `orders[order_date]` (Month)
- **Values**: `[Total Orders]`
- *Matches:* "Analysis by Month" from your reference.

### 7. Product Performance Matrix with Data Bars (Bottom-Right Table)
- **Visual**: **Matrix** or **Table**
- **Columns**: `products[product_name]`, `[Total Units Sold]`, `[Total Revenue]`, `[Total Profit]`, `[Profit Margin %]`
- *Format:* Under **Cell elements**, turn on **Data bars** or **Background color** gradient (blue to purple).
- *Matches:* "Analysis by Ad Type" colored table from your reference.
