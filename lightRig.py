# thanks to Frank Ruiz De Castilla for helping me
import maya.cmds as cmds
import uuid 

currentLight=[];angleX=[];angleY=[];angleZ=[];translateX=[];translateY=[];translateZ=[];intensityRatio=[];lightNames=[];AimLights=[];LightCtrls=[];aimEachOption=[];aimAllOption=[];
finalLights=[];toolsOptions=[];presetsOptions=[];lightShapes=[];sliderOption=[];LightCtrlsBackUP=[]
windowName="lightRigs"
intensity=10
size=9
uuid=str(int(uuid.uuid1()))
sliderName="slider"+str(len(intensityRatio))+uuid
def AreaLight(object):del currentLight [:];currentLight.append('cmds.cmdArnoldAreaLights(n=lightName)')
def SkydomeLight(object):del currentLight [:];currentLight.append('cmds.cmdSkydomeLight(n=lightName)')    
def PhotometricLight(object):del currentLight [:];currentLight.append('cmds.cmdPhotometricLights(n=lightName)')
def DirectionalLight(object):del currentLight [:];currentLight.append('cmds.CreateDirectionalLight(n=lightName)')
def PointLight(object):del currentLight [:];currentLight.append('cmds.CreatePointLight(n=lightName)')
def SpotLight(object):del currentLight [:];currentLight.append('cmds.CreateSpotLight(n=lightName)')
def aimEachON(object):aimEachOption.append('Do It')
def aimEachOff(object):del aimEachOption [:]
def aimAllON(object):aimAllOption.append('Do It')
def aimAllOff(object):del aimAllOption [:]
def toolsOptionsOff(object):del toolsOptions [:];del presetsOptions [:]
def toolsOptionsOn(object):toolsOptions.append('Do It');presetsOptions.append('Do It')
def sliderOn(object):sliderOption.append('Do It')
def sliderOff(object):del sliderOption [:]
def keyLight(object):angle=45;angleY.append(angle);intensityRatio.append(intensity);lightNames.append('key')
def fillLight(object):angle=-45;angleY.append(angle);intensityRatio.append(intensity/2);lightNames.append('fill')
def backLight(object):angle=135;angleY.append(angle);intensityRatio.append(intensity/20);lightNames.append('back')
def threeLightSetup(object):keyLight('');fillLight('');backLight('')
def twoLightSetup(object):keyLight('');fillLight('')
def justKeyLight(object):keyLight('')
def justFillLight(object):fillLight('')
def justBackLight(object):backLight('')

def eraseLists():
    del angleX [:]
    del angleY [:]
    del angleZ [:]
    del intensityRatio [:]
    del lightNames [:]
    del AimLights [:]
    del LightCtrls [:]
    del aimEachOption [:]
    del aimAllOption [:]
    del toolsOptions [:]
    del presetsOptions [:]
    print "selections erased"

def splitPortrait(object):
    zeroAttributes('')
    cmds.setAttr(finalLights[0]+"mainCtrl"+".translateY", 4.3)
    cmds.setAttr(finalLights[0]+"mainCtrl"+".rotateX",20)
    cmds.setAttr(finalLights[0]+"mainCtrl"+".rotateY",-126)
    cmds.setAttr(finalLights[0]+"mainCtrl"+".rotateZ",-19)
    cmds.setAttr(lightShapes[0]+".intensity", 2000)
    cmds.setAttr(finalLights[1]+"mainCtrl"+".rotateY",135)
    cmds.setAttr(finalLights[1]+"mainCtrl"+".translateY",4)
    cmds.setAttr(lightShapes[1]+".intensity", 5000)

def highKey(object):
    zeroAttributes('')
    cmds.setAttr(finalLights[0]+"mainCtrl"+".translateY", 4.3)
    cmds.setAttr(finalLights[0]+"mainCtrl.rotateY", -75)
    cmds.setAttr(finalLights[0]+".rotateY", 51)
    cmds.setAttr(lightShapes[0]+".intensity", 100)
    cmds.setAttr(finalLights[1]+"mainCtrl.rotateY", 132.8)
    cmds.setAttr(finalLights[1]+"mainCtrl.translateY", 4.3)
    cmds.setAttr(finalLights[1]+"mainCtrl.rotateX", 39)
    cmds.setAttr(finalLights[1]+"mainCtrl.rotateZ", 52.4)
    cmds.setAttr(finalLights[1]+"mainCtrl.scaleZ", 1.4)
    cmds.setAttr(finalLights[1]+"mainCtrl.scaleY", 1.4)
    cmds.setAttr(finalLights[1]+"mainCtrl.scaleX", 1.4)
    cmds.setAttr(lightShapes[1]+".intensity", 50)
    cmds.setAttr(finalLights[2]+"mainCtrl.translateY", 14.3)
    cmds.setAttr(finalLights[2]+"mainCtrl.rotateX", 42.5)
    cmds.setAttr(finalLights[2]+"mainCtrl.rotateZ", 41)
    cmds.setAttr(finalLights[2]+"mainCtrl.rotateY", 57.6)
    cmds.setAttr(finalLights[2]+"mainCtrl.scaleY", 0.9)
    cmds.setAttr(finalLights[2]+"mainCtrl.scaleZ", 0.9)
    cmds.setAttr(finalLights[2]+"mainCtrl.scaleX", 0.9)
    cmds.setAttr(lightShapes[2]+".intensity", 250)

def zeroAttributes(object):
    for x in range (len(finalLights)):
        cmds.setAttr(finalLights[x]+".rotate", 0,0,0)
        cmds.setAttr(finalLights[x]+".translate", 0,0,10)
        cmds.setAttr(finalLights[x]+".scale", 1,1,1)
        cmds.setAttr(finalLights[x]+"mainCtrl.rotate", 0,0,0)
        cmds.setAttr(finalLights[x]+"mainCtrl.translate", 0,0,0)
        cmds.setAttr(finalLights[x]+"mainCtrl.scale", 1,1,1)

def setIntensityRatio(object):
    getKey=cmds.getAttr(finalLights[0]+".intensity")
    cmds.setAttr(lightShapes[1]+".intensity", getKey/2)
    cmds.setAttr(lightShapes[2]+".intensity", getKey/20)

def setRGB(object):
    cmds.setAttr(lightShapes[0]+".color", 1,0,0)
    cmds.setAttr(lightShapes[1]+".color", 0,1,0)
    cmds.setAttr(lightShapes[2]+".color", 0,0,1)

def setWhiteLights(object):
    cmds.setAttr(lightShapes[0]+".color", 1,1,1)
    cmds.setAttr(lightShapes[1]+".color", 1,1,1)
    cmds.setAttr(lightShapes[2]+".color", 1,1,1)

def lightManufacture(angX,angY,angZ,intensityValue,baseName,transX,transY,transZ,xAmount):

    lightsAmount=len(cmds.ls(type="light"))+1
    lightName=baseName + str(lightsAmount)
    dSize=size+xAmount
    light= eval(currentLight[0])
    
    cmds.rename( light, lightName )
    finalLights.append(lightName)
    cmds.group(lightName,n=lightName+'Grp')
    cmds.setAttr(lightName+'.translateZ',10)
    cmds.circle(n=lightName+'mainCtrl',nr=(0,1,0),r=dSize)
    lightShapes.append(baseName+'Shape'+str(lightsAmount))
    LightCtrls.append(lightName+'mainCtrl')
    LightCtrlsBackUP.append(lightName+'mainCtrl')
    cmds.makeIdentity(apply=True, t=1,r=1,s=1,n=0,pn=1)
    if len(aimEachOption)>0:
        aimCtrl(lightName)
        cmds.select(lightName+'Aim',lightName)
        cmds.aimConstraint(mo=True)
    cmds.parent(lightName+'Grp',lightName+'mainCtrl')
    cmds.setAttr(baseName+'Shape'+str(lightsAmount)+'.intensity',intensityValue)
    cmds.setAttr(lightName+'Grp.rotateX',angX)
    cmds.setAttr(lightName+'Grp.rotateY',angY)
    cmds.setAttr(lightName+'Grp.rotateZ',angZ)
    if baseName != "noSetup":
        cmds.textCurves(f='Noto Sans Blk' ,t=baseName)
        cmds.rename('Text_'+baseName+'_'+ '1',baseName+'text'+str(lightsAmount))
        cmds.matchTransform(baseName+'text'+str(lightsAmount),lightName)
        cmds.parent(baseName+'text'+str(lightsAmount),lightName)
        cmds.setAttr(baseName+'text'+str(lightsAmount)+".template",1)
        cmds.setAttr(baseName+'text'+str(lightsAmount)+".translateZ",xAmount-1)
        cmds.setAttr(baseName+'text'+str(lightsAmount)+".rotateX",-90)

    cmds.setAttr(lightName+'mainCtrl.translateX',transX)  
    cmds.setAttr(lightName+'mainCtrl.translateY',transY) 
    cmds.setAttr(lightName+'mainCtrl.translateZ',transZ)
    if len(sliderOption)>0:
        cmds.makeIdentity(lightName+'Grp',apply=True, t=1,r=1,s=1,n=0,pn=1)
        sliderConnect(lightName)

def slider(sliderName):

    cmds.curve(d=1,p=[(-1,0,1),(-1,0,-1),(1,0,-1),(1,0,1),(-1,0,1)],k=[0,1,2,3,4],n=sliderName+'ctrlFrame')
    cmds.setAttr(sliderName+'ctrlFrame.scaleX',0.4)
    cmds.setAttr(sliderName+'ctrlFrame.scaleZ',7.8)
    cmds.circle(n=sliderName+'mCtrl',nr=(0,1,0),r=0.36)
    cmds.circle(n=sliderName+'C1',nr=(1,0,0),r=0.36)
    cmds.circle(n=sliderName+'C2',nr=(0,0,1),r=0.36)
    cmds.select(sliderName+'C2Shape',sliderName+'C1Shape')
    cmds.parent(sliderName+'C2Shape',sliderName+'C1Shape', sliderName+'mCtrl', s=True,r=True)
    cmds.delete(sliderName+'C1',sliderName+'C2')
    cmds.select(sliderName+'mCtrl',sliderName+'ctrlFrame')
    cmds.makeIdentity(apply=True, t=1,r=1,s=1,n=0,pn=1)
    cmds.group(sliderName+'mCtrl',sliderName+'ctrlFrame',n=sliderName+'CtrlGrp')
    cmds.setAttr(sliderName+'CtrlGrp.translateX',16)
    cmds.transformLimits(sliderName+'mCtrl',etz=(1,1),tz=(-7.8, 7.8),ty=(0,0),tx=(0,0))
    cmds.transformLimits(sliderName+'mCtrl',ety=(1,1),ty=(0,0))
    cmds.transformLimits(sliderName+'mCtrl',etx=(1,1),tx=(0,0))
    cmds.select(sliderName+'CtrlGrp')
    cmds.makeIdentity(apply=True, t=1,r=1,s=1,n=0,pn=1)
    cmds.setAttr(sliderName+"ctrlFrame.template", 1) 

    cmds.createNode('setRange',n=sliderName+'hourRange')
    cmds.setAttr(sliderName+'hourRange.maxX',24)
    cmds.setAttr(sliderName+'hourRange.oldMinX',-7.8)
    cmds.setAttr(sliderName+'hourRange.oldMaxX',7.8)

    cmds.createNode('setRange',n=sliderName+'degreesRange')
    cmds.setAttr(sliderName+'degreesRange.maxX',360)
    cmds.setAttr(sliderName+'degreesRange.oldMinX',0)
    cmds.setAttr(sliderName+'degreesRange.oldMaxX',24)

    cmds.connectAttr(sliderName+'hourRange.outValueX', sliderName+'degreesRange.valueX')
    cmds.connectAttr(sliderName+'mCtrl.translateZ', sliderName+'hourRange.valueX')
    cmds.createNode('plusMinusAverage',n=sliderName+'plusRotation')
    cmds.connectAttr(sliderName+'degreesRange.outValueX',sliderName+'plusRotation.input1D[0]')

def sliderConnect(lightName):
    cmds.connectAttr(sliderName+'plusRotation.output1D',lightName+'Grp.rotateY')

def squareCtrl():
    defaultSquare=cmds.nurbsSquare(nr=(0, 1, 0), sl1=size*3, sl2=size*3 )
    defaultSquareList=cmds.ls(defaultSquare,dag=1)
    square=cmds.group(em=True,n='mainCtrl')
    global square
    for x in range (len(defaultSquareList)):
        if 'Shape' in defaultSquareList[x]:
            cmds.parent(defaultSquareList[x],square,r=True,s=True)
    cmds.parent(sliderName+'CtrlGrp',square,r=True,s=True)
    cmds.delete(defaultSquare)
    cmds.makeIdentity(square,apply=True, t=1,r=1,s=1,n=0,pn=1)
    cmds.select(clear=True)
    return square

def aimCtrl(lightName):
    cmds.circle(n=lightName+'Aim')
    AimLights.append(lightName+'Aim')
    cmds.parent(lightName+'Aim',lightName+'Grp')
    cmds.setAttr(lightName+'Aim.translateZ',6.5)

def mainAim():
    mainAimName="mainAim"+uuid
    circle1=cmds.ls(cmds.circle(nr=(1,0,0),n=mainAimName),dag=1)
    circle2=cmds.ls(cmds.circle(nr=(0,1,0)),dag=1)
    circle3=cmds.ls(cmds.circle(nr=(0,0,1)),dag=1)
    cmds.parent(circle3[1],circle2[1],circle1[0],r=True,s=True)
    cmds.delete(circle3[0],circle2[0])
    cmds.makeIdentity(circle1,apply=True, t=1,r=1,s=1,n=0,pn=1)
    LightCtrls.append(mainAimName)
    if len(aimEachOption)>0:
        for x in range(len(AimLights)):
            cmds.parentConstraint(mainAimName,AimLights[x],mo=True)
    else:
        for x in range(len(finalLights)):
            cmds.aimConstraint(mainAimName,finalLights[x],mo=True)

def deliver(ss):
    if len(sliderOption)>0:
        slider(sliderName)
    if len(intensityRatio)==0:
        lightManufacture(0,0,0,10,"noSetup",0,0,0,0)
        cmds.select(clear=True)
        if len(presetsOptions) + len(toolsOptions) >0:
            accessoryWindow()

    if len(intensityRatio)>0:
        for x in range(len(intensityRatio)):
            
            angleX.append(0);angleY.append(0);angleZ.append(0);translateX.append(0);translateY.append(0);translateZ.append(0)
            lightManufacture(angleX[x],angleY[x],angleZ[x],intensityRatio[x],lightNames[x],translateX[x],translateY[x],translateZ[x],x)
            if x == len(intensityRatio)-1:
                if len(aimAllOption) >0:
                    mainAim()
                groupName="LightsGrp"+str(len(cmds.ls(type="light")))
                cmds.group(em=True,n=groupName)

                for x in range(len(LightCtrls)):
                    cmds.parent(LightCtrls[x],groupName)

                squareCtrl()
                cmds.parent(groupName,square)
                cmds.select(clear=True)
                    
    if len(presetsOptions) + len(toolsOptions) >0:
        accessoryWindow()
        print finalLights
    if len(presetsOptions) + len(toolsOptions) ==0:
        del finalLights[:]
    cmds.deleteUI(windowName)
      

    eraseLists()
    
def accessoryWindow():
    windowN="lightTools"
    if (cmds.window(windowN,q=True,ex=True)):
        cmds.deleteUI(windowN)
    cmds.window(windowN,t=windowN)
    cc=cmds.columnLayout()
    
    if toolsOptions >0:
        for x in range(len(finalLights)):
            cmds.attrFieldSliderGrp( at=finalLights[x]+'.intensity',l=finalLights[x])
        cmds.separator(h=10)
        
        cmds.rowLayout(nc=2,p=cc)    
        cmds.button(l="set intensity ratio",c=setIntensityRatio)
        cmds.separator(h=10)
    if presetsOptions >0:
        bottom1=cmds.rowLayout(nc=3,p=cc)
        cmds.button(l="splitPortrait",c=splitPortrait)
        cmds.button(l="highKey",c=highKey)
        cmds.iconTextCheckBox( style='textOnly', label="RGB",onc=setRGB,ofc=setWhiteLights, bgc=[0.37,0.37,0.37],fla=False)
    cmds.showWindow()

def sun(object):
    DirectionalLight('')
    threeLightSetup('')
    aimAllON('')
    sliderOn('') 
    deliver('')
    cmds.setAttr(square+".rotateX",-90)
    cmds.setAttr(square+".scale",22,22,22)
    cmds.setAttr(LightCtrlsBackUP[0]+".rotateZ",-45)
    cmds.setAttr(LightCtrlsBackUP[0]+".rotateY",-45)
    cmds.setAttr(LightCtrlsBackUP[1]+".rotateZ",45)
    cmds.setAttr(LightCtrlsBackUP[1]+".rotateX",180)
    cmds.setAttr(LightCtrlsBackUP[1]+".rotateY",135)
    cmds.setAttr(LightCtrlsBackUP[2]+".rotateZ",90)
    cmds.setAttr(LightCtrlsBackUP[2]+".rotateY",-135)

    if hourChosen <=6:
        sliderHour=hourChosen*3.9/6    
    if hourChosen >6:
        sliderHour=hourChosen*7.8/12    
    if hourChosen >=12:
        sliderHour=((hourChosen*11.7/18)-15.6)    
    if hourChosen >18:
        sliderHour=((hourChosen*15.6/24)-15.6)
    cmds.setAttr(sliderName+"mCtrl.translateZ",sliderHour)

    del LightCtrlsBackUP [:]

def lightRigger():
    if (cmds.window(windowName,q=True,ex=True)):
        cmds.deleteUI(windowName)
    cmds.window(windowName,rtf=True,s=True)    
    main=cmds.rowColumnLayout( numberOfColumns=1)

    allTabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    lightRigs=cmds.columnLayout(p=allTabs) 

    cmds.tabLayout(allTabs,edit=True, tabLabel=( (lightRigs, 'lightRigs')))
    firstHalf=cmds.columnLayout(p=lightRigs)
    firstRadio=cmds.gridLayout(p=firstHalf,cw=80,ch=20)
    
    cmds.radioCollection()
    cmds.radioButton( label='Area Light',p=firstRadio, cc=AreaLight)
    #cmds.radioButton( label='Skydome',p=bottom, cc=SkydomeLight)    
    cmds.radioButton( label='Photometric',p=firstRadio, cc=PhotometricLight) 
    cmds.radioButton( label='Directional',p=firstRadio, cc=DirectionalLight)  
    cmds.radioButton( label='Point',p=firstRadio, cc=PointLight)
    cmds.radioButton( label='Spot',p=firstRadio, cc=SpotLight)
    
    spacer=cmds.columnLayout(p=lightRigs)
    secondHalf=cmds.columnLayout(p=lightRigs)
    cmds.separator(p=spacer,h=10)
    secondRadio=cmds.gridLayout(p=spacer,cw=80,ch=20)
    
    cmds.radioCollection()
    cmds.radioButton( label="no setup",p=secondRadio, cc=SpotLight)
    cmds.radioButton( label="two lights",cc=twoLightSetup,p=secondRadio)
    cmds.radioButton( label="three lights", cc=threeLightSetup,p=secondRadio)
    cmds.radioButton( label="fill light",cc=justFillLight,p=secondRadio)
    cmds.radioButton( label="key light",cc=justKeyLight,p=secondRadio)
    cmds.radioButton( label="back light",cc=justBackLight,p=secondRadio)
    
    thirdHalf=cmds.columnLayout(p=lightRigs)
    cmds.separator(p=spacer,h=10) 
    cmds.iconTextRadioCollection() 
    cmds.rowLayout(nc=1, cw1=100, p=thirdHalf)
    cmds.iconTextRadioButton( style='textOnly', label="no aim ctrls",sl=1, bgc=[0.37,0.37,0.37],fla=False,w=242)
    cmds.rowLayout(nc=3, cw3=(100,40,100), p=thirdHalf)
    
    cmds.iconTextRadioButton( style='textOnly', label="aim ctrl for each light",onc=aimEachON,ofc=aimEachOff, bgc=[0.37,0.37,0.37],fla=False,w=120)
    cmds.iconTextRadioButton( style='textOnly', label="aim ctrl for all lights",onc=aimAllON,ofc=aimAllOff, bgc=[0.37,0.37,0.37],fla=False,w=120)
    
    fourthHalf=cmds.columnLayout(p=lightRigs)
    cmds.separator(p=fourthHalf,h=10)
    cmds.rowLayout(nc=3, cw3=(100,40,100), p=fourthHalf)    

    cmds.checkBox( label='light tools', align='left',onc=toolsOptionsOn,ofc=toolsOptionsOff)
    cmds.checkBox( label='slider ctrl', align='left',onc=sliderOn,ofc=sliderOff )    
    cmds.separator(p=fourthHalf,h=10)
    
    cmds.rowLayout(nc=1, cw1=100, p=fourthHalf)
    cmds.button(l="create light",w=242,c=deliver, rs=True)
    
    cmds.showWindow() 
       
lightRigger()
