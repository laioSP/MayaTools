import maya.cmds as cmds

sqList=[]
def squareFun():
    defaultSquare=cmds.nurbsSquare(nr=(0, 1, 0))
    defaultSquareList=cmds.ls(defaultSquare,dag=1)
    square=cmds.group(em=True,n='square')
    for x in range (len(defaultSquareList)):
        if 'Shape' in defaultSquareList[x]:
            cmds.parent(defaultSquareList[x],square,r=True,s=True)
    cmds.delete(defaultSquare)
    cmds.makeIdentity(square,apply=True, t=1,r=1,s=1,n=0,pn=1)
    cmds.select(clear=True)
    sqList.append(square)

def sides():
    global defaultSquare
    defaultSquare=cmds.nurbsSquare(nr=(0, 1, 0))
    global defaultSquareList
    defaultSquareList=cmds.ls(defaultSquare,dag=1)
    cmds.setAttr(defaultSquareList[1]+".rotateZ",90)
    cmds.setAttr(defaultSquareList[5]+".rotateZ",90)
    cmds.setAttr(defaultSquareList[3]+".rotateX",90)
    cmds.setAttr(defaultSquareList[7]+".rotateX",90)
    cmds.setAttr(defaultSquareList[0]+".translateY",0.5)
    cmds.setAttr(defaultSquareList[0]+".rotateY",45)
    cmds.setAttr(defaultSquareList[0]+".scale",1.413,1,1.413)    
    square=cmds.group(em=True,n='square')
    
    for x in range (len(defaultSquareList)):
        cmds.makeIdentity(defaultSquareList[x],apply=True, t=1,r=1,s=1,n=1,pn=1)    
        
        if 'Shape' in defaultSquareList[x]:
            cmds.parent(defaultSquareList[x],square,r=True,s=True)
    cmds.makeIdentity(square,apply=True, t=1,r=1,s=1,n=0,pn=1)
    cmds.select(clear=True)
    sqList.append(square)
    cmds.delete(defaultSquareList[0])
    
def Cube():
    cube=cmds.group(em=True,n='cube')
    shapesList=cmds.ls(sqList,dag=1)
    for x in range (len(shapesList)):
        if 'Shape' in shapesList[x]:
            cmds.parent(shapesList[x],cube,r=True,s=True)
            
      
        cmds.makeIdentity(cube,apply=True, t=1,r=1,s=1,n=0,pn=1)
        cmds.select(clear=True)

squareFun()
squareFun()
cmds.setAttr(sqList[1]+".translateY",1)
freeze=cmds.ls(sqList,dag=1)
cmds.makeIdentity(freeze,apply=True, t=1,r=1,s=1,n=0,pn=1)
sides()
Cube()
cmds.delete(sqList)
del sqList [:]
