import os
from parallelhillclimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.ShowBest()

os.remove('fitness*.txt')
os.remove('tmp*.txt')
os.remove('brain*.txt')
