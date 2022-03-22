import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import pybullet_data
from world import WORLD
from robot import ROBOT

class SIMULATION:

    def __init__(self, directOrGui, simulationID):
        if directOrGui == 'GUI':
            self.physicsClient = p.connect(p.GUI)
        elif directOrGui == 'DIRECT':
            self.physicsClient = p.connect(p.DIRECT)
        else:
            print("No argument for optional GUI. Default=Direct")
            self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        
        self.robot = ROBOT(simulationID)
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()
    
    def Run(self, numSteps):
        for i in range(numSteps):
            print("\nRunning simulation",i)
            time.sleep(1/6000)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            self.Get_Fitness()

    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()
