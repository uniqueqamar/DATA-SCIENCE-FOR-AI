import numpy as np
dataset = np.random.randint(1,51, size=(5,5))
print("original: \n", dataset)

dataset[dataset>25]=0
print(dataset)


print("sum: ", np.sum(dataset))
print("mean: ",np.mean(dataset))
print("max: ", np.max(dataset))
print("min:", np.min(dataset))

