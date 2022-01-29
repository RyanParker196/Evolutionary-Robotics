from email import header
import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")


# pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
# pyrosim.Send_Cube(name="Box2", pos=[x+1,y,z+1] , size=[length, width, height])

def buildStack(i :int, xPos :int, yPos :int):
    [length, width, height] = [1, 1, 1]
    z = .5
    for i in range(10):
        pyrosim.Send_Cube(name="Box_{}".format(i), pos=[xPos,yPos,z] , size=[length, width, height])
        [length, width, height] = [length*.9, width*.9, height*.9]
        z = z + height + .5

for row in range(4):
    for col in range(4):
        buildStack(10, row, col)

pyrosim.End()