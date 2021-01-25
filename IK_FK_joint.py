import maya.cmds as cmds

jointList=[]
def counter(): return len(cmds.ls("mainGroup*",type='locator'))
def getNames():
    currentAmount=str(counter())
    jointNames=[
    ("sbJoint1_"+currentAmount,"IKJoint1_"+currentAmount,"FKJoint1_"+currentAmount,(0, 0, 5)),
    ("sbJoint2_"+currentAmount,"IKJoint2_"+currentAmount,"FKJoint2_"+currentAmount,(0, 0, 0)),
    ("sbJoint3_"+currentAmount,"IKJoint3_"+currentAmount,"FKJoint3_"+currentAmount,(0, 0,-5))]
    return jointNames

def createbones():
    firstJoints=[];secondJoints=[];thirdJoints=[];locators=[];averagePosition=[]
    jointNames=getNames()
    for x in range(3):
        averagePosition.append((jointNames[1][3][x]+jointNames[1][3][x]+jointNames[1][3][x])/3)
    mainGroup=cmds.spaceLocator(p=(averagePosition),n="mainGroup")
    del averagePosition[:]
    cmds.setAttr(mainGroup[0]+".translateY",4 )
    cmds.xform(cp=True)
    cmds.makeIdentity(mainGroup,apply=True, t=1,r=1,s=1,n=0,pn=1)

    for x in jointNames:

        loc=cmds.spaceLocator(n="loc"+x[1],p=x[3],a=True)

        cmds.setAttr("loc"+x[1]+".translateY",1 )
        cmds.xform(cp=True)
        cmds.parent(loc[0],mainGroup)
        locators.append(loc)
        for y in x:
            if y != x[3]:
                cmds.select(clear=True)
                j=cmds.joint(n=y,p=x[3])
                cmds.parent(j,mainGroup)
                if y in jointNames[0]:
                    firstJoints.append(j)
                if y in jointNames[1]:
                    secondJoints.append(j)
                if y in jointNames[2]:
                    thirdJoints.append(j)              
                              
    jointSet=zip(firstJoints,secondJoints,thirdJoints)        
    for x in range(len(jointNames)):
        cmds.parent(thirdJoints[x],secondJoints[x])
        cmds.parent(secondJoints[x],firstJoints[x])
        cmds.parentConstraint(locators[0],firstJoints[x],mo=True)
        cmds.parentConstraint(locators[1],secondJoints[x],mo=True)
        cmds.parentConstraint(locators[2],thirdJoints[x],mo=True)
    cmds.select(clear=True)
    jointList.append(jointSet)
    return jointSet

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
    ctrlList=[]
    IKctrlGrp=cmds.group(n="IKctrlgrp",em=True)
    FKctrlGrp=cmds.group(n="FKctrlgrp",em=True)
    ctrlGrp=cmds.group(n="ctrlgrp")
    cmds.parent(IKctrlGrp,ctrlGrp)
    
    for x in jointList:
    
        slider=buildSlider(1,1,"ik_fk"+x[0][0][-2:]+"_")
        cmds.matchTransform(slider,x[0][0])
        getZ=cmds.getAttr(slider+".translateZ")
        cmds.setAttr(slider+".translateZ",getZ+3)
        sliderCharacters=cmds.ls(slider,dag=1)[7]
        cmds.setAttr(sliderCharacters+".scaleX",5)
        cmds.setAttr(sliderCharacters+".scaleY",5)
        cmds.setAttr(sliderCharacters+".scaleZ",5)
        rangeNode=cmds.listConnections(slider+"Ctrl")[0]
        cmds.parent(slider,ctrlGrp)   
      
        for S in range(len(x)):
            
            ikBones=x[1][S] ;fkBones=x[2][S] ;skinnedBones=x[0][S]       
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
            if len(ctrlList) == 3:
                cmds.parent(ctrlList[2],ctrlList[1])
                cmds.parent(ctrlList[1],ctrlList[0])
                del ctrlList[:]
          
        
        
        
#fsds
