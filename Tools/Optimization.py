from Tools.Coresimulation import WriteDATAfile
import numpy as np
import random

def Swarm(hist,imax,n,pmin,pmax,treshold):
    
    #Get parameters from inputs
    ndim=len(pmax)

    #Initialization 
    p=np.zeros((ndim,n)) #Random parameter value for each particles
    for k in range(0,ndim):
        pk=np.random.rand(n,1)*(pmax[k]-pmin[k])+pmin[k]
        p[k]=pk.T
    
    pbest=p # Initial best value set equal to initial value
    gbest=np.zeros(ndim) # Initial global best value set equal to 0 for all parameters
    v=np.zeros((ndim,n)) # speed for each particles
    p_out=np.zeros(n) # Output for the current particle position
    pb_out=np.zeros(n) # Best personnal output for the particle
    gb_out=np.zeros(0) # Best global output for the swarm
    
    for i in range(0,n):
        pb_out[i]=Swarmfunction(pbest[:,i],hist)
    
    gb_out=pb_out[0]
       
    #Main Loop
    
    for epoch in range(0,imax):
        
        #Test if the new point is a personnal best
        if epoch<>0:
            for i in range(0,n):
                p_out[i]=Swarmfunction(p[:,i],hist)
                
            for i in range(0,n):    
                if p_out[i]<pb_out[i]:
                    for k in range(0,ndim):
                        pbest[k,i]=p[k,i]
                pb_out[i]=p_out[i]
                    
        #Check if the new personnal best is the global best
        for i in range(0,n):     
            if pb_out[i]<gb_out:
                for k in range(0,ndim):
                    gbest[k]=pbest[k,i]
                gb_out=pb_out[i]
        
        #Stop the function if global best output below treshold
        if gb_out<treshold:
            print "Global best below treshold:"+str(gbest)+"after "+str(epoch)+" iterations"
            return gbest
            break
        
        #Update speed of each particle
        for i in range(0,n):
            for k in range(0,ndim):
                v[k,i]=0.1*v[k,i]+1.5*random.random()*(pbest[k,i]-p[k,i])+2.5*random.random()*(gbest[k]-p[k,i])
                p[k,i]+=v[k,i]
    
    
    print "Global best after max iteration:"+str(gbest)      
    return gbest
    
def Swarmfunction(x,*hist):
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

