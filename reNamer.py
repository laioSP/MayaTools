from maya import cmds

space = '_'

riggingConvention = ['CTRL', 'GRP', 'CRV', 'PATH', 'IKCRV', 'MANIP', 'JNT', 'RIGJNT', 'DEFJNT', 'PRXYJNT', 'GHOST', 'GRP', 'RGRP', 
'BSGRP', 'VISGRP', 'SPACE', 'SNAP', 'LINK', 'ZERO', 'XFORM', 'PROXY', 'OFFSET', 'UPVEC', 'HLP', 'PBSHAPE', 'DISPLAY', 'LOC', 
'POS', 'SHRCTRL', 'ATTACH', 'FOL', 'IK', 'EFF', 'DRVKEY', 'PSI']

ultilityConvention = [ 'MULT', 'DIV', 'POW', 'INV', 'ADD', 'MULT', 'VPDOT', 'VPDOT', 'VPCROSS', 'VPMATRIX', 'ADD', 'SUB' 'AVG', 'REV',
'EXP', 'DIST', 'BCOLOR', 'BLENDW', 'COND', 'CLAMP', 'CRVINFO', 'RANGE', 'REMAP', 'CHOICE', 'CHOOSE', 'PLACE3D', 'PLACE2D', 'NUCLEUS',
'HAIRSYS']

deformerConvention = ['SKIN', 'CLS', 'CLSHAND', 'LTC', 'LTCBASE', 'LTCFFD', 'WRAP', 'SWRAP', 'BSHAPE', 'WIRE', 'SCULPT', 'BLEND',
'FLARE', 'SIN', 'SQUASH', 'TWIST', 'WAVE', 'SMOD', 'SMODHAND', 'DMUSH']

constraintConvention = ['AIMCON', 'PNTCON', 'ORICON', 'SCLCON', 'PARCON', 'PVCON', 'TANCON', 'NRMLCON', 'GEOCON', 'POPCON']
currentSelection = cmds.ls(sl=True)

def reNamer(nameInput,amountInput,endInput):
    
    name = cmds.textField(nameInput,query=True,text=True)
    amount = cmds.intField(amountInput ,query=True, value=True)
    radioCol = cmds.iconTextRadioCollection(endInput, query=True, sl=True)
    objType = cmds.iconTextRadioButton(radioCol, query=True, label=True)

    counter=int(amount)
    tempList = []
    tempCounter=1
    for x in currentSelection:
        last=x.split('|')[-1]    
        cmds.reorder(last,b=1)
        print last
        
        temporary=cmds.rename(last,'tempX87234nljsdfnkbjsd' + str(tempCounter))
        tempList.append(temporary)
        tempCounter += 1 
    print tempList 
    del currentSelection[:] 
    for x in tempList:
        newName = name + str(counter) + space + objType  
        cmds.rename(x,newName)
        currentSelection.append(newName)
        counter += 1 
    

    
windowName='reNamer'

if (cmds.window(windowName,q=True,ex=True)):
    cmds.deleteUI(windowName)
cmds.window(windowName,rtf=True,s=True)    
main=cmds.rowColumnLayout( nr=6 )
cmds.text('name of the object')
name = cmds.textField()

countLayout=cmds.rowColumnLayout( nc = 3, p = main )
cmds.separator(p=countLayout,w=100,style='none' )
cmds.text('count from', p = countLayout, w = 100)
amount = cmds.intField(minValue = 1, p = countLayout, w = 30)

form = cmds.formLayout(p=main)
tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
extenssion = cmds.iconTextRadioCollection()

rigTab = cmds.rowColumnLayout( numberOfColumns=6)
for rig in riggingConvention:    
    cmds.iconTextRadioButton( st='textOnly', l=rig, w=60 )
cmds.setParent( '..' )

ultilityTab = cmds.rowColumnLayout( numberOfColumns=6)   
for ultil in ultilityConvention:
    cmds.iconTextRadioButton( st='textOnly', l=ultil, w=60 )
cmds.setParent( '..' )  

deformerTab = cmds.rowColumnLayout( numberOfColumns=6)
for deform in deformerConvention:
    cmds.iconTextRadioButton( st='textOnly', l=deform, w=60 )
cmds.setParent( '..' )  

constraintTab = cmds.rowColumnLayout( numberOfColumns=6)
for constraint in constraintConvention:
    cmds.iconTextRadioButton( st='textOnly', l=constraint, w=60 )
cmds.setParent( '..' ) 

extenssion = cmds.iconTextRadioCollection(extenssion,edit=True)

cmds.tabLayout( tabs, edit = True, tabLabel = ((rigTab, 'rigging'), (ultilityTab, 'ultility'), (deformerTab, 'deformer'), (constraintTab, 'constraint')) )

finalLayout=cmds.rowColumnLayout( nc = 1, p = main )
cmds.button(l = 'rename', p = finalLayout, c='reNamer(name,amount,extenssion)')

cmds.showWindow()
