import numpy as np
from solution import SOLUTION
from copy import deepcopy
import constants as c

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        # Init parent solutions
        self.nextAvailableID = 0
        self.fitnessMatrix = np.zeros(shape=(c.populationSize,c.numGenerations))
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self):
        self.Evaluate(self.parents)

        for currentGeneration in range(c.numGenerations):
            print("Evolve for generation {}".format(currentGeneration))
            self.Evolve_For_One_Generation(currentGeneration)

    def Evolve_For_One_Generation(self, currentGeneration):
        # self.FindBest()
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        self.StoreResults(currentGeneration)

    def FindBest(self):
        maxFit = -10
        for key in self.parents:
            fit = self.parents[key].fitness
            if (fit > maxFit):
                maxFit = fit
                maxKey = key
        self.best = self.parents[maxKey]

    def StoreResults(self, currentGeneration):
        # For each population p
        p = 0 # ranges from 0 to population size
        for key in self.parents:
            self.fitnessMatrix[p][currentGeneration] = self.parents[key].fitness
            p = p + 1

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

            # if child > parent
            if (c > p):
                # Child becomes new parent
                self.parents[key] = self.children[key]

    def Evaluate(self, solutions):
        for key in solutions:
            solutions[key].Start_Simulation('DIRECT')

        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()

    def ShowBest(self):
        maxFit = -10
        for key in self.parents:
            fit = self.parents[key].fitness
            if (fit > maxFit):
                maxFit = fit
                maxKey = key
        print("Best fitness of parent {} = {}".format(maxKey,self.parents[maxKey].fitness))
        self.parents[maxKey].Start_Simulation('GUI')
        np.save('fitnessMatrix.npy', self.fitnessMatrix)
