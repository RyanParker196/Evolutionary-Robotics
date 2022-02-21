import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import time
import random
from simulation import SIMULATION

simulation = SIMULATION()
SIMULATION.Run(1000)
del simulation

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,-9.8)

# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# worldId = p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)

# numSteps = 1000
# torsoValues = np.zeros(numSteps)
# backLegValues = np.zeros(numSteps)

# motorCommandVect = np.linspace(0, 2*np.pi, numSteps)
# # np.save("data/targetAngles.npy", targetAngles)

# for i in range(numSteps):
#     time.sleep(1/60)
#     p.stepSimulation()
#     torsoValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Torso")
#     backLegValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

#     targetAngle = c.amplitude * np.sin(c.frequency * motorCommandVect[i] + c.phaseOffset)
#     pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="BackLeg_Torso",
#         controlMode=p.POSITION_CONTROL, targetPosition=targetAngle, maxForce=500)

#     targetAngle2 = c.amplitude2 * np.sin(c.frequency2 * motorCommandVect[i] + c.phaseOffset2)
#     pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_FrontLeg",
#         controlMode=p.POSITION_CONTROL, targetPosition=-targetAngle2, maxForce=500)


# np.save("data/torsoSensorValues.npy", torsoValues)
# np.save("data/backLegSensorValues.npy", backLegValues)
# p.disconnect()
