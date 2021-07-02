from maya import cmds

def createSphere(name):
    circle1=cmds.ls(cmds.circle(n=name,nr=(1,0,0)),dag=1)
    circle2=cmds.ls(cmds.circle(nr=(0,1,0)),dag=1)
    circle3=cmds.ls(cmds.circle(nr=(0,0,1)),dag=1)
    cmds.parent(circle3[1],circle2[1],circle1[0],r=True,s=True)
    cmds.delete(circle3[0],circle2[0])
    cmds.makeIdentity(circle1,apply=True, t=1,r=1,s=1,n=0,pn=1)
    cmds.select(clear=True)
    return circle1

def createPin(name):
    pinHead=createSphere('pinHead')
    pointer=cmds.ls(cmds.curve(n=name , d=3, p=[(0,0,1), (0, 0, 1.333333),(0, 0, 2), (0, 0, 3), (0, 0, 4,), (0, 0, 4.666667), ( 0, 0, 5)], k=[0, 0, 0, 1, 2, 3, 4, 4, 4]),dag=1) 
    cmds.parent(cmds.ls('pinHead',dag=True)[1:],pointer[1], pointer[0],r=True,s=True)
    cmds.delete(cmds.ls('pinHead',dag=True)[0])
    return pointer

def rotateShape(ctrl, X, Y, Z):
    vertexList = []
    for x in cmds.ls(ctrl,dag=1)[1:]:
        vertexList.append(x + '.cv[*]')       
    cmds.rotate(X, Y, Z,vertexList)      
    return ctrl

def shapeSize(ctrl, value):
    vertexList = []
    for x in cmds.ls(ctrl,dag=1)[1:]:
        vertexList.append(x + '.cv[*]')       
    cmds.scale(value,value,value,vertexList)      
    return ctrl

def createSquare(name):
    defaultSquare=cmds.nurbsSquare(nr=(0, 1, 0))
    defaultSquareList=cmds.ls(defaultSquare,dag=1)
    square=cmds.group(em=True,n=name)
    for x in range (len(defaultSquareList)):
        if 'Shape' in defaultSquareList[x]:
            cmds.parent(defaultSquareList[x],square,r=True,s=True)
    cmds.delete(defaultSquare)
    cmds.makeIdentity(square,apply=True, t=1,r=1,s=1,n=0,pn=1)
    cmds.select(clear=True)
    return square

def createGroup(name,function,parented):
    grp = cmds.group(parented,n=name+'_'+function)
    return grp

def createCTRL(name, junction):
    radius = cmds.getAttr(junction+'.radius')
    main = cmds.circle(n=name+'_CTRL', r=radius)
    cmds.addAttr(k=True, ln='subCtrl', at='bool')
    sub = cmds.circle(n=name[0]+'Sub_CTRL', r=radius*0.7)
    cmds.parent(sub, main)
    cmds.connectAttr(main[0]+'.subCtrl',sub[0]+'.visibility')
    zero = createGroup(name,'ZERO',main)
    link = createGroup(name,'LINK',zero)
    cmds.matchTransform(zero, junction)
    return (main, zero, link)

def changeShape(old,newShape):
    cmds.delete(cmds.ls(old,dag=1)[1:])
    cmds.parent(cmds.ls(newShape,dag=1)[1:], old, s=1,r=1)
    cmds.delete(newShape)
    return old
