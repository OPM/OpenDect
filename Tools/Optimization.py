'''
  Copyright 2016 Statoil ASA. 
 
  This file is part of the Open Porous Media project (OPM). 
 
  OPM is free software: you can redistribute it and/or modify 
  it under the terms of the GNU General Public License as published by 
  the Free Software Foundation, either version 3 of the License, or 
  (at your option) any later version. 
  
   OPM is distributed in the hope that it will be useful, 
   but WITHOUT ANY WARRANTY; without even the implied warranty of 
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
   GNU General Public License for more details. 
  
   You should have received a copy of the GNU General Public License 
   along with OPM.  If not, see <http://www.gnu.org/licenses/>. 
'''

from CoreSimulation import WriteDATAfile,RunEclipse,PlotEclipseResults
import numpy as np
import random
import os
import subprocess
import ert.ecl as ecl
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

def Swarm(hist,imax,n,pmin,pmax,treshold,window,app):
    
    #Get parameters from inputs
    ndim=len(pmax)

    #Initialization 
    p=np.zeros((ndim,n)) #Random parameter value for each particles
    for k in range(0,ndim):
        pk=np.random.rand(n,1)*(pmax[k]-pmin[k])+pmin[k]
        p[k]=pk.T
    
    pbest=p # Initial best value set equal to initial value
    gbest=np.ones(ndim)*0.1 # Initial global best value set equal to 0 for all parameters
    v=np.zeros((ndim,n)) # speed for each particles
    p_out=np.zeros(n) # Output for the current particle position
    pb_out=np.zeros(n) # Best personnal output for the particle
    gb_out=np.zeros(0) # Best global output for the swarm
    
    for i in range(0,n):
        pb_out[i]=Swarmfunction(pbest[:,i],window.hist,window.ExpParams,window.Orientation,window.Padding_top,window.Padding_bottom,window.Crop_pct,window.nblocks,window.nblocks_z,window.nCycle,window.clength,window.Swir)
    
    gb_out=pb_out[0]
       
    #Main Loop
    
    for epoch in range(0,imax):
        window.SetProgress(float(epoch)/imax*100,3)
        #Test if the new point is a personnal best
        if epoch<>0:
            for i in range(0,n):
                p_out[i]=Swarmfunction(p[:,i],window.hist,window.ExpParams,window.Orientation,window.Padding_top,window.Padding_bottom,window.Crop_pct,window.nblocks,window.nblocks_z,window.nCycle,window.clength,window.Swir)
                
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
                window.Writetoconsole("New Best values with delta "+str(gb_out))
        
        #Stop the function if global best output below treshold
        if gb_out<treshold:
            window.Writetoconsole("Global best below treshold:"+str(gbest)+"after "+str(epoch)+" iterations")
            return gbest
            break
        
        #Update speed of each particle
        for i in range(0,n):
            for k in range(0,ndim):
                v[k,i]=0.1*v[k,i]+1.5*random.random()*(pbest[k,i]-p[k,i])+2.5*random.random()*(gbest[k]-p[k,i])
                p[k,i]+=v[k,i]
    	
	window.label_24.setText(str(gbest[5]))
	window.label_25.setText(str(gbest[6]))
	window.label_26.setText(str(gbest[7]))
	window.label_27.setText(str(gbest[0]))
	window.label_30.setText(str(gbest[1]))
	window.label_29.setText(str(gbest[2]))
	window.label_32.setText(str(gbest[3]))
	window.label_34.setText(str(gbest[4]))
	FOPT,DIFF=PlotEclipseResults("temp/CORE_TEST",window.ExpParams,window.Orientation,window.nblocks,window.nblocks_z)
	plt.clf()
	fig  = plt.figure(facecolor="white")
	ax  = fig.add_subplot(111)
	ax.plot(FOPT,'g',DIFF,'r')
	canv = FigureCanvas(fig)   
	window.grid.addWidget(canv, 0, 0)
	window.widget.setLayout(window.grid)
    	window.widget.show()
	app.processEvents()
    
    window.Writetoconsole("Global best after max iteration:"+str(gbest)+" with "+str(gb_out))
    window.SetProgress(0,3)
    return gbest
    
def Swarmfunction(x,hist,ExpParams,Orientation,Padding_top,Padding_bottom,Crop_pct,nblocks,nblocks_z,nCycle,clength,Swcr):
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
    Epsilon=0.00001
    WriteDATAfile(ExpParams,Orientation,Padding_top,Padding_bottom,Crop_pct,nblocks,nblocks_z,Lw,Ew,Tw, Swcr,Sorw,Krwmax,Low,Eow,Tow,Cw,Co,Aw,Ao,nCycle,clength)
    RunEclipse("temp/CORE_TEST.DATA")
    summary = ecl.EclSum("temp/CORE_TEST")
    
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

