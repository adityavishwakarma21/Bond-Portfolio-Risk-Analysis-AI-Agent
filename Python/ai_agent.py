import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"

df = pd.read_csv(DATA_DIR/"bond_portfolio_data.csv")

print("="*60)
print("AI BOND RISK ADVISOR")
print("="*60)

for index,row in df.head(20).iterrows():

    advice=[]

    if row["YieldToMaturity"]>0.075:
        advice.append("High Yield")

    if row["ModifiedDuration"]>8:
        advice.append("High Interest Rate Risk")

    if row["Convexity"]>80:
        advice.append("High Convexity")

    if row["CreditRating"]!="AAA":
        advice.append("Review Credit Rating")

    if len(advice)==0:
        advice.append("Healthy Bond")

    print(row["BondID"]," ---> "," | ".join(advice))
    recommendation=[]

for index,row in df.iterrows():

    advice=[]

    if row["YieldToMaturity"]>0.075:
        advice.append("High Yield")

    if row["ModifiedDuration"]>8:
        advice.append("Interest Rate Risk")

    if row["Convexity"]>80:
        advice.append("High Convexity")

    if row["CreditRating"]!="AAA":
        advice.append("Review Credit Rating")

    if len(advice)==0:
        advice.append("Healthy Bond")

    recommendation.append(", ".join(advice))

df["AI_Recommendation"]=recommendation

df.to_csv(
    BASE_DIR/"report"/"AI_Bond_Recommendations.csv",
    index=False
)

print("\nAI Recommendation Report Saved")