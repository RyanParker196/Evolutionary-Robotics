import os
from parallelhillclimber import PARALLEL_HILL_CLIMBER

os.system('del fitness*.txt')
os.system('del tmp*.txt')
os.system('del brain*.txt')

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.ShowBest()

os.system('del fitness*.txt')
os.system('del tmp*.txt')
os.system('del brain*.txt')