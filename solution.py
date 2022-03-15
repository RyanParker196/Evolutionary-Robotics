import os
import random
import numpy as np
import pyrosim.pyrosim as pyrosim
import random

class SOLUTION:

    def __init__(self):
        self.weights = np.random.rand(3,2)
        self.weights = self.weights * 2 - 1

    def Mutate(self):
        rand_select = random.randint(0,2)


    def Evaluate(self):
        self.Create_World()
        self.Create_Brain()
        self.Create_Body()
        os.system("python3 simulate.py")

        # close loop
        f = open("fitness.txt","r")
        self.fitness = float(f.read())
        f.close()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.Send_Cube(name="Box", pos=[5,5,.5] , size=[1,1,1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in range(2):
                rand_weight = random.random() * 2 - 1
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,targetNeuronName=currentColumn+3,weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[1.5,.5,1.5] , size=[1,1,1])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child ="BackLeg",
            type="revolute",position=[1,.5,1])

        pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[1,1,1])

        # This is still abs value
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child ="FrontLeg",
            type="revolute",position=[2,.5,1])

        pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5] , size=[1,1,1])

        pyrosim.End()