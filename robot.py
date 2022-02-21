import pybullet as p

class ROBOT:
    def __init__(self):
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("body.urdf")

    def Prepare_To_Sense():
        pass
