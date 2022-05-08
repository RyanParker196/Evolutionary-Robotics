import constants as c
import numpy as np
import matplotlib.pyplot as plt

fitnessMatrixA = np.load("fitnessScores/fitnessMatrix-A.npy")
fitnessMatrixB = np.load("fitnessScores/fitnessMatrix-B.npy")

averageMatrixA = np.mean(fitnessMatrixA , axis=0)
averageMatrixB = np.mean(fitnessMatrixB , axis=0)

plt.plot(averageMatrixA, linewidth=3, label='A')
plt.plot(averageMatrixB, linestyle='dashed', label='B')
plt.xticks(list(range(0,c.numGenerations)))
plt.xlabel("Generation")
plt.ylabel("Fitness Value")
plt.legend()
plt.savefig('fig.png')
