from maya import cmds
import pymel.core as pm

shape=pm.selected()[0].split('.')[0]

def getRange(currentSelection):
    list = currentSelection.split('[')[-1].split(']')[0].split(':')
    return range(int(list[0]), int(list[1])+1)

def getPositions(rootPosition):   
    xPos=[]; yPos=[]; zPos=[]
    for x in set(cmds.listAttr(rootPosition)) - set(cmds.listAttr(rootPosition, s=1)):
        fullAttr = cmds.xform(shape + '.' + x, q=True, ws=True, t=True)        
        xPos.append(fullAttr[0]); yPos.append(fullAttr[1]); zPos.append(fullAttr[2])
    return (sum(xPos)/len(xPos), sum(yPos)/len(yPos), sum(zPos)/len(zPos))


def match(driver):
    cmds.select(cl=1)
    if cmds.objectType(driver) == 'mesh':
        cmds.joint( n=shape.split('Shape')[0]+'_JNT', p=getPositions(driver) )
    else:
        J=cmds.joint( n=driver+'_JNT')
        cmds.matchTransform(J, driver)
   
match(cmds.ls(sl=1)[0])
