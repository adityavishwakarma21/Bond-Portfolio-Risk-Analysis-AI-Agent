import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read Bond Portfolio Data
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"

df = pd.read_csv(DATA_DIR / "bond_portfolio_data.csv")

print("=" * 50)
print("BOND PORTFOLIO DATA")
print("=" * 50)

# First 5 rows
print("\nFirst 5 Rows:\n")
print(df.head())

# Shape
print("\nShape:")
print(df.shape)

# Column Names
print("\nColumns:")
print(df.columns.tolist())

# Data Types
print("\nData Types:")
print(df.dtypes)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic Statistics
print("\nStatistics:")
print(df.describe())
print("\n")
print("=" * 50)
print("TOP 10 ISSUERS")
print("=" * 50)

print(df["Issuer"].value_counts().head(10))


print("\n")
print("=" * 50)
print("AVERAGE VALUES")
print("=" * 50)

print("Average Yield :", round(df["YieldToMaturity"].mean(),4))
print("Average Duration :", round(df["ModifiedDuration"].mean(),4))
print("Average Convexity :", round(df["Convexity"].mean(),4))
plt.figure(figsize=(10,6))

top_issuers = df["Issuer"].value_counts().head(10)

top_issuers.plot(kind="bar")

plt.title("Top 10 Bond Issuers")
plt.xlabel("Issuer")
plt.ylabel("Number of Bonds")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../Images/top_issuers.png")

plt.show()
# ==========================
# Top 10 Issuers Chart
# ==========================

plt.figure(figsize=(12,6))

top_issuers = df["Issuer"].value_counts().head(10)

top_issuers.plot(kind="bar", color="steelblue")

plt.title("Top 10 Bond Issuers")
plt.xlabel("Issuer")
plt.ylabel("Number of Bonds")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(BASE_DIR / "Images" / "top_issuers.png")

plt.show()
# ==========================
# Yield Distribution
# ==========================

plt.figure(figsize=(10,6))

plt.hist(df["YieldToMaturity"], bins=20, edgecolor="black")

plt.title("Yield To Maturity Distribution")
plt.xlabel("Yield")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(BASE_DIR / "Images" / "yield_distribution.png")

plt.show()
# ==========================
# Duration Distribution
# ==========================

plt.figure(figsize=(10,6))

plt.hist(df["ModifiedDuration"], bins=20, edgecolor="black")

plt.title("Modified Duration Distribution")
plt.xlabel("Duration")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(BASE_DIR / "Images" / "duration_distribution.png")

plt.show()
# ==========================
# Convexity Distribution
# ==========================

plt.figure(figsize=(10,6))

plt.hist(df["Convexity"], bins=20, edgecolor="black")

plt.title("Convexity Distribution")
plt.xlabel("Convexity")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(BASE_DIR / "Images" / "convexity_distribution.png")

plt.show()