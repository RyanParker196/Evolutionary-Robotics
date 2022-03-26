import os
from solution import SOLUTION
from copy import deepcopy
import constants as c

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        # Clear files
        os.system('rm brain*.nndf')
        os.system('rm fitness*.txt')
        os.system('rm tmp*.txt')

        # Init parent solutions
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self):
        self.Evaluate(self.parents)

        for currentGeneration in range(c.numGenerations):
            print("Evolve for generation {}".format(currentGeneration))
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Print(self):
        for key in self.parents:
            p = self.parents[key].fitness
            c = self.children[key].fitness
            print(p,c)

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
        for key in self.parents:
            p = self.parents[key].fitness
            c = self.children[key].fitness

            # if child < parent
            if (c < p):
                # Child becomes new parent
                self.parents[key] = self.children[key]

    def Evaluate(self, solutions):
        for key in solutions:
            solutions[key].Start_Simulation('DIRECT')

        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()

    def ShowBest(self):
        minFit = 10
        for key in self.parents:
            fit = self.parents[key].fitness
            if (fit < minFit):
                minFit = fit
                minKey = key
        print("Best fitness of parent {} = {}".format(minKey,self.parents[minKey].fitness))
        self.parents[minKey].Start_Simulation('GUI')
