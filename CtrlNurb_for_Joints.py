from __future__ import division
import maya.cmds as cmds

joints=cmds.ls(sl=True,dag=1,type='joint')
clusterList=[]
locList=[]
   
def createCurve(precision):
    positionsList=[]
    for x in range(0,len(joints),precision):
        jointPosition=cmds.xform(joints[x],q=1,ws=1,rp=1)
        positionsList.append(jointPosition)    
    curvy=cmds.curve(p=positionsList,d=3)
    return curvy
        
def nurbCluster():
    cvList = cmds.ls(curvy + ".cv[0:]",fl=True)
    clusterGroup=cmds.group(n='clusterCurve_GRP',em=True)
    for x in cvList:
        cl=cmds.cluster(x)
        clusterList.append(cl)
        cmds.parent(cl,clusterGroup)

def attach(amount,curvy):
    locatorsGroup=cmds.group(n='locatorsCurve_GRP',em=True)
    for x in range(amount):
        locName="strap"+str(x)+"_LOC"
        loc=cmds.spaceLocator(n=locName)
        motionPath=cmds.pathAnimation(loc, fm=True,c=curvy)
        cmds.disconnectAttr(motionPath+"_uValue.output", motionPath+".uValue")
        cmds.setAttr(motionPath+".uValue", (1/amount)*(x+1))
        locList.append(loc)
        cmds.parent(loc,locatorsGroup)

def clustersCtrl():
    ctrlGrpMaster=cmds.group(n='clusters_CTRL_GRP',em=True)
    counter=1
    for x in clusterList:
        ctrl=cmds.circle(n='cluster_CTRL_'+str(counter))
        ctrlGrp=cmds.group(ctrl,n='cluster_CTRL_ZERO_'+str(counter))
        cmds.parent(ctrlGrp,ctrlGrpMaster)
        cmds.matchTransform(ctrlGrp,x[1])
        cmds.parentConstraint(ctrl[0],x[1])
        counter+=1
         
def nurbJoints(precision):
    c=createCurve(precision)
    attach(len(joints),c)
    for x in range(len(joints)):
        cmds.parentConstraint(locList[x],joints[x])
    nurbCluster()
    clustersCtrl()
        
nurbJoints(2)
#nurbJoints(precision)
