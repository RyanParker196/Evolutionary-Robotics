from solution import SOLUTION
from copy import deepcopy 
import constants as c

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self):
        for key in self.parents:
            self.parent = self.parents[key]
            self.parent.Start_Simulation('DIRECT')
            self.Evolve_For_One_Generation()
        # self.parent.Evaluate('GUI')
        # for currentGeneration in range(c.numGenerations):
        #     self.Evolve_For_One_Generation()

        for key in self.parents:
            self.parent = self.parents[key]
            self.parent.Wait_For_Simulation_To_End()
            print(self.parent.fitness)

    def Evolve_For_One_Generation(self):
        pass
        # self.Spawn()
        # self.Mutate()
        # self.child.Start_Simulation('DIRECT')
        # self.Select()

    def Spawn(self):
        self.child = deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if (self.child.fitness > self.parent.fitness):
            self.parent = self.child

    def ShowBest(self):
        pass
        # self.parent.Evaluate('GUI')
        # print("Best fitness score = "+self.parent.fitness)