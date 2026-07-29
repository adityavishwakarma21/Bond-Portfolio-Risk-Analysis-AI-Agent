import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"

df = pd.read_csv(DATA_DIR / "monte_carlo_scenarios.csv")

print("="*60)
print("MONTE CARLO SCENARIO ANALYSIS")
print("="*60)

print("\nDataset Shape :", df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nAverage Profit/Loss :", round(df["PnL_Total_INR"].mean(),2))
print("Maximum Profit :", round(df["PnL_Total_INR"].max(),2))
print("Maximum Loss :", round(df["PnL_Total_INR"].min(),2))
# Top Profit Scenarios

top_profit = df.sort_values(
    by="PnL_Total_INR",
    ascending=False
).head(10)

print("\nTop Profit Scenarios")
print(top_profit[["ScenarioID","PnL_Total_INR"]])
# Worst Loss Scenarios

worst_loss = df.sort_values(
    by="PnL_Total_INR"
).head(10)

print("\nWorst Loss Scenarios")
print(worst_loss[["ScenarioID","PnL_Total_INR"]])
plt.figure(figsize=(10,6))

plt.hist(
    df["PnL_Total_INR"],
    bins=30,
    edgecolor="black"
)

plt.title("Monte Carlo Profit/Loss Distribution")

plt.xlabel("PnL")

plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(BASE_DIR/"Images"/"monte_carlo_distribution.png")

plt.show()
top_profit.to_csv(
    BASE_DIR/"report"/"top_profit_scenarios.csv",
    index=False
)

worst_loss.to_csv(
    BASE_DIR/"report"/"worst_loss_scenarios.csv",
    index=False
)

print("\nMonte Carlo Report Saved")
