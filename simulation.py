import pybullet as p
import time
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet_data
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        pyrosim.Prepare_To_Simulate(1)

        self.world = WORLD()
        self.robot = ROBOT()

    
    def Run(numSteps: int):
        for i in range(numSteps):
            time.sleep(1/60)
            p.stepSimulation()

    def __del__(self):
        p.disconnect()
