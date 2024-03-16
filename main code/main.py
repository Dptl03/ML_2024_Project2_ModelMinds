import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Defining function to calculate Root Mean Squared Error
def calculate_rmse(predictions, targets):

    predictions = np.array(predictions)
    targets = np.array(targets)
    
    squared_errors = (predictions - targets) ** 2    
    mean_squared_error = np.mean(squared_errors)    
    rmse = np.sqrt(mean_squared_error)
    
    return rmse

# Load data from CSV file
data = pd.read_csv('object_info_all2.csv')

# Assuming the last column is the target variable and others are features
X = data.iloc[:, :-3]  # Features
y = data.iloc[:, -3:]   # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

print(X_train, X_test, y_train, y_test)
# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
print(y_pred_test)

# Evaluate the model
train_rmse = calculate_rmse(y_pred_train, y_train)
test_rmse = calculate_rmse(y_pred_test, y_test)


print("Train RMSE:", train_rmse)
print("Test RMSE:", test_rmse)