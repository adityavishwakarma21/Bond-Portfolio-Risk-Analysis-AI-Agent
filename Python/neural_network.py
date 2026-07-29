import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"

df = pd.read_csv(DATA_DIR/"bond_portfolio_data.csv")

X = df[[
    "CouponRate",
    "YearsToMaturity",
    "ModifiedDuration",
    "Convexity"
]]

y = df["YieldToMaturity"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = MLPRegressor(
    hidden_layer_sizes=(64,32),
    max_iter=1000,
    random_state=42
)

model.fit(X_train,y_train)

prediction = model.predict(X_test)

mse = mean_squared_error(y_test,prediction)

print("="*60)
print("NEURAL NETWORK MODEL")
print("="*60)
print("Mean Squared Error :",mse)

result = pd.DataFrame({
    "Actual":y_test,
    "Predicted":prediction
})

result.to_csv(
    BASE_DIR/"report"/"neural_network_predictions.csv",
    index=False
)

print("\nPrediction file saved.")

