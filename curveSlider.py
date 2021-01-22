import maya.cmds as cmds

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
    cmds.group(SliderName,ctrlFrameName,n=slideGroupName)
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
    cmds.setAttr(slideGroupName+'Range.oldMaxX',2*sliderWidth)
    cmds.connectAttr(SliderName+'.translate.translateZ',slideGroupName+'Range'+'.value.valueX')


#buildSlider(sliderWidth,sliderHeight,slideGroupName)
