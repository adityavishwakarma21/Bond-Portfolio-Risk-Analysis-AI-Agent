import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"

df = pd.read_csv(DATA_DIR/"bond_portfolio_data.csv")

# Features
X = df[[
    "CouponRate",
    "YearsToMaturity",
    "ModifiedDuration",
    "Convexity"
]]

# Target
y = df["YieldToMaturity"]

# Train Test Split
X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model=XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    random_state=42
)

model.fit(X_train,y_train)

prediction=model.predict(X_test)

mse=mean_squared_error(y_test,prediction)

print("="*60)
print("XGBOOST MODEL")
print("="*60)
print("Mean Squared Error :",mse)

importance=pd.DataFrame({
    "Feature":X.columns,
    "Importance":model.feature_importances_
})

importance=importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance\n")
print(importance)

importance.to_csv(
    BASE_DIR/"report"/"xgboost_feature_importance.csv",
    index=False
)