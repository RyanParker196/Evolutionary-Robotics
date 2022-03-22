import os
from solution import SOLUTION
from copy import deepcopy 
import constants as c

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del tmp*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self):
        self.Evaluate(self.parents)
        #from evaluate
        self.Evolve_For_One_Generation()

    def Evaluate(self, solutions):
        for key in solutions:
            self.parent = solutions[key]
            self.parent.Start_Simulation('GUI')
        # self.parent.Evaluate('GUI')
        # for currentGeneration in range(c.numGenerations):
        #     self.Evolve_For_One_Generation()

        for key in solutions:
            self.parent = solutions[key]
            self.parent.Wait_For_Simulation_To_End()
            print(self.parent.fitness)

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        exit()
        # self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        print(self.children)
        
    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        if (self.child.fitness > self.parent.fitness):
            self.parent = self.child

    def ShowBest(self):
        pass
        # self.parent.Evaluate('GUI')
        # print("Best fitness score = "+self.parent.fitness)