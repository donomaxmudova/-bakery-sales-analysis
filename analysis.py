from pathlib import Path
import pandas as pd

file_path = Path(__file__).parent / "sales.csv"
sales = pd.read_csv(file_path)

sales["revenue_uzs"] = (
    sales["quantity"] * sales["unit_price_uzs"]
)

print("Total revenue (UZS):")
print(sales["revenue_uzs"].sum())

print("\nUnits sold by product:")
print(
    sales.groupby("product")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nDaily revenue (UZS):")
print(sales.groupby("date")["revenue_uzs"].sum())
