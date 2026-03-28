import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

FILE_PATH = "house_data.csv"

# -------------------------------
# STEP 1: Load Data
# -------------------------------
df = pd.read_csv(FILE_PATH)
print("Initial Data Shape:", df.shape)

# -------------------------------
# STEP 2: Add Data (ONLY IF NEEDED)
# -------------------------------
if df.shape[0] < 10000:
    print("Generating new synthetic data...")

    n_samples = 10000 - df.shape[0]

    new_area = np.random.uniform(1000, 5000, n_samples).astype(int)
    new_bedrooms = np.random.randint(1, 6, n_samples)
    new_bathrooms = np.random.randint(1, 6, n_samples)

    noise = np.random.uniform(-1000, 1000, n_samples)

    new_price = (
        new_area * 3000 + 
        new_bedrooms * 50000 + 
        new_bathrooms * 30000 + 
        noise
    )

    new_df = pd.DataFrame({
        'area': new_area,
        'bedrooms': new_bedrooms,
        'bathrooms': new_bathrooms,
        'price': new_price
    })

    # Append to CSV
    new_df.to_csv(FILE_PATH, mode='a', index=False, header=False)

    print("New data added!")

    # 🔥 IMPORTANT: Reload updated dataset
    df = pd.read_csv(FILE_PATH)

print("Final Data Shape:", df.shape)

# -------------------------------
# STEP 3: Prepare Data
# -------------------------------
X = df.drop('price', axis=1)
y = df['price']

# -------------------------------
# STEP 4: Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# -------------------------------
# STEP 5: Train Model
# -------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------------
# STEP 6: Evaluate Model
# -------------------------------
score = model.score(X_test, y_test)
print(f"Model Accuracy (R^2 Score): {score:.4f}")

# -------------------------------
# STEP 7: Prediction
# -------------------------------
sample = [[2766, 2, 4]]
prediction = model.predict(sample)
print(model.score(X_test,y_test))
print(f"Predicted Price for {sample}: {prediction[0]:.2f}")