import maya.cmds as cmds

def LFW(self):
     
    cmds.spaceLocator(n="Left_Front_Wheel")

def RFW(self):

    cmds.spaceLocator(n="Right_Front_Wheel")

def LFW_GRP(self):
    
    LFW_Selection=cmds.ls(selection=True)
    cmds.parent(LFW_Selection, "Left_Front_Wheel")

def LBW_GRP(self):

    LBW_Selection=cmds.ls(selection=True)
    cmds.group(LBW_Selection, n="Left_Back_Wheel")

def RBW_GRP(self):

    RBW_Selection=cmds.ls(selection=True)
    cmds.group(RBW_Selection, n="Right_Back_Wheel")

def RFW_GRP(self):

    RFW_Selection=cmds.ls(selection=True)
    cmds.parent(RFW_Selection, "Right_Front_Wheel")

def CTRLs(self):

    YValue=cmds.getAttr('Left_Front_Wheel.translateY')
    ZValue= cmds.getAttr('Left_Front_Wheel.translateZ')
    cmds.makeIdentity("Left_Front_Wheel", "Left_Back_Wheel", "Right_Back_Wheel", "Right_Front_Wheel", apply=True, t=1, r=1, s=1, n=0)
    cmds.group("Right_Front_Wheel", "Right_Back_Wheel", "Left_Back_Wheel", "Left_Front_Wheel", n="WheelGRP")
    cmds.select(all=True)
    cmds.group(n="Geo")


    cubeCtrl = cmds.curve(n="Front_Wheels_Direction", degree=1,point=[(-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (-0.5, -0.5, 0.5), 
                        (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5),
                        (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5),
                        (-0.5, 0.5, -0.5)],
                        k=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0])
    cmds.move(0, 0, ZValue)
    cmds.setAttr('Front_Wheels_Direction.translateY', 1.631)
    cmds.setAttr('Front_Wheels_Direction.scaleX', 11.447)
    cmds.setAttr('Front_Wheels_Direction.scaleY', 4.200)
    cmds.makeIdentity('Front_Wheels_Direction', apply=True, t=1, r=1, s=1, n=0)

    cubeCtrl = cmds.curve(n="LFWctrl", degree=1,point=[(-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (-0.5, -0.5, 0.5), 
                        (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5),
                        (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5),
                        (-0.5, 0.5, -0.5)],
                        k=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0])
    cmds.matchTransform("LFWctrl", "Left_Front_Wheel")
    cmds.move(5,0,0,r=True)
    cmds.setAttr('LFWctrl.scaleX', 0.5)
    cmds.setAttr('LFWctrl.scaleY', 2)
    cmds.setAttr('LFWctrl.scaleZ', 2)

    cubeCtrl = cmds.curve(n="LBWctrl", degree=1,point=[(-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (-0.5, -0.5, 0.5), 
                        (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5),
                        (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5),
                        (-0.5, 0.5, -0.5)],
                        k=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0])
    cmds.matchTransform("LBWctrl", "Left_Back_Wheel")
    cmds.move(5,0,0,r=True)
    cmds.setAttr('LBWctrl.scaleX', 0.5)
    cmds.setAttr('LBWctrl.scaleY', 2)
    cmds.setAttr('LBWctrl.scaleZ', 2)

    cubeCtrl = cmds.curve(n="RFWctrl", degree=1,point=[(-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (-0.5, -0.5, 0.5), 
                        (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5),
                        (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5),
                        (-0.5, 0.5, -0.5)],
                        k=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0])
    cmds.matchTransform("RFWctrl", "Right_Front_Wheel")
    cmds.move(-5,0,0,r=True)
    cmds.setAttr('RFWctrl.scaleX', 0.5)
    cmds.setAttr('RFWctrl.scaleY', 2)
    cmds.setAttr('RFWctrl.scaleZ', 2)

    cubeCtrl = cmds.curve(n="RBWctrl", degree=1,point=[(-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (-0.5, -0.5, 0.5), 
                        (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5),
                        (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5),
                        (-0.5, 0.5, -0.5)],
                        k=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0])
    cmds.matchTransform("RBWctrl", "Right_Back_Wheel")
    cmds.move(-5,0,0,r=True)
    cmds.setAttr('RBWctrl.scaleX', 0.5)
    cmds.setAttr('RBWctrl.scaleY', 2)
    cmds.setAttr('RBWctrl.scaleZ', 2)


    cmds.circle(r=15, nry=90, n="Main_Suspension") 
    cmds.move(0,YValue,0,r=True)

    cmds.select("LFWctrl", "LBWctrl", "RFWctrl", "RBWctrl","Main_Suspension")
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

    #Car direction
    cmds.group(em=True,n="TranslateGRP")
    cmds.setAttr('TranslateGRP.hiddenInOutliner',True)
    

    # 1 Quad
    cmds.createNode('plusMinusAverage', n="Average_1_Quad")
    cmds.setAttr('Average_1_Quad.operation', 3)
    cmds.connectAttr('TranslateGRP.translateX', 'Average_1_Quad.input1D[0]')
    cmds.connectAttr('TranslateGRP.translateZ', 'Average_1_Quad.input1D[1]')

    # 2 Quad
    cmds.createNode('plusMinusAverage', n="Average_2_Quad")
    cmds.setAttr('Average_2_Quad.operation', 3)
    cmds.createNode('multiplyDivide', n="multiply_2_Quad")
    cmds.setAttr("multiply_2_Quad.input2Z", -1)
    cmds.connectAttr('TranslateGRP.translateZ', 'multiply_2_Quad.input1.input1Z.')
    cmds.connectAttr('TranslateGRP.translateX', 'Average_2_Quad.input1D[0]')
    cmds.connectAttr('multiply_2_Quad.output.outputZ', 'Average_2_Quad.input1D[1]')

    # 3 Quad
    cmds.createNode('plusMinusAverage', n="Average_3_Quad")
    cmds.setAttr('Average_3_Quad.operation', 3)
    cmds.createNode('multiplyDivide', n="multiply_3_Quad")
    cmds.setAttr("multiply_3_Quad.input2Z", -1)
    cmds.setAttr("multiply_3_Quad.input2X", -1)
    cmds.connectAttr('TranslateGRP.translateZ', 'multiply_3_Quad.input1.input1Z.')
    cmds.connectAttr('TranslateGRP.translateX', 'multiply_3_Quad.input1.input1X.')
    cmds.connectAttr('multiply_3_Quad.output.outputZ', 'Average_3_Quad.input1D[0]')
    cmds.connectAttr('multiply_3_Quad.output.outputZ', 'Average_3_Quad.input1D[1]')

    # 4 Quad
    cmds.createNode('plusMinusAverage', n="Average_4_Quad")
    cmds.setAttr('Average_4_Quad.operation', 3)
    cmds.createNode('multiplyDivide', n="multiply_4_Quad")
    cmds.setAttr("multiply_4_Quad.input2X", -1)
    cmds.connectAttr('TranslateGRP.translateZ', 'Average_4_Quad.input1D[0]')
    cmds.connectAttr('TranslateGRP.translateX', 'multiply_4_Quad.input1.input1X.')
    cmds.connectAttr('multiply_4_Quad.output.outputX', 'Average_4_Quad.input1D[1]')

    #Rotation perncentage
    cmds.createNode('multiplyDivide',n="Divide360")
    cmds.setAttr("Divide360.operation", 2)
    cmds.setAttr("Divide360.input2Y", 360)
    cmds.connectAttr('TranslateGRP.rotate.rotateY', 'Divide360.input1.input1Y.')

    cmds.createNode('plusMinusAverage', n="SliceRotation")
    cmds.addAttr(ln="RoundUP", attributeType='long') 
    cmds.setAttr("SliceRotation.operation", 2)
    cmds.connectAttr('SliceRotation.RoundUP', 'SliceRotation.input1D[1]')

    cmds.connectAttr('Divide360.output.outputY', 'SliceRotation.RoundUP')
    cmds.connectAttr('Divide360.output.outputY', 'SliceRotation.input1D[0]')

    # Conditions
    #        1 and 2
    cmds.createNode('condition', n="condition_between_1_2_")
    cmds.setAttr("condition_between_1_2_.operation", 3)
    cmds.setAttr("condition_between_1_2_.secondTerm", 0.25)
    cmds.connectAttr('Average_1_Quad.output1D', 'condition_between_1_2_.colorIfFalse.colorIfFalseR')
    cmds.connectAttr('Average_2_Quad.output1D', 'condition_between_1_2_.colorIfTrue.colorIfTrueR')
    cmds.connectAttr('SliceRotation.output1D', 'condition_between_1_2_.firstTerm')

    #        3 and 4
    cmds.createNode('condition', n="condition_between_3_4_")
    cmds.setAttr("condition_between_3_4_.operation", 3)
    cmds.setAttr("condition_between_3_4_.secondTerm", -0.25)
    cmds.connectAttr('Average_3_Quad.output1D', 'condition_between_3_4_.colorIfFalse.colorIfFalseR')
    cmds.connectAttr('Average_4_Quad.output1D', 'condition_between_3_4_.colorIfTrue.colorIfTrueR')
    cmds.connectAttr('condition_between_1_2_.firstTerm', 'condition_between_3_4_.firstTerm')

    #        + and -
    cmds.createNode('condition', n="condition_Positive_Negative")
    cmds.setAttr("condition_Positive_Negative.operation", 4)
    cmds.connectAttr('condition_between_3_4_.outColor.outColorR', 'condition_Positive_Negative.colorIfTrue.colorIfTrueR') 
    cmds.connectAttr('condition_between_1_2_.outColor.outColorR', 'condition_Positive_Negative.colorIfFalse.colorIfFalseR')
    cmds.connectAttr('condition_between_3_4_.firstTerm', 'condition_Positive_Negative.firstTerm')


    #   connecting to CTRLs
       
    cmds.createNode('plusMinusAverage', n="Plus_LFW")
    cmds.createNode('plusMinusAverage', n="Plus_LBW")
    cmds.createNode('plusMinusAverage', n="Plus_RBW")
    cmds.createNode('plusMinusAverage', n="Plus_RFW")

    #         Left Front Wheel

    cmds.createNode('unitConversion',n="LFW1_Convert")
    cmds.setAttr("LFW1_Convert.conversionFactor", 1)
    cmds.createNode('unitConversion',n="LFW2_Convert")
    cmds.setAttr("LFW2_Convert.conversionFactor", 1)
    cmds.createNode('unitConversion',n="LFW3_Convert")
    cmds.setAttr("LFW3_Convert.conversionFactor", 1)

    cmds.connectAttr('LFWctrl.rotateX', 'LFW1_Convert.input')
    cmds.connectAttr('LFW1_Convert.output', 'Plus_LFW.input1D[1]')
    cmds.connectAttr('condition_Positive_Negative.outColor.outColorR', 'LFW2_Convert.input')
    cmds.connectAttr('LFW2_Convert.output', 'Plus_LFW.input1D[0]')
    cmds.connectAttr('Plus_LFW.output1D', 'LFW3_Convert.input')
    cmds.connectAttr('LFW3_Convert.output', 'Left_Front_Wheel.rotateX')

    #         Left Back Wheel

    cmds.createNode('unitConversion',n="LBW1_Convert")
    cmds.setAttr("LBW1_Convert.conversionFactor", 1)
    cmds.createNode('unitConversion',n="LBW2_Convert")
    cmds.setAttr("LBW2_Convert.conversionFactor", 1)
    cmds.createNode('unitConversion',n="LBW3_Convert")
    cmds.setAttr("LBW3_Convert.conversionFactor", 1)

    cmds.connectAttr('LBWctrl.rotateX', 'LBW1_Convert.input')
    cmds.connectAttr('LBW1_Convert.output', 'Plus_LBW.input1D[1]')
    cmds.connectAttr('condition_Positive_Negative.outColor.outColorR', 'LBW2_Convert.input')
    cmds.connectAttr('LBW2_Convert.output', 'Plus_LBW.input1D[0]')
    cmds.connectAttr('Plus_LBW.output1D', 'LBW3_Convert.input')
    cmds.connectAttr('LBW3_Convert.output', 'Left_Back_Wheel.rotateX')

    #           Right Back Wheel

    cmds.createNode('unitConversion',n="RBW1_Convert")
    cmds.setAttr("RBW1_Convert.conversionFactor", 1)
    cmds.createNode('unitConversion',n="RBW2_Convert")
    cmds.setAttr("RBW2_Convert.conversionFactor", 1)
    cmds.createNode('unitConversion',n="RBW3_Convert")
    cmds.setAttr("RBW3_Convert.conversionFactor", 1)

    cmds.connectAttr('RBWctrl.rotateX', 'RBW1_Convert.input')
    cmds.connectAttr('RBW1_Convert.output', 'Plus_RBW.input1D[1]')
    cmds.connectAttr('condition_Positive_Negative.outColor.outColorR', 'RBW2_Convert.input')
    cmds.connectAttr('RBW2_Convert.output', 'Plus_RBW.input1D[0]')
    cmds.connectAttr('Plus_RBW.output1D', 'RBW3_Convert.input')
    cmds.connectAttr('RBW3_Convert.output', 'Right_Back_Wheel.rotateX')

    #           Right Front Wheel

    cmds.createNode('unitConversion',n="RFW1_Convert")
    cmds.setAttr("RFW1_Convert.conversionFactor", 1)
    cmds.createNode('unitConversion',n="RFW2_Convert")
    cmds.setAttr("RFW2_Convert.conversionFactor", 1)
    cmds.createNode('unitConversion',n="RFW3_Convert")
    cmds.setAttr("RFW3_Convert.conversionFactor", 1)

    cmds.connectAttr('RFWctrl.rotateX', 'RFW1_Convert.input')
    cmds.connectAttr('RFW1_Convert.output', 'Plus_RFW.input1D[1]')
    cmds.connectAttr('condition_Positive_Negative.outColor.outColorR', 'RFW2_Convert.input')
    cmds.connectAttr('RFW2_Convert.output', 'Plus_RFW.input1D[0]')
    cmds.connectAttr('Plus_RFW.output1D', 'RFW3_Convert.input')
    cmds.connectAttr('RFW3_Convert.output', 'Right_Front_Wheel.rotateX')

    #   suspension
    
    cmds.createNode('plusMinusAverage',n="RFW_Trans_Convert")
    cmds.connectAttr('RFW_Trans_Convert.output3D', 'Right_Front_Wheel.translate')
    cmds.connectAttr('RFWctrl.translate','RFW_Trans_Convert.input3D[0]')
    cmds.connectAttr('Main_Suspension.translate','RFW_Trans_Convert.input3D[1]')

    cmds.createNode('plusMinusAverage',n="RBW_Trans_Convert")
    cmds.connectAttr('RBW_Trans_Convert.output3D', 'Right_Back_Wheel.translate')
    cmds.connectAttr('RBWctrl.translate','RBW_Trans_Convert.input3D[0]')
    cmds.connectAttr('Main_Suspension.translate','RBW_Trans_Convert.input3D[1]')

    cmds.createNode('plusMinusAverage',n="LBW_Trans_Convert")
    cmds.connectAttr('LBW_Trans_Convert.output3D', 'Left_Back_Wheel.translate')
    cmds.connectAttr('LBWctrl.translate','LBW_Trans_Convert.input3D[0]')
    cmds.connectAttr('Main_Suspension.translate','LBW_Trans_Convert.input3D[1]')

    cmds.createNode('plusMinusAverage',n="LFW_Trans_Convert")
    cmds.connectAttr('LFW_Trans_Convert.output3D', 'Left_Front_Wheel.translate')
    cmds.connectAttr('LFWctrl.translate','LFW_Trans_Convert.input3D[0]')
    cmds.connectAttr('Main_Suspension.translate','LFW_Trans_Convert.input3D[1]')

    #     Main CTRLs

    cmds.createNode('unitConversion',n="RFW1_Convert")
    cmds.setAttr("RFW1_Convert.conversionFactor", 1)
    cmds.createNode('unitConversion',n="RFW2_Convert")
    cmds.setAttr("RFW2_Convert.conversionFactor", 1)
    cmds.createNode('unitConversion',n="RFW3_Convert")
    cmds.setAttr("RFW3_Convert.conversionFactor", 1) 

    cmds.parent("LFWctrl", "LBWctrl", "RFWctrl", "RBWctrl","Main_Suspension") 
    cmds.circle(r=20, nry=90, n="Main_CTRL")
    cmds.parent("Main_Suspension","Front_Wheels_Direction", "Main_CTRL")
    cmds.connectAttr('Main_CTRL.translateX', 'TranslateGRP.translateX')
    cmds.connectAttr('Main_CTRL.translateZ', 'TranslateGRP.translateZ')
    cmds.connectAttr('Main_CTRL.translate', 'Geo.translate')
    cmds.connectAttr('Main_CTRL.rotate', 'Geo.rotate')
    cmds.connectAttr('Main_CTRL.rotateY', 'TranslateGRP.rotateY')

    #   FrontWheels

    cmds.createNode('unitConversion',n="FrontWheels_Convert")
    cmds.createNode('reverse',n="FrontWheels_Left_Reverse")
    cmds.setAttr("FrontWheels_Convert.conversionFactor", 1)
    cmds.connectAttr('Front_Wheels_Direction.rotateY', 'Right_Front_Wheel.rotateY')
    cmds.connectAttr('Front_Wheels_Direction.rotateY', 'Left_Front_Wheel.rotateY')
    cmds.connectAttr('Front_Wheels_Direction.rotateY', 'FrontWheels_Convert.input')
    cmds.connectAttr('FrontWheels_Convert.input',  'FrontWheels_Left_Reverse.inputY')
    cmds.connectAttr('FrontWheels_Left_Reverse.outputY',  'Plus_LFW.input1D[2]')
    cmds.connectAttr('FrontWheels_Convert.output',  'Plus_RFW.input1D[2]')


    cmds.delete("direction")

def eraseRig(self):


    cmds.parent( 'WheelGRP', r=True,w=True)
    cmds.select(all=True)
    cmds.select( 'WheelGRP', tgl=True )
    cmds.delete()
    cmds.ungroup( 'WheelGRP')
    cmds.ungroup( 'Left_Back_Wheel')
    cmds.ungroup( 'Right_Back_Wheel')
    cmds.ungroup( 'Right_Front_Wheel')
    cmds.ungroup( 'Left_Front_Wheel')
    cmds.select('Right_Front_Wheel', 'Left_Front_Wheel')
    cmds.delete()


cmds.curve(n="direction", degree=1, point=[(-2, 0, 10), (2, 0, 10), (2, 0, -7), (4, 0, -7), (0, 0, -12), (-4, 0, -7), (-2, 0, -7), (-2, 0, 10)], k=[0, 1 ,2, 3, 4, 5, 6, 7])
cmds.setAttr('direction.rotateY',180)
cmds.makeIdentity("direction", apply=True, t=1, r=1, s=1, n=0)



if cmds.window("Car Autorigger", query=True, exists=True):
    cmds.deleteUI("Car Autorigger")


cmds.window( rtf=True, t="Car Autorigger", s=False)
form = cmds.formLayout()
tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )

Wheels = cmds.columnLayout( rowSpacing=10, columnWidth=250, columnAttach=('both', 5))

cmds.separator(h=10)
cmds.text(l="Vehicle should have the same")
cmds.text(l="direction of the arrow")
cmds.separator(h=10)
cmds.text(l="Create and position one locator on each wheel")
cmds.separator(h=10)
cmds.button( label='Left Front Wheel Locator', command=LFW)
cmds.button( label='Right Front Wheel Locator', command=RFW)
cmds.separator(h=10)
cmds.text(l="Select the geometry of each wheel and ")
cmds.text(l="click the buttons bellow")
cmds.separator(h=10)
cmds.button( label='Left Front Wheel Group', command=LFW_GRP)
cmds.button( label='Right Front Wheel Group', command=RFW_GRP)
cmds.button( label='Left Back Wheel Group', command=LBW_GRP)
cmds.button( label='Right Back Wheel Group', command=RBW_GRP)
cmds.separator(h=10)
cmds.button( label='Create Controlers',h=50, command=CTRLs)
cmds.separator(h=10)
cmds.button(l="Delete Rig", c=eraseRig)

cmds.setParent( '..' )


cmds.tabLayout( tabs, edit=True, tabLabel=((Wheels, 'Wheels')) )

cmds.showWindow()
