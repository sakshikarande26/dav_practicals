#IMPLEMENT SIMPLE LINEAR REGRESSION IN PYTHON

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#sample data
x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,3,4,5,6])

#fit linear model
model = LinearRegression().fit(x, y)

#print coefficients
print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])

#plot the data and regression line
plt.scatter(x, y)
plt.plot(x, model.predict(x), color="red")
plt.title('Simple Linear regression')
plt.xlabel("x")
plt.ylabel("y")

plt.show()





