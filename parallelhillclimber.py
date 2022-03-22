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
        print(self.parents)
        # self.parent = SOLUTION()

    def Evolve(self):
        for key in self.parents:
            print(self.parents[key])
            self.parents[key].Evaluate('GUI')
            
        # self.parent.Evaluate('GUI')
        # for currentGeneration in range(c.numGenerations):
        #     self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate('DIRECT')
        print(self.parent.fitness, self.child.fitness)
        self.Select()

    def Spawn(self):
        # add id + 1
        self.child = deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if (self.child.fitness > self.parent.fitness):
            self.parent = self.child

    def ShowBest(self):
        pass
        # self.parent.Evaluate('GUI')
        # print("Best fitness score = "+str(self.parent.fitness))