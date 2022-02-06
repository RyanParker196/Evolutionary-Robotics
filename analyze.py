import numpy as np
import matplotlib.pyplot as plt

torsoData = np.load("data/torsoSensorValues.npy")
backLegData = np.load("data/backLegSensorValues.npy")
plt.plot(torsoData, label="FrontLeg Sensor Data", linewidth=5)
plt.plot(backLegData, label="BackLeg Sensor Data", linewidth=2)
plt.legend()
plt.show()
