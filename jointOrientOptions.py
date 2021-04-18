import maya.cmds as cmds
currentSelection=cmds.ls(sl=True,type='joint')
for x in range(len(currentSelection)):
    cmds.parent(currentSelection[x+1],currentSelection[x])
    if x + 2 == len(currentSelection):
        break
cmds.select(currentSelection[0])
cmds.joint(e=True,oj='xyz',sao='xup',ch=True,zso=True)

oritentX=cmds.getAttr(str(currentSelection[-2])+".jointOrientX")
oritentY=cmds.getAttr(str(currentSelection[-2])+".jointOrientY")
oritentZ=cmds.getAttr(str(currentSelection[-2])+".jointOrientZ")

cmds.setAttr(str(currentSelection[-1])+".jointOrientX",oritentX)
cmds.setAttr(str(currentSelection[-1])+".jointOrientY",oritentY)
cmds.setAttr(str(currentSelection[-1])+".jointOrientZ",oritentZ)

for x in currentSelection:
    if x != currentSelection[0]:
        cmds.parent(x,w=True)
