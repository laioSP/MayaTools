import maya.cmds as cmds

currentSelection=cmds.ls(sl=True)
clusterList=[]
counter=0
cmds.group(n=currentSelection[0] +"_grp")

degrees=cmds.getAttr(currentSelection[0] + ".degree")
spans=cmds.getAttr(currentSelection[0] + ".spans")
clusterAmount=degrees + spans

def sphere():
    
    global circle1
    circle1=cmds.ls(cmds.circle(nr=(1,0,0)),dag=1)
    circle2=cmds.ls(cmds.circle(nr=(0,1,0)),dag=1)
    circle3=cmds.ls(cmds.circle(nr=(0,0,1)),dag=1)
    cmds.parent(circle3[1],circle2[1],circle1[0],r=True,s=True)
    cmds.delete(circle3[0],circle2[0])
    cmds.makeIdentity(circle1,apply=True, t=1,r=1,s=1,n=0,pn=1)
    cmds.select(clear=True)
    

for y in range(clusterAmount):
    print y
    currentCluster=cmds.cluster(currentSelection[0] +".cv["+str(counter)+"]")
    clusterList.append(currentCluster)
    cmds.parent(currentCluster,currentSelection[0] +"_grp")
    counter+=1
    
    if len(clusterList) == clusterAmount:  
        for x in clusterList:
            print x
            sphere()
        
            cmds.matchTransform(circle1, x)
            cmds.makeIdentity(circle1,apply=True, t=1,r=1,s=1,n=0,pn=1)
            cmds.parentConstraint(circle1, x)
            cmds.setAttr(x[0]+".relative", 1)
            cmds.setAttr(x[1]+".visibility", 0)    
            cmds.parent(circle1,currentSelection[0] +"_grp")
