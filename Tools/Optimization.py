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

from CoreSimulation import WriteDATAfile,RunEclipse_checkout,PlotEclipseResults
import numpy as np
import random
import os
import subprocess
from subprocess import check_output
import ert.ecl as ecl
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

def Swarm(imax,n,pmin,pmax,treshold,window,app):
    
    #Get parameters from inputs
    ndim=len(pmax)
    
    #Get historical data
    hist_oil=[]
    hist_water=[]
    hist_diff=[]

    for node in window.hist:
	hist_oil+=[float(node.split("\t")[0])]
	hist_water+=[float(node.split("\t")[1])]
	hist_diff+=[float(node.split("\t")[2])]

    #Initialization 
    p=np.zeros((ndim,n)) #Random parameter value for each particles
    for k in range(0,ndim):
        pk=np.random.rand(n,1)*(pmax[k]-pmin[k])+pmin[k]
        p[k]=pk.T
    
    pbest=p # Initial best value set equal to initial value
    gbest=np.zeros(ndim)
    
    index=0
    for j,param in enumerate(window.StaticParams):
	if window.ActiveParams[j]:
		gbest[index]=window.StaticParams[j]
		index+=1
		
    
    v=np.zeros((ndim,n)) # speed for each particles
    p_out=np.zeros(n) # Output for the current particle position
    pb_out=np.zeros(n) # Best personnal output for the particle
    gb_out=np.zeros(0) # Best global output for the swarm

    pb_out=Swarmfunction(pbest,window.hist,window.ExpParams,window.Orientation,window.Padding_top,window.Padding_bottom,window.Crop_pct,window.nblocks,window.nblocks_z,window.nCycle,window.clength,window.Swir,n,window)
    
    gb_out=pb_out[0]
       
    #Main Loop

    for epoch in range(0,imax):

        window.SetProgress(float(epoch)/imax*100,3)
        #Test if the new point is a personnal best
        if epoch<>0:
	    window.Writetoconsole("Step "+str(epoch)+":Running Simulations...")
            p_out=Swarmfunction(p,window.hist,window.ExpParams,window.Orientation,window.Padding_top,window.Padding_bottom,window.Crop_pct,window.nblocks,window.nblocks_z,window.nCycle,window.clength,window.Swir,n,window)
                
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
                
                index=0
	        for j,param in enumerate(window.StaticParams):
			if not window.ActiveParams[j]:window.DynamicParams[j]=param
			else:
				window.DynamicParams[j]=gbest[index]
				index+=1
	                
                window.label_24.setText(str(window.DynamicParams[0]))
		window.label_25.setText(str(window.DynamicParams[1]))
		window.label_26.setText(str(window.DynamicParams[2]))
		window.label_27.setText(str(window.DynamicParams[3]))
		window.label_30.setText(str(window.DynamicParams[4]))
		window.label_29.setText(str(window.DynamicParams[5]))
		window.label_32.setText(str(window.DynamicParams[6]))
		window.label_34.setText(str(window.DynamicParams[7]))
		window.label_48.setText(str(window.DynamicParams[8]))
		window.label_49.setText(str(window.DynamicParams[9]))
		window.label_50.setText(str(window.DynamicParams[10]))
		window.label_51.setText(str(window.DynamicParams[11]))

		FOPT,FWPT,DIFF=PlotEclipseResults("temp/CORE_TEST-"+str(i),window.ExpParams,window.Orientation,window.nblocks,window.nblocks_z)
		plt.clf()	
		ax  = window.fig.add_subplot(221)
		ax.plot(FOPT,'g',hist_oil,'g--')
		ax  = window.fig.add_subplot(222)
		ax.plot(FWPT,'r',hist_water,'r--')
		ax  = window.fig.add_subplot(223)
		ax.plot(DIFF,'r',hist_diff,'r--')
		window.canv.draw()
		window.Writetoconsole("New Best values with delta "+str(gb_out))
		app.processEvents()
                
        
        #Stop the function if global best output below treshold
        if gb_out<treshold:
            window.Writetoconsole("Global best below treshold:"+str(gbest)+"after "+str(epoch)+" iterations")
            return gbest
            break
        
        #Update speed of each particle
        for i in range(0,n):
            for k in range(0,ndim):
                v[k,i]=v[k,i]+1.5*random.random()*(pbest[k,i]-p[k,i])+2.5*random.random()*(gbest[k]-p[k,i])
                if p[k,i]+v[k,i]<pmax[k] and  p[k,i]+v[k,i]>pmin[k] and p[k,i]+v[k,i]>0:p[k,i]+=v[k,i]
                
    	


    
    window.Writetoconsole("Global best after max iteration:"+str(gbest)+" with "+str(gb_out))
    window.SetProgress(0,3)
    return gbest
    
def Swarmfunction(p,hist,ExpParams,Orientation,Padding_top,Padding_bottom,Crop_pct,nblocks,nblocks_z,nCycle,clength,Swcr,n,window):
	joblist=[]
	pb_out=[]
	currentjobs=True
	


	for i in range(0,n):
	    
	    index=0
	    for k,param in enumerate(window.StaticParams):

		if not window.ActiveParams[k]:window.DynamicParams[k]=param
		else:	
			window.DynamicParams[k]=p[index,i]
	    		index+=1
	    
	    window.Writetoconsole("Running simulation for :"+str(window.DynamicParams))
	    Epsilon=0.00001
	    WriteDATAfile(window.height,ExpParams,Orientation,Padding_top,Padding_bottom,Crop_pct,nblocks,nblocks_z,window.DynamicParams[3],window.DynamicParams[4],window.DynamicParams[5], Swcr,window.DynamicParams[6],window.DynamicParams[7],window.DynamicParams[0],window.DynamicParams[1],window.DynamicParams[2],window.DynamicParams[11],window.DynamicParams[10],window.DynamicParams[9],window.DynamicParams[8],nCycle,clength,i)
	    joblist+=[RunEclipse_checkout("temp/CORE_TEST-"+str(i)+".DATA")]
	    
	    
	while (currentjobs==True):
		currentjobs=Testforjobs(joblist)


	for i in range(0,n):
	    summary = ecl.EclSum("temp/CORE_TEST-"+str(i)+".DATA")

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
	    pb_out+=[np.sum(DELTA[0]+DELTA[1]+DELTA[2])] #opt on oil only so far
   
	return pb_out

def Testforjobs(x):
	for job in x:
		if job.split()[0] in check_output("bjobs"):
			return True	
	return False