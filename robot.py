from ntpath import join
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
        os.system('del brain{}.nndf'.format(self.simulationID))

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Think(self):
        self.nn.Update()
 
    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)

                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        fitnessScore = -positionOfLinkZero[0]
        
        # Write fitness score to txt file
        sleep(1/6)
        f = open("tmp{}.txt".format(self.simulationID),"w")
        f.write(str(fitnessScore))
        f.close()
        
        # Rename tmp -> fitness
        # TODO: Windows bug, this is a workaround
        # DEL fitness#.txt before rename tmp file
        # os.system('del fitness{}.txt'.format(self.simulationID))
        # os.rename("tmp"+str(self.simulationID)+".txt" , "fitness"+str(self.simulationID)+".txt")
        # os.system('rename tmp{}.txt fitness{}.txt'.format(self.simulationID,self.simulationID))

