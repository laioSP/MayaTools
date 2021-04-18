from maya import cmds

def allAxes():
    allJoints = cmds.ls(type='joint')
    check = cmds.getAttr(allJoints[0] + ".displayLocalAxis")
    switch =  abs(check - 1)        
    for x in allJoints:        
        cmds.setAttr(x + ".displayLocalAxis", switch)
        
def orientUnparented():
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

cmds.OrientJointOptions()
mod = cmds.frameLayout(l='extra tools', cll = True, bgc = (0.3,0.4,0.6))
cmds.button( l = 'Toggle All Axes Visibility', c='allAxes()', p=mod, bgc = (0.3,0.3,0.4) )
cmds.button( l = 'Orient Unparented According to selection ',c = 'orientUnparented()',  p=mod, bgc = (0.3,0.3,0.4) )
