import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"

df = pd.read_csv(DATA_DIR / "bond_portfolio_data.csv")

features = [
    "CouponRate",
    "YearsToMaturity",
    "ModifiedDuration",
    "Convexity"
]

target = "YieldToMaturity"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("="*60)
print("RANDOM FOREST MODEL")
print("="*60)

print("R² Score :", round(r2_score(y_test,prediction),4))
print("MAE :", round(mean_absolute_error(y_test,prediction),4))
import matplotlib.pyplot as plt

importance = model.feature_importances_

plt.figure(figsize=(8,5))

plt.bar(features,importance)

plt.title("Feature Importance")

plt.tight_layout()

plt.savefig(BASE_DIR/"Images"/"feature_importance.png")

plt.show()