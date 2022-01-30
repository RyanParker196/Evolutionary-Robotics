import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")
world = p.loadSDF("world.sdf")

for x in range(1000):
    print("step {}".format(x))
    time.sleep(1/60)
    p.stepSimulation()

p.disconnect()
