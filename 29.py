import pandas as pd   
import seaborn as sns  
import matplotlib.pyplot as  plt 
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True)
df= data.frame


print(df.info())
print(df.describe())


sns.pairplot(df,vars=["MedInc", "AveRooms","HouseAge","MedHouseVal"])
plt.show()

print("Missing values : \n", df.isnull().sum())
