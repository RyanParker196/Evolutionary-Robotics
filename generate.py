import pyrosim.pyrosim as pyrosim
import random

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    pyrosim.Send_Cube(name="Box", pos=[5,5,.5] , size=[1,1,1])

    pyrosim.End()

def Create_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg")

    for i in range(3):
        for j in range(3,5):
            rand_weight = random.random()

            # TODO: Add negative values
            print(rand_weight)
            pyrosim.Send_Synapse(sourceNeuronName=i,targetNeuronName=j,weight=1.0)
            

    pyrosim.End()

def Create_Body():
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

Create_World()
Create_Brain()
Create_Body()
