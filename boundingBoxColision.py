import maya.cmds as cmds

A="Name of Object A"
B="Name of Object B"

counterRef=len(cmds.ls('*bMinZ_BoundingBox*'))
counter=counterRef + 1
 
def boundingBoxConditions():

    listName="listN"+str(counter)
    cmds.createNode('condition',n="aMinX_less_bMaxX_BoundingBox"+str(counter))
    cmds.setAttr("aMinX_less_bMaxX_BoundingBox"+str(counter)+".operation", 4)
    cmds.createNode('condition',n="aMaxX_greater_bMinX_BoundingBox"+str(counter))
    cmds.setAttr("aMaxX_greater_bMinX_BoundingBox"+str(counter)+".operation", 2)
    cmds.createNode('condition',n="aMinY_less_bMaxY_BoundingBox"+str(counter))
    cmds.setAttr("aMinY_less_bMaxY_BoundingBox"+str(counter)+".operation", 4)
    cmds.createNode('condition',n="aMaxY_greater_bMinY_BoundingBox"+str(counter))
    cmds.setAttr("aMaxY_greater_bMinY_BoundingBox"+str(counter)+".operation", 2)
    cmds.createNode('condition',n="aMinZ_less_bMaxZ_BoundingBox"+str(counter))
    cmds.setAttr("aMinZ_less_bMaxZ_BoundingBox"+str(counter)+".operation", 4)
    cmds.createNode('condition',n="aMaxZ_greater_bMinZ_BoundingBox"+str(counter))
    cmds.setAttr("aMaxZ_greater_bMinZ_BoundingBox"+str(counter)+".operation", 2)
    
    cmds.connectAttr("aMinX_less_bMaxX_BoundingBox"+str(counter)+".outColor","aMaxX_greater_bMinX_BoundingBox"+str(counter)+".colorIfTrue")
    cmds.connectAttr("aMaxX_greater_bMinX_BoundingBox"+str(counter)+".outColor","aMinY_less_bMaxY_BoundingBox"+str(counter)+".colorIfTrue")
    cmds.connectAttr("aMinY_less_bMaxY_BoundingBox"+str(counter)+".outColor","aMaxY_greater_bMinY_BoundingBox"+str(counter)+".colorIfTrue")    
    cmds.connectAttr("aMaxY_greater_bMinY_BoundingBox"+str(counter)+".outColor","aMinZ_less_bMaxZ_BoundingBox"+str(counter)+".colorIfTrue")
    cmds.connectAttr( "aMinZ_less_bMaxZ_BoundingBox"+str(counter)+".outColor","aMaxZ_greater_bMinZ_BoundingBox"+str(counter)+".colorIfTrue")
    
    cmds.connectAttr("aMinX_less_bMaxX_BoundingBox"+str(counter)+".colorIfFalse","aMaxX_greater_bMinX_BoundingBox"+str(counter)+".colorIfFalse")
    cmds.connectAttr("aMaxX_greater_bMinX_BoundingBox"+str(counter)+".colorIfFalse","aMinY_less_bMaxY_BoundingBox"+str(counter)+".colorIfFalse")
    cmds.connectAttr("aMinY_less_bMaxY_BoundingBox"+str(counter)+".colorIfFalse","aMaxY_greater_bMinY_BoundingBox"+str(counter)+".colorIfFalse")    
    cmds.connectAttr("aMaxY_greater_bMinY_BoundingBox"+str(counter)+".colorIfFalse","aMinZ_less_bMaxZ_BoundingBox"+str(counter)+".colorIfFalse")
    cmds.connectAttr( "aMinZ_less_bMaxZ_BoundingBox"+str(counter)+".colorIfFalse","aMaxZ_greater_bMinZ_BoundingBox"+str(counter)+".colorIfFalse")
    
    cmds.connectAttr( A+".boundingBox.boundingBoxMin.boundingBoxMinX","aMinX_less_bMaxX_BoundingBox"+str(counter)+".firstTerm")
    cmds.connectAttr( A+".boundingBox.boundingBoxMax.boundingBoxMaxX","aMaxX_greater_bMinX_BoundingBox"+str(counter)+".firstTerm")
    cmds.connectAttr( A+".boundingBox.boundingBoxMin.boundingBoxMinY","aMinY_less_bMaxY_BoundingBox"+str(counter)+".firstTerm")
    cmds.connectAttr( A+".boundingBox.boundingBoxMax.boundingBoxMaxY","aMaxY_greater_bMinY_BoundingBox"+str(counter)+".firstTerm")
    cmds.connectAttr( A+".boundingBox.boundingBoxMin.boundingBoxMinZ","aMinZ_less_bMaxZ_BoundingBox"+str(counter)+".firstTerm")
    cmds.connectAttr( A+".boundingBox.boundingBoxMax.boundingBoxMaxZ","aMaxZ_greater_bMinZ_BoundingBox"+str(counter)+".firstTerm")
    
    cmds.connectAttr( B+".boundingBox.boundingBoxMin.boundingBoxMinX","aMinX_less_bMaxX_BoundingBox"+str(counter)+".secondTerm")
    cmds.connectAttr( B+".boundingBox.boundingBoxMax.boundingBoxMaxX","aMaxX_greater_bMinX_BoundingBox"+str(counter)+".secondTerm")
    cmds.connectAttr( B+".boundingBox.boundingBoxMin.boundingBoxMinY","aMinY_less_bMaxY_BoundingBox"+str(counter)+".secondTerm")
    cmds.connectAttr( B+".boundingBox.boundingBoxMax.boundingBoxMaxY","aMaxY_greater_bMinY_BoundingBox"+str(counter)+".secondTerm")
    cmds.connectAttr( B+".boundingBox.boundingBoxMin.boundingBoxMinZ","aMinZ_less_bMaxZ_BoundingBox"+str(counter)+".secondTerm")
    cmds.connectAttr( B+".boundingBox.boundingBoxMax.boundingBoxMaxZ","aMaxZ_greater_bMinZ_BoundingBox"+str(counter)+".secondTerm")

boundingBoxConditions()
