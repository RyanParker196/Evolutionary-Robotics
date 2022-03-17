import os
from hillclimber import HILL_CLIMBER

hc = HILL_CLIMBER()
hc.Evolve()
x = input("ready?")
if x == 'y':
    hc.ShowBest()
