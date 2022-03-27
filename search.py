import os
from parallelhillclimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.ShowBest()

os.system('rm fitness*.txt')
os.system('rm tmp*.txt')
os.system('rm brain*.txt')
