import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"

df = pd.read_csv(DATA_DIR / "bond_portfolio_data.csv")

print("="*50)
print("BOND ANALYSIS")
print("="*50)

print("\nPortfolio Summary")

print("Total Bonds :", len(df))
print("Average Yield :", round(df["YieldToMaturity"].mean(),4))
print("Average Duration :", round(df["ModifiedDuration"].mean(),4))
print("Average Convexity :", round(df["Convexity"].mean(),4))
print("Average Clean Price :", round(df["CleanPrice"].mean(),2))
print("Average Dirty Price :", round(df["DirtyPrice"].mean(),2))
print("\nTop 10 Highest Yield Bonds")

highest_yield = df.sort_values(
    by="YieldToMaturity",
    ascending=False
)[
    ["BondID","Issuer","YieldToMaturity"]
].head(10)

print(highest_yield)
print("\nTop 10 Longest Duration Bonds")

long_duration = df.sort_values(
    by="ModifiedDuration",
    ascending=False
)[
    ["BondID","Issuer","ModifiedDuration"]
].head(10)

print(long_duration)
print("\nTop 10 Highest Convexity Bonds")

high_convexity = df.sort_values(
    by="Convexity",
    ascending=False
)[
    ["BondID","Issuer","Convexity"]
].head(10)

print(high_convexity)
highest_yield.to_csv(
    BASE_DIR / "report" / "highest_yield_bonds.csv",
    index=False
)

long_duration.to_csv(
    BASE_DIR / "report" / "longest_duration_bonds.csv",
    index=False
)

high_convexity.to_csv(
    BASE_DIR / "report" / "highest_convexity_bonds.csv",
    index=False
)

print("\nReports Saved Successfully")


