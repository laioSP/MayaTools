from maya import cmds

riggingConvention = [['CRV',	'A curve not used as a path, spline IK or control (usually just visual)'],
['CTRL', 'An animator control'],
['PATH', 'A curve used as a path'],
['IKCRV', 'A curve used in a spline IK system'],
['MANIP', 'A type of control that is never animated. Just used for visual settings'],
['JNT', 'The core skeleton ONLY'],
['RIGJNT', 'A utility joint used in rigs but NOT part of the base skeleton and NOT used as a skin influence.'],
['DEFJNT', 'A utility joint used in rigs that is a skin influence. (These are NOT in the core skeleton)'],
['PRXYJNT',	'A joint manipulated during skeleton editing only.'],
['GHOST', "A double joint used as a templated guide line between two objects or a joint showing the rig pose during skeleton editing. (It's unselectable and templated)"],
['GRP',	'logical grouping of nodes'],
['RGRP', 'A logical grouping of rig nodes'],
['BSGRP', 'A logical grouping of nodes used to distinguish blendshape grouping'],
['VISGRP', 'A geometry container signifying that meshes under it should show/hide together'],
['SPACE', 'A transform used to parent constrain to other nodes, providing controls with space switching capabilities.'],
['SNAP', 'A node used to snap/align two assets together (like props to hands, helmets to heads, etc.)'],
['LINK', "A transform used as the primary attachment for a rig to it's driver (core joint or another control)."],
['ZERO', 'A group used to zero the values of transforms below it and connect rigs in series.'],
['XFORM', 'A transform node used as an intermediate layer between controls and/or their zero nodes.'],
['PROXY', "A transform used as an intermediate object for connecting rigs to a chain which is itself driven by more than one rig. (Ex: A hand rig follows a PROXY which is influenced by both the arm's FK and IK rigs.)"],
['OFFSET', 'A transform used to counter movement of its children (usually for counteracting double transformations)'],
['UPVEC', 'A transform used as an up vector object for a constraint.'],
['HLP',	'A general use term for transforms used in rigs that have no other specific name/function'],
['PBSHAPE',	'A transform used as a proxy node driving multiple blend shape nodes at once'],
['DISPLAY',	'A non-renderable mesh used as a control, mark a position or convey information.'],
['LOC',	''],
['POS',	'A locator used for its position on a distance node'],
['SHRCTRL',	'A locator shape node shared via instancing to expose a common set of attributes under multiple controls'],
['ATTACH', 'Locator parented or constrained to another node to attach FX, lighting, etc. on shaded assets.'],
['FXLOC', 'Locator used specifically to attach FX rigs or FX components'],
['ATTACH', 'Muscle surface attach used to attach FX, lighting, etc. to a mesh surface on shaded assets.'],
['FOL',	'A follicle node'],
['IK', ''],
['EFF',	''],
['DRVKEY',	'An f-curve used as a driven key in a rig.'],
['PSI',	'A node used to interpolate between PSDs']]

ultilityConvention = [['MULT', 'multiplyDivide(Multiply mode)'],
['DIV', 'multiplyDivide(Divide mode)'],
['POW', 'multiplyDivide(Power mode)'],
['INV', 'multiplyDivide(Multiply x -1)'],
['ADD', 'addDoubleLinear'],
['MULT', 'multDoubleLinear'],
['VPDOT', 'vectorProduct(Dot product mode)'],
['VPCROSS', 'vectorProduct(Cross product mode)'],
['VPMATRIX', 'vectorProduct(Vector matrix mode)'],
['ADD', 'plusMinusAverage(Add mode)'],
['SUB', 'plusMinusAverage(Subtract mode)'],
['AVG', 'plusMinusAverage(Average mode)'],
['REV', 'reverse'],
['EXP', 'expression'],
['DIST', 'distanceBetween'],
['BCOLOR', 'blendColors'],
['BLENDW', 'blendWeighted'],
['COND', 'condition'],
['CLAMP', 'clamp'],
['CRVINFO', 'curveInfo'],
['RANGE', 'setRange'],
['REMAP', 'remapValue'],
['CHOICE', 'choice'],
['CHOOSE', 'chooser'],
['PLACE3D', 'place3dTexture'],
['PLACE2D', 'place2dTexture'],
['NUCLEUS', 'nucleus'],
['HAIRSYS', 'hairSystem']]

deformerConvention = [['SKIN', 'skinCluster | The descriptive name of this node will match the geometry or lattice name it is attached to.'],
['CLS', 'cluster'],
['CLSHAND', 'clusterHandle'],
['LTC', 'lattice | The deformed lattice shape used to deform the geo. All positional and descriptive elements of the lattice name should be the same except for one of these three suffixes for lattice and ffd.'],
['LTCBASE', 'baseLattice | The undeformed lattice used by the ffd node as a reference.'],
['LTCFFD', 'The ffd node that calculates the deformations using the above two lattices.'],
['WRA', 'wrap	 '],
['SWRAP', 'shrinkWrap'],	 
['BSHAPE', 'blendShape '],
['WIRE', 'wire'],
['SCULPT', 'sculpt'],
['BEND', 'deformBend'],
['FLARE', 'deformFlare'],
['SIN', 'deformSine'],
['SQUASH', 'deformSquash'],
['TWIST', 'deformTwist'],
['WAVE', 'deformWave'],
['SMOD', 'softMod'],
['SMODHAND', 'softModHandle'],
['DMUSH', 'deltaMush']]

constraintConvention = [['AIMCON', 'aimConstraint'],
['PNTCON', 'pointConstraint'],
['ORICON', 'orientConstraint'],
['SCLCON', 'scaleConstraint'],
['PARCON', 'parentConstraint'],
['PVCON', 'poleVectorConstraint'],
['TANCON', 'tangentConstraint'],
['NRMLCON', 'normalConstraint'],
['GEOCON', 'geometryConstraint'],
['POPCON', 'pointOnPolyConstraint']]

space = '_'

def reNamer():
    currentSelection = cmds.ls(sl=True)
    nameInput = cmds.textField(name,query=True,text=True)
    amountInput = cmds.intField(amount ,query=True, value=True)
    radioInput = cmds.iconTextRadioCollection(extenssion, query=True, sl=True)
    objType = cmds.iconTextRadioButton(radioInput, query=True, label=True)
    hierarchyInput = cmds.checkBox( hierarchy, query=True, value = True )
    counter=amountInput
    tempList = []
    extenssionList=[]
    tempCounter=1

    if objType == 'maintain extensions':
        for x in currentSelection:
            last=x.split('|')[-1]
            uniqueExtenssions=last.split('_')[-1]
            if uniqueExtenssions == last:
                extenssionList.append('')
            else:
                extenssionList.append(uniqueExtenssions)
            temporary=cmds.rename(last,'tempX87234nljsdfnkbjsd' + str(tempCounter))
            tempList.append(temporary)
            tempCounter += 1
    else:
        for x in currentSelection:    
            last=x.split('|')[-1]
            extenssionList.append(objType)
            temporary=cmds.rename(last,'tempX87234nljsdfnkbjsd' + str(tempCounter))
            tempList.append(temporary)
            tempCounter += 1 

    for x in range(len(tempList)):
        if counter == 0:
            newName = nameInput + space + extenssionList[x]  
        else:
            newName = nameInput + str(counter) + space + extenssionList[x]
        if hierarchyInput == True:
            cmds.reorder(tempList[x],b=1)
        cmds.rename(tempList[x],newName)
        counter += 1 

def disableUI():
    cmds.text(objectName, edit = True, enable = False)
    cmds.textField(name,edit = True, enable = False)
    cmds.text(countFrom, edit = True, enable = False)
    cmds.intField(amount ,edit = True, enable = False)
    
def enableUI():
    cmds.text(objectName, edit = True, enable = True)
    cmds.textField(name,edit = True,enable = True)
    cmds.text(countFrom, edit = True, enable = True)
    cmds.intField(amount ,edit = True, enable = True)
    
if (cmds.window('reNamer',q=True,ex=True)):
    cmds.deleteUI('reNamer')
cmds.window('reNamer',rtf = True,s=True)    
main = cmds.rowColumnLayout( nr=6 )
objectName = cmds.text('name of the object')
name = cmds.textField()

countLayout=cmds.rowColumnLayout( nc = 5, p = main )
cmds.separator(p=countLayout,w=50,style='none' )
countFrom = cmds.text('count from', p = countLayout, w = 100)
amount = cmds.intField(minValue = 0, p = countLayout, w = 30)
cmds.separator(p=countLayout,w=20,style='none' )
hierarchy = cmds.checkBox( label='order hierarchy', align='right', p = countLayout )

cmds.iconTextRadioCollection()
cmds.iconTextCheckBox( st='textOnly', l='switch extensions', w=120, bgc = [.4,.4,.4], onc = 'disableUI()', ofc = 'enableUI()' )


extenssion = cmds.iconTextRadioCollection()
cmds.iconTextRadioButton( st='textOnly', l='maintain extensions', w=120, sl=True, bgc = [.4,.4,.4] )

form = cmds.formLayout(p=main)
tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

rigTab = cmds.rowColumnLayout( numberOfColumns=6)
for rig in riggingConvention:    
    cmds.iconTextRadioButton( st='textOnly', l = rig[0], w=60, ann = rig[1], bgc = [.1,.8,.7] )
cmds.setParent( '..' )

ultilityTab = cmds.rowColumnLayout( numberOfColumns=6)   
for ultil in ultilityConvention:
    cmds.iconTextRadioButton( st='textOnly', l=ultil[0], ann=ultil[1], w=60, bgc = [.1,.6,.7] )
cmds.setParent( '..' )  

deformerTab = cmds.rowColumnLayout( numberOfColumns=6)
for deform in deformerConvention:
    cmds.iconTextRadioButton( st='textOnly', l=deform[0], ann=deform[1], w=60, bgc = [.1,.4,.7] )
cmds.setParent( '..' )  

constraintTab = cmds.rowColumnLayout( numberOfColumns=6)
for constraint in constraintConvention:
    cmds.iconTextRadioButton( st='textOnly', l=constraint[0], ann=constraint[1], w=60, bgc = [.3,.3,.7] )
cmds.setParent( '..' ) 

extenssion = cmds.iconTextRadioCollection(extenssion,edit=True)

cmds.tabLayout( tabs, edit = True, tabLabel = ((rigTab, 'rigging'), (ultilityTab, 'ultility'), (deformerTab, 'deformer'), (constraintTab, 'constraint')), bgc = [.3,.3,.3] )
finalLayout = cmds.rowColumnLayout( nr = 1, p = main )
cmds.separator(p=finalLayout,w=80,style='none' )
cmds.button(l = 'rename', p = finalLayout, c='reNamer()',w=200)

cmds.showWindow()
