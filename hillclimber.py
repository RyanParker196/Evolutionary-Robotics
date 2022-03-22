from solution import SOLUTION
from copy import deepcopy 
import constants as c

class HILL_CLIMBER:

    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate('GUI')
        for currentGeneration in range(c.numGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate('DIRECT')
        self.Select()

    def Spawn(self):
        self.child = deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if (self.child.fitness > self.parent.fitness):
            self.parent = self.child

    def ShowBest(self):
        self.parent.Evaluate('GUI')
        print("Best fitness score = "+self.parent.fitness)