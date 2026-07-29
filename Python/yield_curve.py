import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"

df = pd.read_csv(DATA_DIR / "yield_curve_history.csv")

print("="*60)
print("YIELD CURVE ANALYSIS")
print("="*60)

print("\nDataset Shape :", df.shape)

print("\nAverage Yield :", round(df["Yield"].mean(),4))
print("Maximum Yield :", round(df["Yield"].max(),4))
print("Minimum Yield :", round(df["Yield"].min(),4))
# Average Yield by Tenor

avg_yield = df.groupby("Tenor_Years")["Yield"].mean()

print("\nAverage Yield by Tenor")
print(avg_yield)
plt.figure(figsize=(12,6))

avg_yield.plot(
    marker="o",
    linewidth=2
)

plt.title("Average Yield Curve")
plt.xlabel("Tenor (Years)")
plt.ylabel("Yield")

plt.grid(True)

plt.tight_layout()

plt.savefig(BASE_DIR/"Images"/"yield_curve.png")

plt.show()
avg_yield.to_csv(
    BASE_DIR/"report"/"average_yield_curve.csv"
)

print("\nYield Curve Report Saved")