import maya.cmds as cmds

CS=cmds.ls(sl=True,dag=1)
IKList=[]
FKList=[]
SKList=[]
slider=[]

for x in CS:
        
    if "IK" in x:
        if "FK" not in x:
            IKList.append(x)
    if "FK" in x:
        if "IK" not in x:
            FKList.append(x)
    if "IK" not in x:
        if "FK" not in x:
            if "effector" not in x:
                SKList.append(x)
    if "IK_FK_Ctrl" in x:
        slider.append(x)


tuppleBones=zip(IKList,FKList,SKList)
rangeNode=cmds.createNode('setRange')
cmds.setAttr(rangeNode+".maxX",1)
cmds.setAttr(rangeNode+".oldMaxX",2)
cmds.connectAttr(slider[0]+".translateZ",rangeNode+".valueX")

def IK_FK_switch(ik,fk,sb):
    cmds.createNode('')
    blendColor=cmds.createNode("blendColors")
    cmds.connectAttr(rangeNode+".outValueX",blendColor+".blender")
    cmds.connectAttr(ik+".rotate", blendColor+".color2")
    cmds.connectAttr(fk+".rotate", blendColor+".color1")
    cmds.connectAttr(blendColor+".output", sb+".rotate")
    
for x in range(len(IKList)):
    print x
    ik=IKList[x]
    fk=FKList[x]
    sb=SKList[x]
    print (ik,fk,sb)
    IK_FK_switch(ik,fk,sb)
