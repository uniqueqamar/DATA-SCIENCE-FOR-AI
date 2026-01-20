import matplotlib.pyplot as plt   
#data =[1,2,3,4,5,1,1,1,2,2,3,4,3,2,1,2,3,]
#plt.hist(data,bins = 5, color ="green",edgecolor= "black")
#plt.show()


x=[1,2,3,4]
y=[22,25,45,23]
plt.scatter(x,y,color="red")
plt.title("Scatter Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend("Dataset1")
plt.show()