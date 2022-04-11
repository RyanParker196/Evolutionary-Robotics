import os
import random
import time
from turtle import pos
import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import constants as c

class SOLUTION:

    def Set_ID(self, id):
        self.myID = id

    def __init__(self, id):
        self.myID = id
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Start_Simulation(self, directOrGui):
        # Generate robot
        self.Create_World()
        self.Create_Brain()
        self.Create_Body()

        # Run simulation
        os.system("start /B python3 simulate.py " +
                  directOrGui + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        # Wait for fitness to exist
        fitnessFileName = "fitness{}.txt".format(self.myID)
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        # Read fitness from file
        f = open("fitness{}.txt".format(self.myID), "r")
        self.fitness = float(f.read())
        f.close()

        # Delete fitness
        os.remove('fitness{}.txt'.format(self.myID))

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.Send_Cube(name="Box", pos=[-3,0,2.5] , size=[1,1,1])
        pyrosim.Send_Cube(name="Stand", pos=[-3,0,1] , size=[2,2,2])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))

        # Build nodes
        # 7 sensors
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Arm")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="UpperArm")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LegBackRight")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="LegBackLeft")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="LegFrontRight")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="LegFrontLeft")

        # 6 motors
        pyrosim.Send_Motor_Neuron(name=7, jointName= "Torso_Arm")
        pyrosim.Send_Motor_Neuron(name=8, jointName= "Arm_UpperArm")
        pyrosim.Send_Motor_Neuron(name=9, jointName= "Torso_LegBackRight")
        pyrosim.Send_Motor_Neuron(name=10, jointName= "Torso_LegBackLeft")
        pyrosim.Send_Motor_Neuron(name=11, jointName= "Torso_LegFrontRight")
        pyrosim.Send_Motor_Neuron(name=12, jointName= "Torso_LegFrontLeft")

        # Build edges
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                rand_weight = random.random() * 2 - 1
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,targetNeuronName=currentColumn+c.numSensorNeurons,weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[2, 1, 1])

        pyrosim.Send_Joint(name="Torso_Arm", parent="Torso", child="Arm",
                           type="revolute", position=[-1, 0, 2], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="Arm", pos=[0, 0, .5], size=[c.xLeg, c.yLeg, 1])

        pyrosim.Send_Joint(name="Arm_UpperArm", parent="Arm", child="UpperArm",
                           type="revolute", position=[0, 0, 1], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="UpperArm", pos=[-.5, 0, 0], size=[1, c.yLeg, c.xLeg])

        pyrosim.Send_Joint(name="Torso_LegBackRight", parent="Torso", child="LegBackRight",
                           type="revolute", position=[1, .5, 1], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="LegBackRight", pos=[0, 0, -.5], size=[c.xLeg, c.yLeg, 1])

        pyrosim.Send_Joint(name="Torso_LegBackLeft", parent="Torso", child="LegBackLeft",
                           type="revolute", position=[1, -.5, 1], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="LegBackLeft", pos=[0, 0, -.5], size=[c.xLeg, c.yLeg, 1])

        pyrosim.Send_Joint(name="Torso_LegFrontRight", parent="Torso", child="LegFrontRight",
                           type="revolute", position=[-1, .5, 1], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="LegFrontRight", pos=[0, 0, -.5], size=[c.xLeg, c.yLeg, 1])

        pyrosim.Send_Joint(name="Torso_LegFrontLeft", parent="Torso", child="LegFrontLeg",
                           type="revolute", position=[-1, -.5, 1], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="LegFrontLeg", pos=[0, 0, -.5], size=[c.xLeg, c.yLeg, 1])

        pyrosim.End()
