import constants as c
import numpy as np
import matplotlib.pyplot as plt

fitnessMatrix = np.load("fitnessMatrix.npy")
# print(fitnessMatrix)

averageMatrix = np.mean(fitnessMatrix, axis=0)
print(averageMatrix)

plt.plot(averageMatrix, linewidth=3)
# plt.plot(fitnessMatrix.T, linestyle='dashed')
plt.xticks([0,1,2,3])
plt.xlabel("Generation")
plt.ylabel("Fitness Value")

plt.show()
