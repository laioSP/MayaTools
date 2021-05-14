from maya import cmds
cages=cmds.ls(sl=1)
objList=cmds.ls(sl=1)

def getVertices():
    vertices=[]
    for x in objList:
        getVtx = cmds.ls(x+".vtx[*]")[0]
        getRange = getVtx.split('[')[-1].split(']')[0].split(':')
        for v in range(int(getRange[0]),int(getRange[1])):
            vertices.append(x+".vtx["+str(v)+"]")
    return vertices
    
def verify(frame, point):

    getBox = cmds.exactWorldBoundingBox( frame)
    xMax,yMax, zMax, xMin, yMin, zMin = getBox
    getPosition = cmds.xform( point, q=True, ws=True, t=True)
    xPos, yPos, zPos = getPosition
    if xMin >= xPos:
        if xMax <= xPos:
            if yMin >= yPos:
                if yMax <= yPos:
                    if zMin >= zPos:
                        if zMax <= zPos:
                            return frame

def collectVertices():
    vertices = getVertices()
    for frame in cages:
        for vertice in vertices:
            Filter = verify(frame, vertice)
            if Filter:
                setName = Filter+'_set_'
                counter = (len(cmds.ls(setName+'*')) / 2)+1
                if counter < 10:
                    counter = '0' + str(counter)
                else:
                    counter = str(counter)
                print counter                   
                if cmds.ls(setName + counter):
                    cmds.sets(vertice, add=setName + str(counter))
                else:    
                    cmds.sets(vertice, n=setName + counter)

for x in objList:
    print x
    getVtx = cmds.ls(x+".vtx[*]")[0]
    getRange = getVtx.split('[')[-1].split(']')[0].split(':')
    for v in range(int(getRange[0]),int(getRange[1])):
        vertices.append(x+".vtx["+str(v)+"]")

collectVertices()from maya import cmds
cages=cmds.ls(sl=1)
objList=cmds.ls(sl=1)

def getVertices():
    vertices=[]
    for x in objList:
        getVtx = cmds.ls(x+".vtx[*]")[0]
        getRange = getVtx.split('[')[-1].split(']')[0].split(':')
        for v in range(int(getRange[0]),int(getRange[1])):
            vertices.append(x+".vtx["+str(v)+"]")
    return vertices
    
def verify(frame, point):

    getBox = cmds.exactWorldBoundingBox( frame)
    xMax,yMax, zMax, xMin, yMin, zMin = getBox
    getPosition = cmds.xform( point, q=True, ws=True, t=True)
    xPos, yPos, zPos = getPosition
    if xMin >= xPos:
        if xMax <= xPos:
            if yMin >= yPos:
                if yMax <= yPos:
                    if zMin >= zPos:
                        if zMax <= zPos:
                            return frame

def collectVertices():
    vertices = getVertices()
    for frame in cages:
        for vertice in vertices:
            Filter = verify(frame, vertice)
            if Filter:
                setName = Filter+'_set_'
                counter = (len(cmds.ls(setName+'*')) / 2)+1
                if counter < 10:
                    counter = '0' + str(counter)
                else:
                    counter = str(counter)
                print counter                   
                if cmds.ls(setName + counter):
                    cmds.sets(vertice, add=setName + str(counter))
                else:    
                    cmds.sets(vertice, n=setName + counter)

for x in objList:
    print x
    getVtx = cmds.ls(x+".vtx[*]")[0]
    getRange = getVtx.split('[')[-1].split(']')[0].split(':')
    for v in range(int(getRange[0]),int(getRange[1])):
        vertices.append(x+".vtx["+str(v)+"]")

collectVertices()
