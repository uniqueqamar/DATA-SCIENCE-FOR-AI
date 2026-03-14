from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[800],[1000],[1200]])
y = np.array([20,25,30])

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[1100]])
print(prediction)

plt.scatter(X,y,color="blue", label="Data Points")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.title("Linear Regression Example")
plt.xlabel("Square Footage")
plt.ylabel("Price (in $1000s)")
plt.legend()
plt.show()
 