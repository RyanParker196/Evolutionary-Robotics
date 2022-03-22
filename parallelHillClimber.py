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
        self.Print()
        self.ShowBest()

    def Evaluate(self, solutions):
        for key in solutions:
            self.parent = solutions[key]
            self.parent.Start_Simulation('DIRECT')
        # self.parent.Evaluate('GUI')
        # for currentGeneration in range(c.numGenerations):
        #     self.Evolve_For_One_Generation()

        for key in solutions:
            self.parent = solutions[key]
            self.parent.Wait_For_Simulation_To_End()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()

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
            childFitness = self.children[key]
            parentFitness = self.parents[key]

            if (childFitness.fitness  > parentFitness.fitness):
                self.parents[key] = self.children[key]

    def ShowBest(self):
        self.lowestFitness = self.parents[0]
        print(self.lowestFitness.fitness)
        print("starting sim")
        self.lowestFitness.Start_Simulation('GUI')
        # self.parent.Evaluate('GUI')
        # print("Best fitness score = "+self.parent.fitness)

    def Print(self):
        print()
        for key in self.parents:
            print('Parent {} fitness = {}'.format(key, self.parents[key].fitness))
            print('Child {} fitness = {}'.format(key, self.parents[key].fitness))
        print()