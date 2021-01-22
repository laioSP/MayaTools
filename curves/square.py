import maya.cmds as cmds

defaultSquare=cmds.nurbsSquare(nr=(0, 1, 0))
defaultSquareList=cmds.ls(defaultSquare,dag=1)
square=cmds.group(em=True,n='square')
for x in range (len(defaultSquareList)):
    if 'Shape' in defaultSquareList[x]:
        cmds.parent(defaultSquareList[x],square,r=True,s=True)
cmds.delete(defaultSquare)
cmds.makeIdentity(square,apply=True, t=1,r=1,s=1,n=0,pn=1)
cmds.select(clear=True)
