import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Drop unnecessary column
df = df.drop("customerID", axis=1)

# Handle missing values
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.fillna(df.mean(numeric_only=True))

# Encode target
le = LabelEncoder()
df["Churn"] = le.fit_transform(df["Churn"])   # Yes=1, No=0

# Separate X and y
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Convert categorical
X = pd.get_dummies(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

# Save
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(X.columns, open("columns.pkl", "wb"))
pickle.dump(le, open("label_encoder.pkl", "wb"))

print("✅ Model trained successfully!")