import numpy as np
import pandas as pd   
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score
import matplotlib.pyplot as plt 


np.random.seed(42)
X= np.random.rand(100,1)*100
Y = 3* np.random.randn(100,1)*2

X_train, X_test, Y_train,Y_test= train_test_split(X,Y,test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)


print("COefficients: ",model.coef_[0][0])
print("INtercept: ",model.intercept_[0])

plt.scatter(X_test,Y_test,color = "green", label = "Actual")
plt.plot(X_test, Y_pred, color="Red",label= "predict")
plt.title("Linear Regression Model ")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()