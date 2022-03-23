import os
from solution import SOLUTION
from copy import deepcopy
import constants as c

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        # Clear files
        os.system('del brain*.nndf')
        os.system('del fitness*.txt')
        os.system('del tmp*.txt')
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self):
        self.Evaluate(self.parents)

        for currentGeneration in range(c.numGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        # self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        if (self.child.fitness > self.parent.fitness):
            self.parent = self.child

    def Evaluate(self, solutions):
        for key in solutions:
            solutions[key].Start_Simulation('DIRECT')

        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()
            print(solutions[key].fitness)


    def ShowBest(self):
        pass
        # self.parent.Evaluate('GUI')
        # print("Best fitness score = "+str(self.parent.fitness))
