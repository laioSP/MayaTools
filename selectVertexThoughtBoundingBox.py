from maya import cmds
collidingCages = []
objList = []

def screening():
    allObjs=cmds.ls(type='mesh')
    for obj in allObjs:
        for frame in cages:
            if obj not in cages:
                check = verify(frame, obj)           
                if check:
                    collidingCages.append(check[1])
                    objList.append(check[0])
    
def getVertices():
    vertices=[]
    for x in objList:
        getVtx = cmds.ls(x+".vtx[*]")[0]
        getRange = getVtx.split('[')[-1].split(']')[0].split(':')
        for v in range(int(getRange[0]),int(getRange[1])):
            vertices.append(x+".vtx["+str(v)+"]")
    return vertices

def getLocation(input):
    if 'Shape' in input:
        inputTransform = input.split('Shape')[0] + input.split('Shape')[1]
        input = inputTransform
        xMax,yMax, zMax, xMin, yMin, zMin = cmds.exactWorldBoundingBox( input ) 
        return (input, xMax, yMax, zMax, xMin, yMin, zMin) 
        
    if cmds.objectType(input) == 'transform':        
        if cmds.objectType(cmds.ls(input,dag=1)[1]) == 'mesh':
            xMax,yMax, zMax, xMin, yMin, zMin = cmds.exactWorldBoundingBox( input )
            return (input, xMax, yMax, zMax, xMin, yMin, zMin) 
    if ".vtx[" in input:
        temp = cmds.xform( input, q=True, ws=True, t=True)
        xMax, yMax, zMax = temp
        xMin, yMin, zMin = temp
        return (input, xMax, yMax, zMax, xMin, yMin, zMin)       

def verify(frame, point):
    result = []

    pointObj, xMax,yMax, zMax, xMin, yMin, zMin = getLocation(frame)
    frameObj, xPosMax, yPosMax, zPosMax, xPosMin, yPosMin, zPosMin = getLocation(point)  

    if xMin >= xPosMin:
        result.append(frameObj)
        result.append(pointObj)
        result.append(xMin)
        if xMax <= xPosMax:
            result[2]=xMin, xMax
            if yMin >= yPosMin:
                result[2]=xMin, xMax, yMin
                if yMax <= yPosMax:
                    result[2]=xMin, xMax, yMin, yMax
                    if zMin >= zPosMin:
                        result[2]=xMin, xMax, yMin, yMax, zMin
                        if zMax <= zPosMax:
                            result[2]=xMin, xMax, yMin, yMax, zMin, zMax
                            return result
                        else:
                            return result
                    else:
                        return result
                else:
                    return result
            else:
                return result

def collectVertices():
    screening()
    vertices = getVertices()
    for frame in collidingCages:
        for vertice in vertices:
            Filter = verify(frame, vertice)
            if Filter:     
                if len(Filter[2]) == 6 :
                    print Filter
                    setName = Filter[1]+'_set_'
                    counter = (len(cmds.ls(setName+'*')) / 2)+1

                    if counter < 10:
                        counter = '0' + str(counter)
                    else:
                        counter = str(counter)
                    print counter       
                    if cmds.ls(setName + counter):
                        cmds.sets(vertice, add=setName + counter)
                    else:    
                        cmds.sets(vertice, n=setName + counter)

cages=cmds.ls(sl=1, dag=1, type='mesh')        
collectVertices()  
