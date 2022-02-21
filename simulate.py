import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
SIMULATION.Run(simulation, c.numSteps)
del simulation
