import maya.cmds as cmds

circle1=cmds.ls(cmds.circle(nr=(1,0,0)),dag=1)
circle2=cmds.ls(cmds.circle(nr=(0,1,0)),dag=1)
circle3=cmds.ls(cmds.circle(nr=(0,0,1)),dag=1)
cmds.parent(circle3[1],circle2[1],circle1[0],r=True,s=True)
cmds.delete(circle3[0],circle2[0])
cmds.makeIdentity(circle1,apply=True, t=1,r=1,s=1,n=0,pn=1)
cmds.select(clear=True)
