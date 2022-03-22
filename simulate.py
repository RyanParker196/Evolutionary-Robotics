import constants as c
import sys
from simulation import SIMULATION

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run(c.numSteps)
del simulation
