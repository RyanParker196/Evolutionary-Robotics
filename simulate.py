import constants as c
import sys
from simulation import SIMULATION

directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.Run(c.numSteps)
del simulation
