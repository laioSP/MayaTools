import maya.cmds as cmds
import maya.mel as mel
import re

arri_prime_lenses = ["8mm/T2.8", "12mm/T1.3", "12mm/T1.8", "12mm/T2.0", "14mm/T1.3", "15mm/T1.8", "16mm/T1.3", "18mm/T1.8", "21mm/T1.8",
"25mm/T1.8", "27mm/T1.3", "29mm/T1.8", "32mm/T1.3", "35mm/T1.8", "40mm/T1.8", "50mm/T1.3", "47mm/T1.8", "58mm/T1.8", "65mm/T1.3", "75mm/T1.8", 
"95mm/T1.8", "100mm/T1.3", "125mm/T1.8", "135mm/T1.3", "150mm/T1.8", "200mm/T2.5", "280mm/T2.8"]
cooke_prime_lenses = ["12mm/T2.0","14mm/T2.0","16mm/T2.0","18mm/T1.4", "21mm/T2.0", "25mm/T1.4","27mm/T2.0","32mm/T1.4", "40mm/T1.4", "50mm/T1.4",
"65mm/T1.4", "75mm/T1.4", "100mm/T1.4","100mm/T2.0", "135mm/T1.4","150mm/T2.0","180mm/T2.0", "300mm/T2.8"]
zeiss_prime_lenses = ["15mm/T1.8", "18mm/T1.5", "21mm/T1.5", "25mm/T1.5", "29mm/T1.5", "35mm/T1.5", "40mm/T1.5", "50mm/T1.5", "65mm/T1.5", 
"85mm/T1.5", "100mm/T1.5", "135mm/T1.5", "150mm/T1.8", "200mm/T2.2"]
canon_primeCinema_lenses = ["14mm/T3.1", "20mm/T1.5", "24mm/T1.5", "35mm/T1.5", "50mm/T1.3", "85mm/T1.3", "135mm/T2.2"]
canon_primeDslr_lenses = ["14mm/F2.8", "24mm/F1.4", "35mm/F1.4", "50mm/F1.2", "85mm/F1.2", "135mm/F2.0", "200mm/F2.0", "300mm/F2.8", "400mm/F2.8",
 "500mm/F4.0", "600mm/F4.0", "800mm/F5.6"]
schneider_prime_lenses = ['14mm/T2.2','18mm/T2.2','25mm/T2.1','35mm/T2.1','50mm/T2.0','75mm/T2.0','95mm/T2.0','100mm/T2.1']
panavision_prime_lenses = ['10mm/T1.9','14.5mm/T1.9','17.5mm/T1.9','21mm/T1.9','35mm/T1.9','40mm/T1.9','50mm/T1.9','65mm/T1.8','75mm/T1.9','85mm/T1.8'
,'100mm/T1.9','125mm/T1.8','150mm/T1.9']
arri_zoom_lenses = ['9.5-18mm/T2.9','15.5-45mm/T2.8','18-80mm/T2.6','30-80mm/T2.8','45-250mm/T2.6']
zeiss_zoom_lenses = ['15-30mm/T0.9','28-80mm/T2.9','70-200mm/T2.9']
canon_zoomCinema_lenses=['14.5-60mm/T2.6','15.5-47mm/T2.8','17-120mm/T2.95','18-80mm/T4.4','30-105mm/T2.8','70-200mm/T4.4']
canon_zoomDslr_lenses=['8-15mm/F4.0','11-24mm/F4.0','16-35mm/F2.8','17-40mm/F4.0','24-70mm/F2.8','70-200mm/F2.8']
fujinon_zoom_lenses =['14-35mm/T2.9','14.5-45mm/T2.0','18-85mm/T2.0','20-120mm/T3.5','24-180mm/T2.6','25-300mm/T3.5','28-100mm/T2.9']
panavision_zoom_lenses =['15-40mm/T2.6','19-90mm/T2.8','17.5-75mm/T2.3','24-275mm/T2.8','24.5-105mm/T3.2','27-75mm/T2.6','34-385mm/T4.0',
'135-420mm/T2.8','190-590mm/T4.0'];
camerasCC=['alexa 65/A3X','alexa_LF/A2X','alexa_LF/A2X','alexa_sxt_w/Super_35_alev_III','alexa_mini/Super_35_alev_III','amira/Super_35_alev_III',
'ursa_mini_Pro/super35_black_magic','ursa_broadcast/twoThirds_inch_black_magic','phantom_flex_4k/Super_35_phantom','sony_venice/sony_35mm',
'monstro_8k/monstro_8k','helium_8k/helium_8k','gemini/s35mm_5k','dragon-x_6k_s35/dragon6k_s35','EOS_C700_FF/canon5_9K','EOS_C500_mark_II/canon5_9K',
'EOS_C300/canonSuper_35mm','canon_EOS_RP/fullFrame','canon_EOS_5D_Mark_IV/fullFrame', 'canon_EOS_6D_Mark_II/fullFrame','canon_EOS_90D/canonApsc',
'nikon_D500/nikonApsc','Nikon_D750/fullFrame','iPhoneXs/iPhoneMax','iPhoneXs/iPhoneMax','iPhoneMax/iPhoneMax','iPhone5/iPhone5','iPhone5S/iPhone6','iPhone6/iPhone6',
'iPhone4S/iPhone4S','LG_G3/iPhone6']  

shutterAngle=[144];ShutterType=[0];current_Lenses=[];current_camera=['default'];current_prime=[];current_zoom=[];LensesNodes=[];IrisNodes=[];annotationNames=[];
motionBlur=[0];depthOfField=[0];NearClip=[0];FarClip=[0];Frustum=[0];RollingShutter=[0];RollingShutterDuration=[0];toolWindow=[''];cameraControls=['1'];accessoryNode=[]
currentCamName=['default'];custom_sensor=[];custom_lensMin=[18];custom_lensMax=[200];custom_blades=[6];custom_curvature=[0];custom_fStop=[1.8];manufacturedCustom=[]
rigSelection=['not']

ArriSignature ={"blades":11,"curvature":0.5}; ArriMaster={"blades":9,"curvature":0.5}; CookeS4={"blades":9,"curvature":0}; ZeissSupreme={"blades":16,"curvature":0.5};
CanonPrimeCinema={"blades":11,"curvature":0.5}; CanonPrimeDslr={"blades":9,"curvature":0.5}; SchneiderXenon={"blades":14,"curvature":0.1}; PanavisionPrimoPrime={"blades":11,"curvature":0.5};
ArriAluraZoom={"blades":9,"curvature":0.5}; ZeissZoom={"blades":16,"curvature":0.5}; CanonZoomCinema={"blades":11,"curvature":0.5}; CanonZoomDslr={"blades":8,"curvature":0.5};
fujinonCabrio={"blades":9,"curvature":0.5}; PanavisionPrimoZoom={"blades":11,"curvature":0.5}; UserLens={"blades":custom_blades[0],"curvature":custom_curvature[0]}

default=[36.000,24.000]
Super_35_alev_III=[28.25,18.17];A2X=[36.70,25.54];A3X=[54.12,25.58];monstro_8k=[40.96,21.60];helium_8k=[29.90,15.77];gemini_5k_s35=[30.72,18];
dragon6k_s35=[30.7,15.8];super35_black_magic=[25.34,14.25];twoThirds_inch_black_magic=[13.056,7.344];Super_35_phantom=[27.6,15.5];sony_35mm=[36.2,24.1];
fullFrame=[35.9,24.0];canon5_9K=[38.1,20.1];canonSuper_35mm=[24.6,13.8];s35mm_5k=[30.72,18];canonApsc=[22.3,14.8];nikonApsc=[23.5,15.7];
iPhone4S=[3,264,2,448];iPhone6=[4.80,3.60];iPhone5=[4.54,3.42];iPhoneMax=[5.6,4.2];disableDefaultCamera=[];

AP=ArriSignature;CP=CookeS4;ZP=ZeissSupreme;CP=CanonPrimeCinema;DP=CanonPrimeDslr;SP=SchneiderXenon;PP=PanavisionPrimoPrime;AZ=ArriAluraZoom;ZZ=ZeissZoom;CZ=CanonZoomCinema;
DZ=CanonZoomDslr;FZ=fujinonCabrio;PZ=PanavisionPrimoZoom;XZ=UserLens

cycle=str(len(cmds.ls(type='camera'))-3)
lens_SliderName='lenses'+cycle
zoom_SliderName='Zoom'+cycle
FStop_SliderName="fStop"+cycle
windowName="cameraMaker"
actualCameraName='cam'
cameraName='cam'+cycle

class lensesFabrication(object):
    def __init__(self,lensLength):
        self.lensLength=lensLength
             
    def manufacturing(self,lensLength):
        current_Lenses.append(lensLength)
        print current_Lenses

    def customMaxLens(self,lensLength):
        del custom_lensMax[:]
        custom_lensMax.append(round(lensLength,2))
        print custom_lensMax
        print round(lensLength,2)

    def customMinLens(self,lensLength):
        del custom_lensMin[:]
        custom_lensMin.append(round(lensLength,2))
        print custom_lensMin
        print round(lensLength,2)

    def customFStop(self,lensLength):
        del custom_fStop[:]
        custom_fStop.append(round(lensLength,2))
        print custom_fStop
        print round(lensLength,2)

    def customBlades(self,lensLength):
        del custom_blades[:]
        custom_blades.append(lensLength)
        print custom_blades
        print lensLength

    def customCurvature(self,lensLength):
        del custom_curvature[:]
        custom_curvature.append(round(lensLength,1))
        print custom_curvature
        print round(lensLength,1)

    def create(self,lensLength):
        del manufacturedCustom[:]
        manufacturedCustom.append('XZ_'+str(custom_lensMin[0])+'-'+str(custom_lensMax[0])+'mm'+'/F'+str(custom_fStop[0])+'__')
        current_Lenses.append(manufacturedCustom[0])
        print current_Lenses
    def delete(self,lensLength):
        current_Lenses.remove(manufacturedCustom[0])
        print current_Lenses
    def trash(self,lensLength):
        current_Lenses.remove(lensLength)
        print current_Lenses
    
class cameraFabrication(object):
    def __init__(self,cameraSensor,height,width,shutterA,ShutterT,motionB,depthOfF,near,far,fru,duration,rolling,Ccontrols):
        self.cameraSensor=cameraSensor
        self.height=height
        self.width=width
        self.shutterA=shutterA
        self.ShutterT=ShutterT
        self.motionB=motionB
        self.depthOfF=depthOfF
        self.near=near
        self.far=far
        self.fru=fru
        self.duration=duration
        self.rolling=rolling
        self.Ccontrols=Ccontrols

    def manufacturing(self,cameraSensor):
        del currentCamName[:]
        del current_camera[:]
        [sensor]=re.split('/',cameraSensor)[1:]
        [camName]=(re.split('/',cameraSensor)[:1])
        current_camera.append(sensor)
        currentCamName.append(camName[7:])
        print current_camera
        print currentCamName

    def custom(self,height,width):
        del current_camera[:]
        del custom_sensor[:]
        del currentCamName[:]
        custom_sensor.append(height)
        custom_sensor.append(width)
        current_camera.append('custom_sensor')
        currentCamName.append('customCamera')
        print current_camera
        print 'height '+str(height)
        print 'width '+str(width)
        print current_camera
        
    def shutterAng(self,shutterA):
        del shutterAngle[:]
        shutterAngle.append(shutterA)
        print shutter
        
    def ShutterTy(self,ShutterT):
        del ShutterType[:]
        box=0;triangle=1;curve=2
        ShutterType.append(eval(ShutterT))
        print ShutterType
        
    def motionBlu(self,motionB):
        del motionBlur[:]
        motionBlur.append(motionB)
        print motionBlur
        
    def depthOfFie(self,depthOfF): 
        del depthOfField[:]
        depthOfField.append(depthOfF)
        print depthOfField

    def NearC(self,near):
        del NearClip[:]
        NearClip.append(near)
        print NearClip
        
    def FarC(self,far):
        del FarClip[:]
        FarClip.append(far)
        print FarClip  
        
    def Frust(self,fru):
        del Frustum[:]
        Frustum.append(fru)
        print Frustum     

    def RollingDuration(self,duration):
        del RollingShutterDuration[:]
        RollingShutterDuration.append(duration)
        print RollingShutterDuration
        
    def RollingShut(self,rolling):
        del RollingShutter[:]
        off=0;top=1;bottom=2;left=3;right=4
        RollingShutter.append(eval(rolling))
        print RollingShutter   
        
    def defaultControls(self,Ccontrols):
        del cameraControls[:]
        cameraControls.append('1')
        print cameraControls
        
    def AimControls(self,Ccontrols):
        del cameraControls[:]
        cameraControls.append('2')
        print cameraControls

    def UpControls(self,Ccontrols):        
        del cameraControls[:]
        cameraControls.append('3')
        print cameraControls

    def rig(self,rType):
        del rigSelection[:]
        rigSelection.append(rType)
        print rigSelection

class slider():

    def buildSlider(self,sliderWidth,sliderHeight,slideGroupName):
        self.slideGroupName=slideGroupName
        self.sliderWidth=sliderWidth
        self.sliderHeight=sliderHeight      
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

Sl=slider()
#Sl.buildSlider(sliderWidth,sliderHeight,slideGroupName)

class numericDisplay():
    def __init__(self,name,XX,YY,ZZ):
        self.name=name
        self.XX=XX
        self.YY=YY
        self.ZZ=ZZ
        mel.eval('evaluator -name dynamics -c "disablingNodes=legacy2016";')
        mel.eval('evaluator -name dynamics -c "handledNodes=none";')
        mel.eval('evaluator -name dynamics -c "action=none";')

        cmds.particle(p=(XX,YY,ZZ),c=1,n=name)
        cmds.setAttr(name+".particleRenderType", 2)
        cmds.addAttr(name+"Shape",longName=name+'Input')
        mel.eval('addAttr -is true -ln "pointSize" '+ name+'Shape;')
        mel.eval('addAttr -is true -ln "selectedOnly" -at bool -dv false '+ name+'Shape;')
        mel.eval('addAttr -is true -dt "string" -ln "attributeName" '+ name+'Shape;')
        mel.eval('setAttr -type "string" '+ name+'Shape.attributeName '+name+"Input;")
        cmds.setAttr(name+"Shape.template",1)

def trashAll(self):
    del current_Lenses[:]
    del current_prime[:]
    del current_zoom[:]
    del LensesNodes[:]
    del IrisNodes[:]
    del annotationNames[:]
    print current_Lenses
    print current_prime  
    print current_zoom 
    print LensesNodes
    print IrisNodes
    print annotationNames

def reset(self):
    trashAll('')
    CameraMaker()

def OnCamTools(cameraTools):
    del toolWindow[:]
    toolWindow.append('cameraTools')
    print toolWindow

def OffCamTools(cameraTools):
    del toolWindow[:]
    print toolWindow

def delivery(self):

    if len(current_Lenses)<1:
        LF.manufacturing('FZ_25-300mm/T3.5__')
        LF.manufacturing('PZ_190-590mm/T4.0__')
    if len(current_Lenses)==1:
        LF.manufacturing('FZ_25-300mm/T3.5__')
    for c in current_Lenses:
        typeCheck=c[1:2]
        if typeCheck == 'P':
            current_prime.append(c)
        
        if typeCheck == 'Z':
            current_zoom.append(c)
            
    print current_prime  
    print current_zoom  
    
    for x in range (len(current_prime)):
            
        lens=str(current_prime[x])            
        lensSplitP=re.split('/',lens)
        lensName=lens.replace('.', '_').replace('/', '_').replace('-', '_')+cycle
        focalLength=float(lensSplitP[0][3:-2])
        Fstop=(lensSplitP[1])[1:][:3]            
        TStopCheck=(lensSplitP[1])[:1]
        brand=lens[0:2]
        blades=eval(brand)["blades"]
        curvature=eval(brand)["curvature"]
        if TStopCheck =='T':
            Fstop=(float((lensSplitP[1])[1:][:3]))*0.9

        if TStopCheck =='F':
            Fstop=float((lensSplitP[1])[1:][:3])
                                     
        cmds.createNode('condition', n=lensName)
        cmds.setAttr(lensName+".colorIfTrueR", float(focalLength))
        cmds.setAttr(lensName+'.colorIfTrueG', float(focalLength))        
        cmds.setAttr(lensName+'.colorIfTrueB', Fstop)
        cmds.setAttr(lensName + ".ihi", 0)
        LensesNodes.append(lensName) 
        
        cmds.createNode('condition', n=lensName+'_'+str(blades)+'_')
        cmds.setAttr(lensName+'_'+str(blades)+'_'+".colorIfTrueR", blades)
        cmds.setAttr(lensName+'_'+str(blades)+'_'+".colorIfTrueG", curvature)
        cmds.setAttr(lensName+'_'+str(blades)+'_'+".colorIfTrueB", 22)
        cmds.setAttr(lensName+'_'+str(blades)+'_'+".ihi", 0)
        IrisNodes.append(lensName+'_'+str(blades)+'_')

        annotationNames.append(str(focalLength)+"mm")
           
    for x in range (len(current_zoom)):
                                              
        lens=str(current_zoom[x])
        brand=lens[0:2]
        lensSplitHalf=re.split('/',lens)
        lensSplitMM=re.split('-',lensSplitHalf[0])
        lensName=lens.replace('.', '_').replace('/', '_').replace('-', '_')+cycle    
        LensMin=float(lensSplitMM[0][3:])
        LensMax=float(lensSplitMM[1][:-2])
        Fstop=float(lensSplitHalf[1][1:-2])
        blades=eval(brand)["blades"]
        curvature=eval(brand)["curvature"]
            
        cmds.createNode('condition', n=lensName)
        cmds.setAttr(lensName+'.colorIfTrueR', LensMin)
        cmds.setAttr(lensName+'.colorIfTrueG', LensMax)
        cmds.setAttr(lensName+'.colorIfTrueB', Fstop)
        cmds.setAttr(lensName + ".ihi", 0)
        LensesNodes.append(lensName)   

        cmds.createNode('condition', n=lensName+'_'+str(blades)+'_')
        cmds.setAttr(lensName+'_'+str(blades)+'_'+".colorIfTrueR", blades)
        cmds.setAttr(lensName+'_'+str(blades)+'_'+".colorIfTrueG", curvature)
        cmds.setAttr(lensName+'_'+str(blades)+'_'+".colorIfTrueB", 22)
        cmds.setAttr(lensName+'_'+str(blades)+'_'+".ihi", 0)
        IrisNodes.append(lensName+'_'+str(blades)+'_') 

        annotationNames.append(str(LensMin)+"_"+str(LensMax)+"mm")
   
    if len(current_zoom)+len(current_prime)==len(current_Lenses):
        setConditions()
        ctrls()
        connect()

def setConditions():
    for x in range(len(LensesNodes)):
        cmds.setAttr(LensesNodes[x]+'.secondTerm', x)

    for x in range(len(IrisNodes)):
        cmds.setAttr(IrisNodes[x]+'.secondTerm', x)

def connect():
                    
    firstLens=LensesNodes[0]
    lastLens=LensesNodes[-1]
    print firstLens
    print lastLens
                
    cmds.connectAttr(lastLens+'.outColor', firstLens+'.colorIfFalse')
    cmds.connectAttr(lastLens+'.outColor.outColorR', zoom_SliderName+'Range.minX')
    cmds.connectAttr(lastLens+'.outColor.outColorG', zoom_SliderName+'Range.maxX')
    cmds.createNode('condition',n=zoom_SliderName+"visibility")
    cmds.connectAttr(zoom_SliderName+'Range.maxX', zoom_SliderName+"visibility.firstTerm")
    cmds.connectAttr(zoom_SliderName+'Range.minX', zoom_SliderName+"visibility.secondTerm")
    cmds.connectAttr(zoom_SliderName+"visibility.outColorR", zoom_SliderName+".visibility")
    cmds.connectAttr(lastLens+".outColorB", FStop_SliderName+"Range.minX")
    cmds.setAttr(FStop_SliderName+"Range.maxX",22)
    
    firstIris=IrisNodes[0]
    lastIris=IrisNodes[-1] 
    
    cmds.connectAttr(lastIris+'.outColor', firstIris+'.colorIfFalse')    
    
    for x in range (len(LensesNodes)):
        
        u=x+1              
        lensOutput=LensesNodes[x]    
        cmds.connectAttr(lens_SliderName+'Range.round', lensOutput+'.firstTerm')               

        lensInput=LensesNodes[u]              
        cmds.connectAttr(lensOutput+'.outColor', lensInput+'.colorIfFalse')

        if u == (len(LensesNodes)-1):

            cmds.connectAttr(lens_SliderName+'Range.round', LensesNodes[-1]+'.firstTerm') 
            for i in range (len(IrisNodes)):
                                
                lensOutput=IrisNodes[i]     
                cmds.connectAttr(lens_SliderName+'Range.round', lensOutput+'.firstTerm')             
                i+=1
                lensInput=IrisNodes[i]              
                cmds.connectAttr(lensOutput+'.outColor', lensInput+'.colorIfFalse')
                u=i+1
                if u == (len(IrisNodes)):
                    cmds.connectAttr(lens_SliderName+'Range.round', IrisNodes[-1]  +'.firstTerm') 

                    cameraFab()
                    trashAll('')
                    break
                
def annotation():
    lensesAmount=2.008/len(LensesNodes)
    cmds.group(n='anotations'+cameraName,em=True)
    cmds.group(n='ann'+cameraName,em=True)
    cmds.group(n='anotationsLoc'+cameraName,em=True)

    for x in range(len(annotationNames)):
        an=annotationNames[x]
        anName=an.replace('.', '_')+str(x)+'_'
        locatorName='As'+anName+cycle+LensesNodes[x]
        
        cmds.spaceLocator(n=locatorName)
        cmds.annotate(locatorName,tx=an, p=(0, 0, 0))
        cmds.rename("anno"+anName+cycle)
        cmds.parent("anno"+anName+cycle,locatorName)
        cmds.setAttr(locatorName+'.translateX',lensesAmount*(x) )
        cmds.setAttr("anno"+anName+cycle+'.translateY',-0.28 )
        cmds.setAttr("anno"+anName+"Shape"+cycle+".template",1)
        cmds.parent("anno"+anName+cycle,'ann'+cameraName)
        cmds.parent(locatorName,'anotationsLoc'+cameraName)
    
    cmds.hide('anotationsLoc'+cameraName)    
    cmds.parent('anotationsLoc'+cameraName,'ann'+cameraName,'anotations'+cameraName)
    cmds.setAttr('anotations'+cameraName+'.translateX',-0.961 )
    cmds.setAttr('anotations'+cameraName+'.translateY',1.593 )
    cmds.parent('anotations'+cameraName,'ann'+cameraName,'anotationsLoc'+cameraName,'MainCtrl'+cameraName)

def ctrls():
        
    Sl.buildSlider(1,0.08,lens_SliderName)
    cmds.setAttr(lens_SliderName+".tz",0.044)     
    cmds.setAttr(lens_SliderName+".rz",90)
    cmds.setAttr(lens_SliderName+".rx",90)
    cmds.setAttr(lens_SliderName+".ty",1.5)
    cmds.setAttr(lens_SliderName+'Range.maxX',len(LensesNodes)-1)
    cmds.addAttr(lens_SliderName+'Range',ln="round",at='long',dv=0)    
    cmds.connectAttr(lens_SliderName+'Range.outValueX', lens_SliderName+'Range.round')
    
    Sl.buildSlider(1,0.08,zoom_SliderName)
    cmds.setAttr(zoom_SliderName+".tz",0.044) 
    cmds.setAttr(zoom_SliderName+".rz",90)
    cmds.setAttr(zoom_SliderName+".rx",90)
    cmds.setAttr(zoom_SliderName+".ty",1.8)
    
    Sl.buildSlider(1,0.08,FStop_SliderName)
    cmds.setAttr(FStop_SliderName+".tz",0.044) 
    cmds.setAttr(FStop_SliderName+".rz",90)
    cmds.setAttr(FStop_SliderName+".rx",90)
    cmds.setAttr(FStop_SliderName+".ty",2.1)
    
    cmds.curve(d=1,p=[(1.044803,2.328214,0),(-0.961111,2.328214,0),(-0.961111,-0.955556,0) ,
    (1.044803,-0.955556,0),(1.044803,2.328214,0)], k=(0,1,2 ,3,4),n=cameraName+'Frame')
    cmds.setAttr(cameraName+'Frame.template', 1)
    cmds.group(cameraName+'Frame',FStop_SliderName,zoom_SliderName,lens_SliderName, n='MainCtrl'+cameraName)
    annotation()
    
def cameraFab():
    fw=eval(current_camera[0])[1]*0.0393701
    fh=eval(current_camera[0])[0]*0.0393701   
    cameraNodes=cmds.camera(n=currentCamName[0],hfa=float(fh),vfa=float(fw),sa=shutterAngle[0],mb=motionBlur[0])
    global cameraNodes
    cmds.setAttr(cameraNodes[1]+".aiShutterType", ShutterType[0])
    cmds.setAttr(cameraNodes[1]+".aiEnableDOF",depthOfField[0])
    cmds.setAttr(cameraNodes[1]+".displayCameraNearClip",NearClip[0])
    cmds.setAttr(cameraNodes[1]+".displayCameraFarClip",FarClip[0])
    cmds.setAttr(cameraNodes[1]+".displayCameraFrustum",Frustum[0])
    cmds.setAttr(cameraNodes[1]+".aiRollingShutter",RollingShutter[0])
    cmds.setAttr(cameraNodes[1]+".aiRollingShutterDuration", RollingShutterDuration[0])
    controlers()
    cmds.connectAttr(zoom_SliderName+'Range.outValueX', cameraNodes[1]+'.focalLength')
    cmds.connectAttr( IrisNodes[-1]+".outColorR", cameraNodes[1]+".aiApertureBlades")
    cmds.connectAttr(IrisNodes[-1]+".outColorG", cameraNodes[1]+".aiApertureBladeCurvature")
    cmds.parent('MainCtrl'+cameraName ,cameraNodes[0])   
    numericDisplay(zoom_SliderName+"Display",0,1.607,0)
    numericDisplay(FStop_SliderName+"Display",0,2.209,0)
    cmds.parent(FStop_SliderName+"Display",zoom_SliderName+"Display",'MainCtrl'+cameraName)
    cmds.connectAttr(cameraNodes[1]+".focalLength", zoom_SliderName+"DisplayShape."+zoom_SliderName+"DisplayInput")
    cmds.connectAttr(cameraNodes[1]+".fStop", FStop_SliderName+"DisplayShape."+FStop_SliderName+"DisplayInput")
    cmds.connectAttr(FStop_SliderName+"Range.outValueX",cameraNodes[1]+".fStop")
    cmds.select(clear=True)
    if 'FirstStep' in rigSelection:eval(rigSelection[0]+'()');eval(toolWindow[0]+'()');cmds.deleteUI(windowName)
    if 'SecondStep'in rigSelection:eval(rigSelection[0]+'()');eval(toolWindow[0]+'()');cmds.deleteUI(windowName)
    if 'not' in rigSelection:eval(toolWindow[0]+'()');cmds.deleteUI(windowName)

def torusCtrl(name):
    cmds.polyTorus(n=name+cycle,r=1.5,sr=0.02)
    cmds.setAttr(name+cycle+"Shape.primaryVisibility", 0)
    cmds.setAttr(name+cycle+"Shape.castsShadows", 0)
    cmds.setAttr(name+cycle+"Shape.aiVisibleInDiffuseReflection", 0)
    cmds.setAttr(name+cycle+"Shape.aiVisibleInSpecularReflection", 0)
    cmds.setAttr(name+cycle+"Shape.aiVisibleInDiffuseTransmission", 0)
    cmds.setAttr(name+cycle+"Shape.aiVisibleInSpecularTransmission", 0)
    cmds.setAttr(name+cycle+"Shape.aiVisibleInVolume",0)
    cmds.setAttr(name+cycle+"Shape.aiSelfShadows", 0)

def FirstStep():
    torusCtrl('springFirstStep')
    cmds.setAttr('springFirstStep'+cycle+'.translateZ',-5)
    cmds.constrain(s=True,st=5,d=0.1, p=(0, 0, -13),n='FirstStep'+cycle)
    cmds.parent(cameraNodes[0]+'_aim','springFirstStep'+cycle)
    cmds.setAttr("rigidSolver.ihi", 0)  
    cmds.setAttr("time1.ihi", 0)  
    cmds.circle(r=3,nr=(0,1,0),n='masterCtrl'+cycle)
    cmds.parent(cameraNodes[0]+'_group','springFirstStep'+cycle,'FirstStep'+cycle,'masterCtrl'+cycle)

def SecondStep():
    FirstStep()
    torusCtrl('springSecondStep')
    cmds.setAttr('springSecondStep'+cycle+'.translateZ',-13)
    cmds.constrain(s=True,st=5,d=0.1, p=(0, 0, -18),n='SecondStep'+cycle)
    cmds.parent('FirstStep'+cycle,'springSecondStep'+cycle)
    cmds.parent('springSecondStep'+cycle,'SecondStep'+cycle,'masterCtrl'+cycle)

def controlers():
    mel.eval('cameraMakeNode '+cameraControls[0]+'"";')
def newCam(self):
    mel.eval('lookThroughModelPanel '+cameraNodes[0]+' modelPanel4')
def persp(self):
    mel.eval('lookThroughModelPanel persp modelPanel4')
def toolProperty():
    cmds.toolPropertyWindow()
def tumbleCmd():
    cmds.setToolTo('tumbleContext') 
def trackCmd():
    cmds.setToolTo('trackContext')      
def dollyCmd():
    cmds.setToolTo('dollyContext')
def zoomCmd():
    cmds.setToolTo('boxZoomSuperContext')
def panZoomCmd():
    cmds.setToolTo('PanZoomContext')
def pencilCmd():
    cmds.setToolTo('greasePencilSuperContext')
def rollCmd():
    cmds.setToolTo('rollContext')
def azimuthCmd():
    cmds.setToolTo('azimuthElevationContext')  
def yawPitchCmd():
    cmds.setToolTo('yawPitchContext')
def flyCmd():
    cmds.setToolTo('flyThroughContext')
def walkCmd():
    cmds.setToolTo('walkContext')
def SuperContext():
    cmds.setToolTo('selectSuperContext') 

def cameraTools():
    camTools=windowName+"Tools"
    if (cmds.window(camTools,q=True,ex=True)):
        cmds.deleteUI(camTools)
    cmds.window(camTools,rtf=True,s=False)
    
    windowDivider=cmds.rowColumnLayout(nc=5)
    main=cmds.rowColumnLayout(nr=3,p=windowDivider)
    tools=cmds.rowColumnLayout(nc=3,p=main)
    
    buttonHeight=20
    buttonWidth=140
    toolsColumn=cmds.gridLayout(p=tools,nc=1,cwh=(buttonWidth,buttonHeight))
    cmds.iconTextButton(style='textOnly',l="Tumble Tool",bgc=[0.37,0.37,0.37],p=toolsColumn,c=tumbleCmd)
    cmds.iconTextButton(style='textOnly',l="Track Tool",bgc=[0.37,0.37,0.37],p=toolsColumn,c=trackCmd)
    cmds.iconTextButton(style='textOnly',l="Dolly Tool",bgc=[0.37,0.37,0.37],p=toolsColumn,c=dollyCmd)
    cmds.iconTextButton(style='textOnly',l="Zoom Tool",bgc=[0.37,0.37,0.37],p=toolsColumn,c=zoomCmd)
    cmds.iconTextButton(style='textOnly',l="2D Pan/Zoom Tool",bgc=[0.37,0.37,0.37],p=toolsColumn,c=panZoomCmd)
    cmds.iconTextButton(style='textOnly',l="Grease Pencil Tool",bgc=[0.37,0.37,0.37],p=toolsColumn,c=pencilCmd)
    cmds.iconTextButton(style='textOnly',l="Roll Tool",bgc=[0.37,0.37,0.37],p=toolsColumn,c=rollCmd)
    cmds.iconTextButton(style='textOnly',l="Azimuth Elevation Tool",bgc=[0.37,0.37,0.37],p=toolsColumn,c=azimuthCmd)
    cmds.iconTextButton(style='textOnly',l="Yaw-Pitch Tool",bgc=[0.37,0.37,0.37],p=toolsColumn,c=yawPitchCmd)
    cmds.iconTextButton(style='textOnly',l="Fly Tool",bgc=[0.37,0.37,0.37],p=toolsColumn,c=flyCmd)
    cmds.iconTextButton(style='textOnly',l="Walk Tool",bgc=[0.37,0.37,0.37],p=toolsColumn,c=walkCmd)
    
    cmds.rowColumnLayout(p=tools)
    icon='hollowBoxIcon.xpm'
    settingsColumn=cmds.gridLayout(p=tools,nc=1,cwh=(buttonWidth/10,buttonHeight))
    cmds.iconTextButton( style='iconAndTextVertical',bgc=[0.37,0.37,0.37], image1=icon,p=settingsColumn,c=("tumbleCmd(),toolProperty()"))
    cmds.iconTextButton( style='iconAndTextVertical',bgc=[0.37,0.37,0.37], image1=icon,p=settingsColumn,c=("trackCmd(),toolProperty()"))
    cmds.iconTextButton( style='iconAndTextVertical',bgc=[0.37,0.37,0.37], image1=icon,p=settingsColumn,c=("dollyCmd(),toolProperty()"))
    cmds.iconTextButton( style='iconAndTextVertical',bgc=[0.37,0.37,0.37], image1=icon,p=settingsColumn,c=("zoomCmd(),toolProperty()"))
    cmds.iconTextButton( style='iconAndTextVertical',bgc=[0.37,0.37,0.37], image1=icon,p=settingsColumn,c=("panZoomCmd(),toolProperty()"))
    cmds.iconTextButton( style='iconAndTextVertical',bgc=[0.37,0.37,0.37], image1=icon,p=settingsColumn,c=("pencilCmd(),toolProperty()"))
    cmds.iconTextButton( style='iconAndTextVertical',bgc=[0.37,0.37,0.37], image1=icon,p=settingsColumn,c=("rollCmd(),toolProperty()"))
    cmds.iconTextButton( style='iconAndTextVertical',bgc=[0.37,0.37,0.37], image1=icon,p=settingsColumn,c=("azimuthCmd(),toolProperty()"))
    cmds.iconTextButton( style='iconAndTextVertical',bgc=[0.37,0.37,0.37], image1=icon,p=settingsColumn,c=("yawPitchCmd(),toolProperty()"))
    cmds.iconTextButton( style='iconAndTextVertical',bgc=[0.37,0.37,0.37], image1=icon,p=settingsColumn,c=("flyCmd(),toolProperty()"))
    cmds.iconTextButton( style='iconAndTextVertical',bgc=[0.37,0.37,0.37], image1=icon,p=settingsColumn,c=("walkCmd(),toolProperty()") )
    
    cmds.rowColumnLayout(nc=1,p=main)
    cmds.separator(style='none',h=20) 
    cmds.iconTextButton( style='textOnly',bgc=[0.37,0.37,0.37],w=155,h=40,l='exit tool',c=SuperContext) 
    cmds.separator(style='none')   
    secondHalf=cmds.rowColumnLayout(nc=2,p=windowDivider)

    cmds.separator(p=secondHalf,h=40, style='none')
    cmds.text(l='change Camera',al='center')
    cmds.separator(p=secondHalf,h=5, style='none')
    chooseCamera=cmds.rowColumnLayout(nr=1,p=secondHalf)
    cmds.separator(p=chooseCamera,w=20, style='none')
    cmds.button(l="persp cam",c=persp,p=chooseCamera,w=150,h=50)
    cmds.button(l=cameraNodes[0],c=newCam,p=chooseCamera,w=150) 
    cmds.separator(p=secondHalf,h=40, style='none')   
    cmds.text(l='Controls',al='center',p=secondHalf)
    cmds.separator(p=secondHalf,h=5, style='none')
    cameraControlers=cmds.rowColumnLayout(nc=5,p=secondHalf)
         
    cmds.separator(p=cameraControlers,w=22, style='none')
    defaultCCtrl=cmds.button(l='default Camera',p=cameraControlers,c=('CameraFab.defaultControls(""),controlers()'),en=disableDefaultCamera[0])
    cmds.button(l='default and Aim',p=cameraControlers,c=('CameraFab.AimControls(""),controlers()')) 
    cmds.button(l='default and Aim and Up',p=cameraControlers,c=('CameraFab.UpControls(""),controlers()')) 
    cmds.separator(p=secondHalf,h=20, style='none')
    cameraSliders=cmds.rowColumnLayout(nr=7,p=secondHalf) 
   
    cmds.attrFieldSliderGrp( min=0, max=2,p=cameraSliders,pre=1,s=2, at=lens_SliderName+"Ctrl.translateZ",l='lenses')
    cmds.attrFieldSliderGrp( min=0, max=2,p=cameraSliders, at=FStop_SliderName+"Ctrl.translateZ",l='fStop',co2=(0,20) )
    cmds.attrFieldSliderGrp(min=0, max=2,p=cameraSliders, at=zoom_SliderName+"Ctrl.translateZ",l='zoom')
    cmds.rowColumnLayout(nc=1,p=secondHalf) 
    cameraSelection = cmds.selectionConnection( s=cameraNodes[1] )
    cmds.channelBox(mlc=cameraSelection,hol=False,st=True,fw=80,w=180,nn=True,p=windowDivider)

    if 'FirstStep' in rigSelection:
        firsStepSelection = cmds.selectionConnection( s='FirstStep'+cycle )
        cmds.channelBox(mlc=firsStepSelection,hol=False,st=True,fw=80,h=288,w=180,nn=True,p=windowDivider);cmds.showWindow()
    if 'SecondStep' in rigSelection:
        firsStepSelection = cmds.selectionConnection( s='FirstStep'+cycle )
        cmds.channelBox(mlc=firsStepSelection,hol=False,st=True,fw=80,h=288,w=180,nn=True,p=windowDivider)
        secondStepSelection = cmds.selectionConnection( s='SecondStep'+cycle )     
        cmds.channelBox(mlc=secondStepSelection,hol=False,st=True,fw=80,h=288,w=180,nn=True,p=windowDivider);cmds.showWindow()  
    if 'not' in rigSelection:cmds.showWindow()
    
LF=lensesFabrication('')
CameraFab=cameraFabrication('','','','','','','','','','','','','')
def disableRigs(f):cmds.disable(oneStepButton);cmds.disable(twoStepsButton)
def enableRigs(f):cmds.disable(oneStepButton, v=False );cmds.disable(twoStepsButton, v=False )

def disableDefault(s):del disableDefaultCamera[:];disableDefaultCamera.append(0)
def enableDefault(s):del disableDefaultCamera[:];disableDefaultCamera.append(1)
###########################################################Window
def CameraMaker():
    
    if (cmds.window(windowName,q=True,ex=True)):
        cmds.deleteUI(windowName)
    cmds.window(windowName,rtf=True,s=True)    
    main=cmds.rowColumnLayout( numberOfColumns=1)
    diagramming = cmds.rowColumnLayout( numberOfColumns=3, p=main,columnWidth=[(1, 300), (2, 430), (3, 80)])   
    
    ###############cameras tabs
    camerasTab = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5, p=diagramming)
    cameras=cmds.columnLayout(p=camerasTab)
    sensorsMatch=cmds.columnLayout(p=camerasTab)
    freeCamera=cmds.columnLayout(p=camerasTab, adj=True, rs=20)
    
    cmds.tabLayout( camerasTab,edit=True, tabLabel=((cameras, 'camera presets'), (sensorsMatch, 'sensors'), (freeCamera, 'free camera')) )
    ###################lenses tabs
    Ltabs=cmds.tabLayout(p=diagramming)
    ####prime lens
    primePresets=cmds.tabLayout('prime lens',p=Ltabs)

    arriPrime=cmds.columnLayout('arri',adj=True, rs=5,p=primePresets)
    cookePrime=cmds.columnLayout('cooke',adj=True, rs=5,p=primePresets)
    zeissPrime=cmds.columnLayout('zeiss',adj=True, rs=5,p=primePresets)
    canonPrime=cmds.columnLayout('canon',adj=True, rs=5,p=primePresets)
    schneiderPrime=cmds.columnLayout('schneider',adj=True, rs=5,p=primePresets)
    panavisionPrime=cmds.columnLayout('panavision',adj=True, rs=5,p=primePresets)
    
    ####zoom lens
    zoomPresets=cmds.tabLayout('zoom',p=Ltabs)
    arriZoom=cmds.columnLayout('arri',adj=True, rs=5,p=zoomPresets)
    zeissZoom=cmds.columnLayout('zeiss',adj=True, rs=5,p=zoomPresets)
    canonZoom=cmds.columnLayout('canon',adj=True, rs=5,p=zoomPresets)
    fujinonZoom=cmds.columnLayout('fujinon',adj=True, rs=5,p=zoomPresets)
    panavisionZoom=cmds.columnLayout('panavision',adj=True, rs=5,p=zoomPresets)
    
    ####free lens
    freeLenses=cmds.columnLayout('free lens' ,adj=True, rs=5,p=Ltabs)
    
    ########################################## rigs
    rigs=cmds.columnLayout(p=diagramming)
    
    ##########################################cameras
    cmds.columnLayout(p=cameras)
    cmds.scrollLayout(w=290,h=300)
    cmds.gridLayout(nc=2,cwh=(136,30))
    
    camPresets=cmds.iconTextRadioCollection('')
    for c in range (len(camerasCC)):
        cam=camerasCC[c]
        box=re.split('/',cam)
        [iconText]=box[:1]
        FabCom=("CameraFab.manufacturing('camera_%s')")%(cam)     
        cmds.iconTextRadioButton(st='textOnly',l=iconText,bgc=[0.37,0.37,0.37],fla=False,onc=FabCom) 

    cmds.scrollLayout(w=290,h=300,p=sensorsMatch)
    cmds.gridLayout(nc=2,cwh=(136,30))
    halfCamerasCC=[]
    for c in range (len(camerasCC)):
        cam=camerasCC[c]
        box=re.split('/',cam)
        [item]=box[1:]
        halfCamerasCC.append(item)  
    sensorList = list(dict.fromkeys(halfCamerasCC))
                        
    for c in range (len(sensorList)):
        sen=sensorList[c]
        print sen        
        FabCom=("CameraFab.manufacturing('camera/%s')")%(sen)  
        cmds.iconTextRadioButton(st='textOnly',l=sen,bgc=[0.37,0.37,0.37],fla=False,onc=FabCom) 
     
    cmds.separator(height=20, style='none', p=freeCamera)
    cmds.floatFieldGrp( numberOfFields=2,pre=3,p=freeCamera, label='Camera Aperture (mm)', extraLabel='mm', value1=36.000, value2=24.000, cc=CameraFab.custom)
    cmds.floatSliderGrp(l="shutter angle", pre=3, field=True , p=freeCamera, minValue=45, maxValue=270, value=144,cc=CameraFab.shutterAng)
    cmds.optionMenu( label='shutter type', p=freeCamera,cc=CameraFab.ShutterTy)
    cmds.menuItem( label='box')
    cmds.menuItem( label='triangle')
    cmds.menuItem( label='curve')
    
    ##########################################lenses buttons
    cmds.button(l='reset',p=rigs,h=18,w=80,c=reset)
    
    ########################prime lenses
    ######### arri prime
    cmds.gridLayout(nc=5,cwh=(80,30),p=arriPrime)

    for ap in range (len(arri_prime_lenses)):
        lensLength=arri_prime_lenses[ap]
        FabCom=("LF.manufacturing('AP_%s__')")%(lensLength)
        TrashCom=("LF.trash('AP_%s__')")%(lensLength)
        cmds.iconTextCheckBox( style='textOnly', label=lensLength,onc=FabCom, ofc=TrashCom, bgc=[0.37,0.37,0.37],fla=False)

    ######### cooke prime   
    cmds.gridLayout(nc=5,cwh=(80,30),p=cookePrime)
    
    for co in range (len(cooke_prime_lenses)): 
        lensLength=cooke_prime_lenses[co]
        FabCom=("LF.manufacturing('CP_%s__')")%(lensLength)
        TrashCom=("LF.trash('CP_%s__')")%(lensLength)
        cmds.iconTextCheckBox( style='textOnly', label=lensLength,onc=FabCom, ofc=TrashCom, bgc=[0.37,0.37,0.37],fla=False)
        
    ######### zeiss prime   
    cmds.gridLayout(nc=5,cwh=(80,30),p=zeissPrime)

    for ze in range (len(zeiss_prime_lenses)): 
        lensLength=zeiss_prime_lenses[ze]
        FabCom=("LF.manufacturing('ZP_%s__')")%(lensLength)
        TrashCom=("LF.trash('ZP_%s__')")%(lensLength)
        off=False

        cmds.iconTextCheckBox( style='textOnly', label=lensLength,onc=FabCom, ofc=TrashCom, bgc=[0.37,0.37,0.37],fla=False)

    ######### canon prime
    canonDivision=cmds.rowColumnLayout(numberOfRows=4,p=canonPrime)
    cmds.text("cinema",p=canonDivision)
    canonCinema=cmds.gridLayout(nc=5,cwh=(80,30),p=canonDivision)
    cmds.text("dslr",p=canonDivision)
    canonDslr=cmds.gridLayout(nc=5,cwh=(80,30),p=canonDivision)
    
    for ca in range (len(canon_primeCinema_lenses)): 
        lensLength=canon_primeCinema_lenses[ca]
        FabCom=("LF.manufacturing('CP_%s__')")%(lensLength)
        TrashCom=("LF.trash('CP_%s__')")%(lensLength)
        cmds.iconTextCheckBox( style='textOnly', label=lensLength,onc=FabCom, ofc=TrashCom, bgc=[0.37,0.37,0.37], p=canonCinema,fla=False)  
      
    for ca in range (len(canon_primeDslr_lenses)): 
        lensLength=canon_primeDslr_lenses[ca]
        FabCom=("LF.manufacturing('DP_%s__')")%(lensLength)
        TrashCom=("LF.trash('DP_%s__')")%(lensLength)
        cmds.iconTextCheckBox( style='textOnly', label=lensLength,onc=FabCom, ofc=TrashCom, bgc=[0.37,0.37,0.37], p=canonDslr,fla=False)   
        
        ######### schneider prime   
    cmds.gridLayout(nc=5,cwh=(80,30),p=schneiderPrime)
    
    for sc in range (len(schneider_prime_lenses)): 
        lensLength=schneider_prime_lenses[sc]
        FabCom=("LF.manufacturing('SP_%s__')")%(lensLength)
        TrashCom=("LF.trash('SP_%s__')")%(lensLength)
        cmds.iconTextCheckBox( style='textOnly', label=lensLength,onc=FabCom, ofc=TrashCom, bgc=[0.37,0.37,0.37],fla=False)
        
        ######### panavision prime   
    cmds.gridLayout(nc=5,cwh=(80,30),p=panavisionPrime)
    
    for pa in range (len(panavision_prime_lenses)): 
        lensLength=panavision_prime_lenses[pa]
        FabCom=("LF.manufacturing('PP_%s__')")%(lensLength)
        TrashCom=("LF.trash('PP_%s__')")%(lensLength)
        cmds.iconTextCheckBox( style='textOnly', label=lensLength,onc=FabCom, ofc=TrashCom, bgc=[0.37,0.37,0.37],fla=False)
        
        ########################zoom lenses
        ######### arri zoom 
    cmds.gridLayout(nc=4,cwh=(100,30),p=arriZoom)
    
    for az in range (len(arri_zoom_lenses)):
        lensLength=arri_zoom_lenses[az]
        FabCom=("LF.manufacturing('AZ_%s__')")%(lensLength)
        TrashCom=("LF.trash('AZ_%s__')")%(lensLength)
        cmds.iconTextCheckBox( style='textOnly', label=lensLength,onc=FabCom, ofc=TrashCom, bgc=[0.37,0.37,0.37],fla=False)
        
        ######### zeiss zoom 
    cmds.gridLayout(nc=5,cwh=(100,30),p=zeissZoom)
    
    for zz in range (len(zeiss_zoom_lenses)):
        lensLength=zeiss_zoom_lenses[zz]
        FabCom=("LF.manufacturing('ZZ_%s__')")%(lensLength)
        TrashCom=("LF.trash('ZZ_%s__')")%(lensLength)
        cmds.iconTextCheckBox( style='textOnly', label=lensLength,onc=FabCom, ofc=TrashCom, bgc=[0.37,0.37,0.37],fla=False)
         
        ######### canon zoom
    canonZDivision=cmds.rowColumnLayout(numberOfRows=4,p=canonZoom)
    cmds.text("cinema",p=canonZDivision)
    canonZCinema=cmds.gridLayout(nc=4,cwh=(100,30),p=canonZDivision)
    cmds.text("dslr",p=canonZDivision)
    canonZDslr=cmds.gridLayout(nc=4,cwh=(100,30),p=canonZDivision)

    for ca in range (len(canon_zoomCinema_lenses)): 
        lensLength=canon_zoomCinema_lenses[ca]
        FabCom=("LF.manufacturing('CZ_%s__')")%(lensLength)
        TrashCom=("LF.trash('CZ_%s__')")%(lensLength)
        cmds.iconTextCheckBox( style='textOnly', label=lensLength,onc=FabCom, ofc=TrashCom, bgc=[0.37,0.37,0.37], p=canonZCinema,fla=False)  
      
    for ca in range (len(canon_zoomDslr_lenses)): 
        lensLength=canon_zoomDslr_lenses[ca]
        FabCom=("LF.manufacturing('DZ_%s__')")%(lensLength)
        TrashCom=("LF.trash('DZ_%s__')")%(lensLength)
        cmds.iconTextCheckBox( style='textOnly', label=lensLength,onc=FabCom, ofc=TrashCom, bgc=[0.37,0.37,0.37], p=canonZDslr,fla=False)   
        
        ######### fujinon zoom 
    cmds.gridLayout(nc=4,cwh=(100,30),p=fujinonZoom)
    
    for fu in range (len(fujinon_zoom_lenses)):
        lensLength=fujinon_zoom_lenses[fu]
        FabCom=("LF.manufacturing('FZ_%s__')")%(lensLength)
        TrashCom=("LF.trash('FZ_%s__')")%(lensLength)
        cmds.iconTextCheckBox( style='textOnly', label=lensLength,onc=FabCom, ofc=TrashCom, bgc=[0.37,0.37,0.37],fla=False)
        ######### panavision zoom   
    cmds.gridLayout(nc=4,cwh=(100,30),p=panavisionZoom)
    
    for pz in range (len(panavision_zoom_lenses)):
        lensLength=panavision_zoom_lenses[pz]
        FabCom=("LF.manufacturing('PZ_%s__')")%(lensLength)
        TrashCom=("LF.trash('PZ_%s__')")%(lensLength)
        cmds.iconTextCheckBox( style='textOnly', label=lensLength,onc=FabCom, ofc=TrashCom, bgc=[0.37,0.37,0.37],fla=False)

        ######### free lens 
    cmds.separator(p=freeLenses,height=20, style='none')
    cmds.floatSliderGrp(l="min focal length",field=True, pre=1, p=freeLenses, maxValue=800, value=18,cc=LF.customMinLens)
    cmds.floatSliderGrp(l="max focal length",field=True, pre=1, p=freeLenses, maxValue=800, value=200,cc=LF.customMaxLens)
    cmds.floatSliderGrp(l="fStop",field=True, pre=2, p=freeLenses, maxValue=22, value=1.8,cc=LF.customFStop)
    cmds.intSliderGrp(l="aperture blades",field=True, p=freeLenses, minValue=3, maxValue=20, value=6,cc=LF.customBlades)
    cmds.floatSliderGrp(l="aperture blade curvature",field=True, pre=1, p=freeLenses, minValue=0, maxValue=1, value=0,cc=LF.customCurvature)
    cmds.button(l="delete lens", p=freeLenses,c=LF.delete)
    cmds.button(l="create lens", p=freeLenses,c=LF.create)
     ########################################## Rigs
    
    cmds.separator(p=rigs,h=20, style='none')
    cmds.gridLayout(nc=1,cwh=(80,50),p=rigs)
    cmds.iconTextRadioCollection( p=rigs)
    cmds.iconTextRadioButton(st='textOnly',l='default \nCamera',sl=True,bgc=[0.37,0.37,0.37],onc=disableRigs,ofc=enableRigs,fla=False,cc=CameraFab.defaultControls) 
    cmds.iconTextRadioButton(st='textOnly',l='Camera \nand Aim' ,bgc=[0.37,0.37,0.37],fla=False,cc=CameraFab.AimControls) 
    cmds.iconTextRadioButton(st='textOnly',l='Camera \nand Aim \nand Up',bgc=[0.37,0.37,0.37],fla=False,cc=CameraFab.UpControls)
    cmds.separator(p=rigs,h=20, style='none')

    cmds.gridLayout(nc=1,cwh=(80,30),p=rigs)
    cmds.iconTextRadioCollection()
    cmds.iconTextRadioButton(st='textOnly',l='no rig' ,bgc=[0.37,0.37,0.37],sl=True,fla=False,cc="CameraFab.rig('not')") 
    oneStepButton=cmds.iconTextRadioButton(st='textOnly',l='elastic rig\none step' ,bgc=[0.37,0.37,0.37],fla=False,onc=disableDefault,ofc=enableDefault,cc="CameraFab.rig('FirstStep')")
    twoStepsButton=cmds.iconTextRadioButton(st='textOnly',l='elastic rig\ntwo steps',bgc=[0.37,0.37,0.37],fla=False,onc=disableDefault,ofc=enableDefault,cc="CameraFab.rig('SecondStep')")   
    global twoStepsButton
    global oneStepButton
    bottom=cmds.rowColumnLayout(numberOfColumns=12, p=main)
    cmds.separator(p=bottom,w=20, style='none')
    cmds.checkBox( label='motion blur', v=0, p=bottom,cc=CameraFab.motionBlu)
    cmds.separator(p=bottom,w=50, style='none')
    cmds.checkBox( label='depth of field', v=0, p=bottom,cc=CameraFab.depthOfFie)
    cmds.separator(p=bottom,w=50, style='none')
    cmds.checkBox( label='display near clip', v=0, p=bottom,cc=CameraFab.NearC)
    cmds.separator(p=bottom,w=50, style='none')
    cmds.checkBox( label='display far clip', v=0, p=bottom,cc=CameraFab.FarC)
    cmds.separator(p=bottom,w=50, style='none')
    cmds.checkBox( label='display frustum', v=0, p=bottom,cc=CameraFab.Frust)
    cmds.separator(p=bottom,w=50, style='none')
    cmds.checkBox( label='camera tools', v=0, p=bottom,onc=OnCamTools,ofc=OffCamTools)
       
    bottom2=cmds.rowColumnLayout(numberOfColumns=7, p=main, cs=(50,50))
    cmds.separator(p=bottom2,w=100, style='none')
    cmds.optionMenu( label='rolling shutter', p=bottom2,cc=CameraFab.RollingShut)
    cmds.menuItem( label='off' )
    cmds.menuItem( label='top' )
    cmds.menuItem( label='bottom')
    cmds.menuItem( label='left')
    cmds.menuItem( label='right')
    cmds.floatSliderGrp(l="rolling shutter duration", pre=3,field=True , p=bottom2, minValue=0, maxValue=1, value=0,cc=CameraFab.RollingDuration)
    cmds.button(p=main, l="create camera", c=delivery)
    cmds.showWindow()   
   
CameraMaker()
disableRigs('') 
