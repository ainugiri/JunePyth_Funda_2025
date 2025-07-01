# CREATE PROGRAM / APPLICATION, 
# LEARN FROM DATA

"""
1. Data-> collect data from various sources
2. Preprocess -> clean and prepare the data for analysis 
3, Select Model ->
4. Train the model -> make model learn from the data
5. Test the model -> evaluate the model's performance (Test data -> actual vs predicted)
6. Deploy the model -> make the model available for use
7. Monitor and maintain the model -> ensure the model continues to perform well over time
"""

# age: 1 - 100000, 99500, 100500,99200,100250
# age: 2 - 95000, 94000,96000,95500,95000
# age: 3 - 90000, 91000,89500,90500,90000
# age: 4 - 80000, 81000,79500,80500,80000
# age: 5 - 75000, 74000,76000,75500,75000

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

carage = np.array([1,1,1,1,1,
                   2,2,2,2,2,
                   3,3,3,3,3,
                   4,4,4,4,4,
                   5,5,5,5,5])          # Feature: Age of the car
carprice = np.array([104000, 99500, 100500, 99200, 100250,
                     95000, 94000, 96000, 95500, 95000,
                     90000, 91000, 89500, 90500, 90000,
                     80000, 81000, 79500, 80500, 80000,
                     75000, 74000, 76000, 75500, 75000])  # Target: Price of the car

model = LinearRegression()  # Create a linear regression model
carage = carage.reshape(-1, 1)  # Reshape the feature array for the model
carprice = carprice.reshape(-1, 1)  # Reshape the target array for the model
model.fit(carage, carprice)  # Train the model with the data

age2 = int(input("Enter the age of the car"))  # Get user input for car age
predicted_price = model.predict(np.array([[age2]]))  # Predict the price based on the input age
print(f"The predicted price of the car is: {predicted_price[0][0]}")  # Print the predicted price

plt.scatter(carage, carprice, color='blue')  # Plot the original data points
plt.plot(carage, model.predict(carage), color='red')  # Plot the regression
plt.title('Car Age vs Price')  # Set the title of the plot
plt.xlabel('Age of the Car (Years)')  # Set the x-axis label
plt.ylabel('Price of the Car')  # Set the y-axis label
plt.show()  # Display the plot  

