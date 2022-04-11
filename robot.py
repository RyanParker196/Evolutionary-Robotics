from ntpath import join
import shutil
import constants as c
import os
from time import sleep
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self, simulationID):
        self.robotId = p.loadURDF("body.urdf")
        self.simulationID = simulationID
        
        # Read and delete brain
        self.nn = NEURAL_NETWORK("brain{}.nndf".format(simulationID))
        os.remove('brain{}.nndf'.format(self.simulationID))

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    # TODO
    def Think(self):
        self.nn.Update()
 
    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange

                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

    def Get_Fitness(self):
        
        # Calculate fitness
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        fitnessScore = positionOfLinkZero[0]
        
        # Write fitness score to txt file
        f = open("tmp{}.txt".format(self.simulationID),"w")
        f.write(str(fitnessScore))
        f.close()
        
        # Rename after finished writing to tmp
        shutil.move(f"tmp{self.simulationID}.txt", f"fitness{self.simulationID}.txt")
