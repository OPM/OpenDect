import dicom
import numpy as np
import math
import pylab
import matplotlib.pyplot as plt
import os
import sys
from os import listdir
from os.path import join
from decimal import Decimal
import subprocess
import ert.ecl as ecl
from pyswarm import pso

def GetMult(rows):
    
    found=False
    while found==False:
        istart=int(round(math.sqrt(rows)))
        for i in range(istart,rows):
            if rows%i==0:
                found=True
                return max(i,rows/i),min(i,rows/i)
        rows+=1


     


def UpscaleGrid(x,y,n):

	x=GetUniqueInt(x)
	y=GetUniqueInt(y)
	x,y=np.meshgrid(x,y,indexing='ij')
	return x,y

def GetUniqueInt(x):
        x=x/n
        x.astype(int)
        x=np.unique(x)
	return x

def UpscalePoro(z,x,y,nblocks,n):
    
    new = np.ones((nblocks,nblocks))
       
    x=x/n
    x.astype(int)
    y=y/n
    y.astype(int)
    
    for xi,yi,zi in zip(x,y,z):
        for xii,yii,zii in zip(xi,yi,zi):
            new[xii][yii]+=zii
    for i in enumerate(new):
		for j in enumerate(new[i[0]]):
			new[i[0]][j[0]]=j[1]/float(n**2)

    return new
 
def GetMaskedValues(x,Offsetr,Offsetc):

	# A circle shape is generated based on the diameter and the x/y offsets
    n=x.shape[0]
    a=n/2+Offsetc
    b=n/2+Offsetr
    r=n/2
    ny,nx = np.ogrid[-a:n-a, -b:n-b]
    	
    	# The mask will apply to the values inside the circle
    	
    mask = nx*nx + ny*ny > r*r
    x[mask]=0

    return x

def GetMaskedValues2(x,Offsetr,Offsetc,Crop_pct,Diameter):

	# A circle shape is generated based on the diameter and the x/y offsets
    n=x.shape[0]
    a=n/2+Offsetc
    r=1-Crop_pct/Diameter

    x=x[a*r:-a*r,a*r:-a*r]

    return x

def GetPoro(x1,x2,parameters):	 
		 # Show the image in the middle og the core
    
    rho_matrix=float(parameters[0])
    rho_fluid=float(parameters[1])
    M=float(parameters[2])
    P=float(parameters[3])
    Q=float(parameters[4])

    Density=M*(x1)+P*(x2)+Q
    Phi=(rho_matrix-Density)/(rho_matrix-rho_fluid)
 
    return Phi

def pltCircle(ds1,Offsetr,Offsetc):
    a=int(ds1.shape[0]*Crop_pct/Diameter/2)
    pylab.imshow(ds1, cmap=pylab.cm.bone)
    circle=plt.Circle((ds1.shape[0]/2+Offsetr,ds1.shape[0]/2+Offsetc),a,color='r',linewidth=1,fill=False)
    pylab.gcf().gca().add_artist(circle)
    pylab.plot((a-10+Offsetr , a+10+Offsetr), (a+Offsetc, a+Offsetc), 'k')
    pylab.plot((a+Offsetr, a+Offsetr),(a-10+Offsetc , a+10+Offsetc), 'k')
    pylab.show()





