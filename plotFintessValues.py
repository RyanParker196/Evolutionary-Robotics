import constants as c
import numpy as np
import matplotlib.pyplot as plt

fitnessMatrix = np.load("fitnessMatrix.npy")
# print(fitnessMatrix)

averageMatrix = np.mean(fitnessMatrix, axis=0)
print(averageMatrix)

plt.plot(averageMatrix, linewidth=3)
# plt.plot(fitnessMatrix.T, linestyle='dashed')
plt.xticks(list(range(0,c.numGenerations)))
plt.xlabel("Generation")
plt.ylabel("Fitness Value")

plt.show()
