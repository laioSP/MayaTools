from maya import cmds
cages=cmds.ls(sl=1)
vertices=cmds.ls(sl=1)

def getName():
    name=vertices[0].split('vtx')[0].split('.')[0]
    return name
    
def verticesRange():
    verticesRangeList = []
    for x in vertices:
        b=x.split('vtx')[-1]
        c=b.split(']')[0].split('[')[-1].split(':')
        last=c[-1]
        first=c[0]

        if first != last:
            verticesRangeList.append( range( int(first), int(last)+1))
        else:
             verticesRangeList.append([int(first)])
                
    return verticesRangeList     

def verify(frame, point, objName):

    getBox = cmds.exactWorldBoundingBox( frame)
    xMax,yMax, zMax, xMin, yMin, zMin = getBox
    getPosition = cmds.xform( objName+'.vtx['+str(point)+']', q=True, ws=True, t=True)
    xPos, yPos, zPos = getPosition
    if xMin >= xPos:
        if xMax <= xPos:
            if yMin >= yPos:
                if yMax <= yPos:
                    if zMin >= zPos:
                        if zMax <= zPos:
                            return True
def collectVertices(frame):
    insideBB = []
    verticesRangeList = verticesRange()
    name = name=vertices[0].split('vtx')[0].split('.')[0]
    for localRange in verticesRangeList:
        for y in localRange:

            if verify(x, y, name):
                insideBB.append(name+'.vtx['+str(y)+']')
    setName=name.split('_')[1]+'Set_'
    print setName
    counter =  (len(cmds.ls(setName+'*')) / 2)+1
    print counter
    cmds.sets(insideBB, n=setName + str(counter))

for x in cages:
    collectVertices(x)
