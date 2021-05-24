from maya import cmds
import pymel.core as pm

driven = 'joint1' 
driver = cmds.ls(sl=1)[0]
shape=pm.selected()[0].split('.')[0]


def getRange(currentSelection):
    list = currentSelection.split('[')[-1].split(']')[0].split(':')
    return range(int(list[0]), int(list[1])+1)

def getPositions(rootPosition):   
    xPos=[]; yPos=[]; zPos=[]
    for x in set(cmds.listAttr(rootPosition)) - set(cmds.listAttr(rootPosition, s=1)):
        fullAttr = cmds.getAttr(shape + '.' + x)[0]
        xPos.append(fullAttr[0]); yPos.append(fullAttr[1]); zPos.append(fullAttr[2])
    return (sum(xPos)/len(xPos), sum(yPos)/len(yPos), sum(zPos)/len(zPos))

driven = 'joint1' 
driver = cmds.ls(sl=1)[0]

def match(driven, driver):
    driverPos = getPositions(driver)
    
    print driverPos
    cmds.setAttr(driven+'.translateX',driverPos[0])
    cmds.setAttr(driven+'.translateY',driverPos[1])
    cmds.setAttr(driven+'.translateZ',driverPos[2])
    
match(driven, driver)
