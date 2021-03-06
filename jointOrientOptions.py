from maya import cmds
import pymel.core as pm

def getRange(currentSelection):
    list = currentSelection.split('[')[-1].split(']')[0].split(':')
    return range(int(list[0]), int(list[1])+1)

def getPositions(rootPosition, shape):   
    xPos=[]; yPos=[]; zPos=[]
    for x in set(cmds.listAttr(rootPosition)) - set(cmds.listAttr(rootPosition, s=1)):
        fullAttr = cmds.xform(shape + '.' + x, q=True, ws=True, t=True)        
        xPos.append(fullAttr[0]); yPos.append(fullAttr[1]); zPos.append(fullAttr[2])
    return (sum(xPos)/len(xPos), sum(yPos)/len(yPos), sum(zPos)/len(zPos))

def match(driver):
    shape=pm.selected()[0].split('.')[0]
    cmds.select(cl=1)
    
    if cmds.objectType(driver) == 'mesh':
        cmds.joint( n=shape.split('Shape')[0]+'_JNT', p=getPositions(driver, shape) )
    else:
        J=cmds.joint( n=driver+'_JNT')
        cmds.matchTransform(J, driver)

def allAxes():
    allJoints = cmds.ls(type='joint')
    check = cmds.getAttr(allJoints[0] + ".displayLocalAxis")
    switch =  abs(check - 1)        
    for x in allJoints:        
        cmds.setAttr(x + ".displayLocalAxis", switch)
        
def getOrientation(referenced, direction):
    orientAngle = cmds.getAttr(referenced+".jointOrient" + direction)
    return orientAngle
        
def orient(oriented, direction, value):
    orientJoint = cmds.setAttr(oriented + ".jointOrient" + direction, value)
    return orientJoint

def copyOrientation(referenced, oriented):    
    orient(oriented, 'X', getOrientation(referenced, 'X'))
    orient(oriented, 'Y', getOrientation(referenced, 'Y'))
    orient(oriented, 'Z', getOrientation(referenced, 'Z'))

def reOrient(target, direction):
    turns = (getOrientation(target, direction) + 90)/360
    orient(target, direction, 360*abs(int(turns) - turns))
           
def orientUnparented():
    currentSelection=cmds.ls(sl=True,type='joint')
    for x in range(len(currentSelection)):
        cmds.parent(currentSelection[x+1],currentSelection[x])
        if x + 2 == len(currentSelection):
            break
    cmds.select(currentSelection[0])
    cmds.joint(e=True,oj='xyz',sao='xup',ch=True,zso=True)
    copyOrientation(str(currentSelection[-2]), str(currentSelection[-1]))
    
    for x in currentSelection:
        if x != currentSelection[0]:
            cmds.parent(x,w=True)

cmds.OrientJointOptions()
mod = cmds.frameLayout(l='extra tools', cll = True, bgc = (0.3,0.4,0.6))
cmds.button( l = 'Create Joint ',c = 'match(cmds.ls(sl=1)[0])',  p=mod, bgc = (0.3,0.3,0.4) )
cmds.button( l = 'Orient Unparented According to selection ',c = 'orientUnparented()',  p=mod, bgc = (0.3,0.3,0.4) )
cmds.button( l = 'Copy Orientation ',c = 'copyOrientation(cmds.ls(sl=True)[0], cmds.ls(sl=True)[1])',  p=mod, bgc = (0.3,0.3,0.4) )
cmds.button( l = 'Toggle All Axes Visibility', c='allAxes()', p=mod, bgc = (0.3,0.3,0.4) )
rotationOptions = cmds.gridLayout( cwh=[210,40],numberOfColumns=3, p=mod )
cmds.button( l = '',c = 'reOrient(cmds.ls(sl=True)[0], "X")',  p=rotationOptions, bgc = (1,0,0) )
cmds.button( l = '',c = 'reOrient(cmds.ls(sl=True)[0], "Y")',  p=rotationOptions, bgc = (0,1,0) )
cmds.button( l = '',c = 'reOrient(cmds.ls(sl=True)[0], "Z")',  p=rotationOptions, bgc = (0,0,1) )
