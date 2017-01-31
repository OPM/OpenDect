from pyswarm import pso
from Tools.Coresimulation import WriteDATAfile

def Swarm(x,*hist):
    Lw = x[0]
    Ew = x[1] 
    Tw = x[2]
    Sorw = x[3]
    Krwmax = x[4]
    Low = x[5]
    Eow = x[6]
    Tow = x[7]
    Cw= x[8]
    Co= x[9]
    Aw= x[10]
    Ao= x[11]


    WriteDATAfile(nblocks,nblocks_z,Lw,Ew,Tw, Swir,Sorw,Krwmax,Low,Eow,Tow,Cw,Co,Aw,Ao)
    RunEclipse("CORE_TEST.DATA")
    summary = ecl.EclSum("CORE_TEST")
    
    FOPT=summary["FOPT"]
    FWPT=summary["FWPT"]
    BPR_IN=summary["BPR:"+str(int(float(nblocks)/2)+1)+","+str(int(float(nblocks)/2)+1)+","+str(nblocks_z)]
    BPR_OUT=summary["BPR:"+str(int(float(nblocks)/2)+1)+","+str(int(float(nblocks)/2)+1)+",1"]
    BPR_IN_init=BPR_IN.first.value
    BPR_OUT_init=BPR_OUT.first.value
    DELTA=[[],[],[]]
    TEST=[]

    for node1,node2,node3,node4,node5 in zip(FOPT,FWPT,BPR_IN,BPR_OUT,hist):
            hist_node=node5.split("\t")
            hist_oil=float(hist_node[0])+Epsilon
            hist_wat=float(hist_node[1])+Epsilon
            hist_diff=float(hist_node[2])+Epsilon
            DELTA[0]+=[((node1.value-hist_oil)/hist_oil)**2]
            DELTA[1]+=[((node2.value-hist_wat)/hist_wat)**2]
            DELTA[2]+=[(((abs(node3.value-node4.value)/abs(BPR_IN_init/BPR_OUT_init))-hist_diff)/hist_diff)**2]
    

    return np.sum(DELTA[1]+DELTA[2])
