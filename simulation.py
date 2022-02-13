import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
worldId = p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

numSteps = 1000
torsoValues = np.zeros(numSteps)
backLegValues = np.zeros(numSteps)

for i in range(numSteps):
    time.sleep(1/60)
    p.stepSimulation()
    torsoValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Torso")
    backLegValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

np.save("data/torsoSensorValues.npy", torsoValues)
np.save("data/backLegSensorValues.npy", backLegValues)
p.disconnect()
