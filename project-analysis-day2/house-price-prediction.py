import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


# Read CSV file
df = pd.read_csv('house_data.csv')
print(df.head())
# Getting length
print(df.info())
# But Shape is Easier to Implement 
print(df.shape)
stopper = 10000
# Adding Check Condition

if df.shape[0] < 10000:
    def generate_price(a,b,c):
        return new_area * 3 + new_bedrooms *2 + new_bathrooms *1
    
    # Lets Add new Data
    new_area = np.random.uniform(1000,5000,10990).astype('i')
    new_bedrooms = np.random.uniform(1,5,10990).astype('i')
    new_bathrooms = np.random.uniform(1,5,10990).astype('i')
    noise = np.random.uniform(-1000, 1000, len(new_area))
    new_price = (new_area * 3) + (new_bedrooms * 2) + (new_bathrooms * 1) + noise

    data = {
            'area': new_area,
            'bedrooms':new_bedrooms,
            'bathrooms':new_bathrooms,
            'price':new_price
        }

    new_df = pd.DataFrame(data)
    print(new_df.head())
    new_df.to_csv('house_data.csv',mode='a',index=False,header=False)
    print(df.tail())

    # Finally after Spending 1 hour I was able to add data without using loops 
    # Learning from yesterday's mistake !
    # Adding Check Condition to Avoid Unnecessary muliple addition of the data 

# Now we can start with ml 

X = df.drop('price',axis='columns')
y = df['price']
# Let's Check the shape of X
# print(X.shape)
# print(X.head())
# Let's Check the shape of y
# print(y.shape)
# print(y.head())

# Now Let's do Train Test Split 
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25)

# Let's Explore the data 
# print(len(X_train))
# print(len(X_test))

# # Now Let's Train the Model
model = LinearRegression()
model.fit(X_train,y_train)

# model score ?
print(model.score(X_test,y_test))
# 0.9895436491853772
# This means the model is Accurate

# # Let's Try Predict
print(model.predict([[2766,2,4]]))
[8984615.38461538]

