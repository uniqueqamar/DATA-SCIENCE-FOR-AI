import numpy as np
outcomes = np.array([1,2,3,4,5,6])

probabilities = np.array([1/6]*6)

expectation = np.sum(outcomes*probabilities)
print("Expectation (Mean):",expectation)

variance = np.sum((outcomes-expectation)**2*probabilities)
std_dev = np.sqrt(variance)
print(variance)
print(std_dev)