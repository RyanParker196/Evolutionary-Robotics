import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR


class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for motor in self.motors.values():
            motor.Set_Value(self.robotId, t)

    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)
