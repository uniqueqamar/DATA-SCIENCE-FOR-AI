from sklearn.linear_model import LogisticRegression 
import numpy as np
import matplotlib.pyplot as plt

x = np.array([[1],[2],[3],[4],[5]])
y = np.array([1,0,1,1,0])
model = LogisticRegression()
model.fit(x,y)
prediction = model.predict([[2]])
print(prediction)
plt.scatter(x,y, color = "blue",label = "data points")
plt.plot(x, model.predict(x),color = "red", label = "LogesticRegression")
plt.title("Logistic Regression example ")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
