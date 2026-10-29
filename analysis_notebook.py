# Superstore Sales & Profitability Analysis
# Source dataset: Kaggle Sample Superstore
# Download the CSV from: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
# Place it beside this notebook as "Sample - Superstore.csv".

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path("Sample - Superstore.csv")
if not DATA_PATH.exists():
    raise FileNotFoundError("Download Sample - Superstore.csv from Kaggle and place it beside this notebook.")

df = pd.read_csv(DATA_PATH, encoding="latin-1")
df.columns = df.columns.str.strip()
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")
for col in ["Sales", "Profit", "Discount", "Quantity"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 1. Data quality checks
print("Rows and columns:", df.shape)
print("Duplicate rows:", df.duplicated().sum())
print("Missing values by column:")
print(df.isna().sum().sort_values(ascending=False).head(10))

# 2. Clean analysis fields (retain original columns)
df = df.drop_duplicates().copy()
df = df.dropna(subset=["Order Date", "Sales", "Profit"])
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.to_period("M").dt.to_timestamp()
df["Profit Margin"] = np.where(df["Sales"] != 0, df["Profit"] / df["Sales"], np.nan)

# 3. Executive KPIs
kpis = pd.Series({
    "Total Sales": df["Sales"].sum(),
    "Total Profit": df["Profit"].sum(),
    "Profit Margin": df["Profit"].sum() / df["Sales"].sum(),
    "Orders": df["Order ID"].nunique(),
    "Customers": df["Customer ID"].nunique(),
    "Units Sold": df["Quantity"].sum(),
    "Average Discount": df["Discount"].mean()
})
display(kpis.to_frame("Value").style.format("{:,.2f}"))

# 4. Category and region profitability
category = df.groupby("Category").agg(
    Sales=("Sales", "sum"), Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique"), Units=("Quantity", "sum")
)
category["Profit Margin"] = category["Profit"] / category["Sales"]
display(category.sort_values("Sales", ascending=False).style.format({
    "Sales":"${:,.0f}", "Profit":"${:,.0f}", "Profit Margin":"{:.1%}"
}))

region = df.groupby("Region").agg(Sales=("Sales","sum"), Profit=("Profit","sum"))
region["Profit Margin"] = region["Profit"] / region["Sales"]
display(region.sort_values("Profit", ascending=False).style.format({
    "Sales":"${:,.0f}", "Profit":"${:,.0f}", "Profit Margin":"{:.1%}"
}))

# 5. Subcategory analysis: identify revenue and profit gaps
subcat = df.groupby(["Category","Sub-Category"]).agg(
    Sales=("Sales","sum"), Profit=("Profit","sum"), Discount=("Discount","mean")
).sort_values("Profit")
display(subcat.style.format({"Sales":"${:,.0f}","Profit":"${:,.0f}","Discount":"{:.1%}"}))

# 6. Discount analysis
df["Discount Band"] = pd.cut(
    df["Discount"], bins=[-0.001, 0, .10, .20, .30, .50, 1.0],
    labels=["0%", ">0–10%", ">10–20%", ">20–30%", ">30–50%", ">50%"],
    include_lowest=True
)
discount = df.groupby("Discount Band", observed=False).agg(
    Sales=("Sales","sum"), Profit=("Profit","sum"), Rows=("Profit","size")
)
discount["Profit Margin"] = discount["Profit"] / discount["Sales"]
display(discount.style.format({"Sales":"${:,.0f}","Profit":"${:,.0f}","Profit Margin":"{:.1%}"}))

# 7. Monthly trend
monthly = df.groupby("Month").agg(Sales=("Sales","sum"), Profit=("Profit","sum"))
fig, ax = plt.subplots(figsize=(12,5))
monthly["Sales"].plot(ax=ax, label="Sales", linewidth=2)
monthly["Profit"].plot(ax=ax, label="Profit", linewidth=2)
ax.set_title("Monthly Sales and Profit Trend")
ax.set_ylabel("USD")
ax.grid(alpha=.25); ax.legend(); plt.tight_layout(); plt.show()

# 8. Charts
fig, axes = plt.subplots(1, 2, figsize=(13,5))
category["Sales"].sort_values().plot(kind="barh", ax=axes[0], title="Sales by Category")
category["Profit"].sort_values().plot(kind="barh", ax=axes[1], title="Profit by Category")
for ax in axes:
    ax.grid(axis="x", alpha=.2); ax.set_axisbelow(True)
plt.tight_layout(); plt.show()

subcat.sort_values("Profit")["Profit"].plot(kind="barh", figsize=(10,7), title="Profit by Subcategory")
plt.axvline(0, color="black", linewidth=.8); plt.grid(axis="x", alpha=.2); plt.tight_layout(); plt.show()

# 9. Export clean analysis tables
out = Path("outputs"); out.mkdir(exist_ok=True)
kpis.to_csv(out/"executive_kpis.csv", header=["Value"])
category.to_csv(out/"category_performance.csv")
region.to_csv(out/"region_performance.csv")
subcat.to_csv(out/"subcategory_performance.csv")
discount.to_csv(out/"discount_analysis.csv")
monthly.to_csv(out/"monthly_trend.csv")
print(f"Exported analysis tables to {out.resolve()}")

# 10. Interpret findings using your computed results before publishing:
# - Prioritize subcategories with negative profit for pricing, cost, and discount review.
# - Compare profit margin as well as sales; high revenue does not guarantee strong profitability.
# - Evaluate discount bands with adequate transaction counts before changing policy.
# - Segment regional actions based on both absolute profit and margin.
