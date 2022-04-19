import pybullet as p

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        # switched to loading world(box) in robot.py
        # self.worldId = p.loadSDF("world.sdf")

