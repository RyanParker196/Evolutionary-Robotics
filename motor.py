from ntpath import join
import numpy as np
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName) -> None:
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.motorValues = np.linspace(0, 2*np.pi, c.numSteps)

    def Set_Value(self, robotId, desiredAngle):
        self.targetAngle = c.amplitude * np.sin(c.frequency * desiredAngle + c.phaseOffset)
        pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=self.jointName,
            controlMode=p.POSITION_CONTROL, targetPosition=self.targetAngle, maxForce=500)

    def Save_Values(self):
        np.save("data/targetAngles.npy", self.targetAngles)