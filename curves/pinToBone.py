import maya.cmds as cmds

#select the bones you want to add pin on and run the script

pointerList=[]
def pinMaker():
    
    del pointerList[:]
    ring=cmds.ls(cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=1 ,d=3, ut=0 , tol=0.01, s=8, ch=1),dag=1)
    pointer=cmds.ls(cmds.curve(n="pin" , d=3, p=[(0,0,1), (0, 0, 1.333333),(0, 0, 2), (0, 0, 3), (0, 0, 4,), (0, 0, 4.666667), ( 0, 0, 5)], k=[0, 0, 0, 1, 2, 3, 4, 4, 4]),dag=1) 
    cmds.parent(ring[1],pointer[1], pointer[0],r=True,s=True)
    cmds.delete(ring[0])
    cmds.move(0, 0, 5.031416, pointer[0]+".scalePivot", pointer[0]+".rotatePivot", absolute=True)
    cmds.makeIdentity(pointer,apply=True, t=1,r=1,s=1,n=0,pn=1)
    cmds.select(clear=True)
    pointerList.append(pointer[0])

bones=cmds.ls(sl=True)

for x in bones:

    pinMaker()
    print pointer 
    cmds.matchTransform(pointerList[0] , x)
