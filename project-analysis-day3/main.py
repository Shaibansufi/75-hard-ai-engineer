from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = FastAPI()

# -------------------------------
# TRAIN MODEL (same as before)
# -------------------------------
df = pd.read_csv("house_data.csv")

X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------------
# HOME PAGE (FORM)
# -------------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h2>House Price Prediction</h2>
            <form action="/predict" method="get">
                Area: <input type="number" name="area"><br><br>
                Bedrooms: <input type="number" name="bedrooms"><br><br>
                Bathrooms: <input type="number" name="bathrooms"><br><br>
                <input type="submit" value="Predict">
            </form>
        </body>
    </html>
    """

# -------------------------------
# PREDICTION ENDPOINT
# -------------------------------
@app.get("/predict", response_class=HTMLResponse)
def predict(area: float, bedrooms: int, bathrooms: int):
    prediction = model.predict([[area, bedrooms, bathrooms]])

    return f"""
    <html>
        <body>
            <h2>Predicted Price: {prediction[0]:.2f}</h2>
            <a href="/">Go Back</a>
        </body>
    </html>
    """