import maya.cmds as cmds
import math 
jointList=[];locators=[]
jointsAmount=16
def counter(): return len(cmds.ls("bonesGrp*")); 

def getLocation():
    locations=[]
    temp=[]
    deliver=[]
    for x in locators:
        cl=cmds.getAttr(x+".translate")[0]
        locations.append(cl)
    start=locations[0];end=locations[1]
    #distance=math.sqrt((end[0]-start[0])**2+(end[1]-start[1])**2+(end[2]-start[2])**2)
    for h in range (jointsAmount ):
        for d in range(len(end)):
            if h==0:
                ref=start[d]
                temp.append(ref)
            else:
                ref=(((end[d]-start[d])/(jointsAmount-1))*(h))+start[d]
                temp.append(ref)
            if len(temp) == 3:
                    print temp
                    deliver.append((temp[0],temp[1],temp[2]))
                    del temp[:]    
    return deliver

def getNames():
    locations=getLocation()
    currentAmount=str(counter())
    jointNames=[]
    for x in range(jointsAmount):
        jointNames.append(("sbJoint"+str(x)+"_"+currentAmount,"IKJoint"+str(x)+"_"+currentAmount,"FKJoint"+str(x)+"_"+currentAmount,locations[x]))
    return jointNames

def createbones():
    sbJoints=[];ikJoints=[];fkJoints=[]
    jointNames=getNames()    
    mainGroup=cmds.group(em=True, n="bonesGrp")
    for x in jointNames:
        for y in x:
            if y != x[-1]:              
                cmds.select(clear=True)
                j=cmds.joint(n=y,p=x[3])
                cmds.parent(j,mainGroup) 
                if y == x[0]:
                    sbJoints.append(y)
                if y in x[1]:
                    ikJoints.append(y)
                if y in x[2]:
                    fkJoints.append(y)
                              
    jointSet=zip(sbJoints,ikJoints,fkJoints)        
    for x in range(len(jointNames)):      
        if jointNames[x] != jointNames[-1]:
            cmds.parent(fkJoints[x+1],fkJoints[x])
            cmds.parent(ikJoints[x+1],ikJoints[x])
            cmds.parent(sbJoints[x+1],sbJoints[x])
        
    cmds.select(clear=True)
    jointList.append(jointSet)
    return jointSet
    
def locator():
    del locators[:]
    def create(name):
        loc=cmds.spaceLocator(n=name+"_locator_"+str(counter()))
        annotation=cmds.annotate(loc,tx=name,p=(1,1,1))
        cmds.setAttr(annotation+".template",1)
        cmds.parent(annotation,loc)
        return loc
    start=create("start")[0]
    end=create("end")[0]
    cmds.setAttr(start+".translateX",5)
    locators.append(start)
    locators.append(end) 
    
def buildSlider(sliderWidth,sliderHeight,slideGroupName):
 
    SliderName=slideGroupName+'Ctrl'
    ctrlFrameName=slideGroupName+'Frame'
    
    f='Noto Sans Blk'
    szz=sliderWidth*5
    fontChoice=f+'|sz:'+str(szz)
    textGroup=slideGroupName+'_characters'
    
    cmds.curve(d=1,p=[(-1,0,1),(-1,0,-1),(1,0,-1),(1,0,1),(-1,0,1)],k=[0,1,2,3,4],n=ctrlFrameName)
    cmds.setAttr(ctrlFrameName+'.scaleX',sliderHeight)
    cmds.setAttr(ctrlFrameName+'.scaleZ',sliderWidth)
    cmds.setAttr(ctrlFrameName+'.template', 1)
    cmds.circle(n=SliderName,nr=(0,1,0),r=sliderHeight)
    cmds.circle(n=SliderName[1:-1],nr=(1,0,0),r=sliderHeight)
    cmds.circle(n=SliderName[:-1],nr=(0,0,1),r=sliderHeight)
    cmds.select(SliderName[:-1]+'Shape',SliderName[1:-1]+'Shape')
    cmds.parent(SliderName[:-1]+'Shape',SliderName[1:-1]+'Shape', SliderName, s=True,r=True)
    cmds.delete(SliderName[1:-1],SliderName[:-1])
    cmds.select(SliderName,ctrlFrameName)
    cmds.setAttr(SliderName+".tz",-sliderWidth)
    sliderGroup=cmds.group(SliderName,ctrlFrameName,n=slideGroupName)
    cmds.makeIdentity(apply=True, t=1,r=1,s=1,n=0,pn=1)
    cmds.transformLimits(SliderName,etz=(1,1),tz=(0, 2*sliderWidth))
            
    cmds.setAttr(SliderName+".tx",lock=True)
    cmds.setAttr(SliderName+".ty",lock=True)
    cmds.setAttr(SliderName+".rx",lock=True)
    cmds.setAttr(SliderName+".rz",lock=True)
    cmds.setAttr(SliderName+".ry",lock=True)
    cmds.setAttr(SliderName+".rz",lock=True)
    cmds.setAttr(SliderName+".sz",lock=True)
    cmds.setAttr(SliderName+".sy",lock=True)
    cmds.setAttr(SliderName+".sx",lock=True)
    cmds.setAttr(SliderName+".v",lock=True)
                    
    cmds.textCurves(f=fontChoice ,t=slideGroupName.replace("_"," ")[:-1],n=textGroup)
                      
    cmds.setAttr(textGroup+'Shape.rx',-90)
    cmds.setAttr(textGroup+'Shape.ry',-90)
    cmds.setAttr(textGroup+'Shape.tz',-sliderWidth)  
    cmds.setAttr(textGroup+'Shape.tx',sliderHeight)
    cmds.parent(textGroup+'Shape',ctrlFrameName)
    
    cmds.createNode('setRange',n=slideGroupName+'Range')
    cmds.setAttr(slideGroupName+"Range.ihi", 0)
    cmds.setAttr(slideGroupName+'Range.oldMinX',0)
    cmds.setAttr(slideGroupName+'Range.oldMaxX',sliderWidth)
    cmds.setAttr(slideGroupName+'Range.maxX',sliderWidth)
    cmds.connectAttr(SliderName+'.translate.translateZ',slideGroupName+'Range'+'.value.valueX')
    
    return sliderGroup

def switch():
    currentAmount=str(counter())
    ctrlList=[]
    IKctrlGrp=cmds.group(n="IKctrlgrp"+currentAmount,em=True)
    FKctrlGrp=cmds.group(n="FKctrlgrp"+currentAmount,em=True)
    ctrlGrp=cmds.group(n="ctrlgrp"+currentAmount)
    cmds.parent(IKctrlGrp,ctrlGrp)
    
    for x in jointList:
        print x
        slider=buildSlider(1,1,"ik_fk"+x[0][0][-2:]+"_")
        cmds.matchTransform(slider,x[0][0])
        getZ=cmds.getAttr(slider+".translateZ")
        cmds.setAttr(slider+".translateX",getZ+3)
        sliderCharacters=cmds.ls(slider,dag=1)[7]
        cmds.setAttr(sliderCharacters+".scaleX",5)
        cmds.setAttr(sliderCharacters+".scaleY",5)
        cmds.setAttr(sliderCharacters+".scaleZ",5)
        rangeNode=cmds.listConnections(slider+"Ctrl")[0]
        cmds.parent(slider,ctrlGrp)   
      
        for j in x:            
            ikBones=j[1] ;fkBones=j[2] ;skinnedBones=j[0]
            switch=cmds.createNode('blendColors')
            cmds.connectAttr(rangeNode+".outValueX",switch+".blender")
            cmds.connectAttr(ikBones+".rotate",switch+".color2")
            cmds.connectAttr(fkBones+".rotate",switch+".color1")
            cmds.connectAttr(switch+".output",skinnedBones+".rotate")        
            ctrl=cmds.circle( nr=(0, 0, 1),r=2,n=fkBones+"_ctrl")
            cmds.matchTransform(ctrl,fkBones)
            cmds.parent(ctrl,FKctrlGrp)
            cmds.makeIdentity(ctrl,apply=True, t=1,r=1,s=1,n=0,pn=1)
            cmds.parentConstraint(ctrl,fkBones)
            ctrlList.append(ctrl)
    for p in range(len(ctrlList)):      
        if ctrlList[p] != ctrlList[-1]:
            cmds.parent(ctrlList[p+1],ctrlList[p])
    del ctrlList[:]
