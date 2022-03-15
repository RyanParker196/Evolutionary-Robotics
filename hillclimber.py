from solution import SOLUTION
from copy import deepcopy 
import constants as c

class HILL_CLIMBER:

    def __init__(self):
        self.parent = SOLUTION()
        self.child = deepcopy(self.parent)

    def Evolve(self):
        self.parent.Evaluate()
        for currentGeneration in range(c.numGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate
        self.Select()

    def Spawn(self):
        pass

    def Mutate(self):
        self.child.Mutate()

    def Evaluate(self):
        pass

    def Select(self):
        pass

