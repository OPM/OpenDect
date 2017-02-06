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

import numpy as np
import math

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
    mask = (nx*nx + ny*ny > r*r)
    x[mask]=0
	
    return x
    
def GetMaskedValues2(x,Offsetr,Offsetc,Crop_pct,Diameter):

	# A circle shape is generated based on the diameter and the x/y offsets
    n=x.shape[0]
    a=n/2+Offsetc
    r=1-float(Crop_pct)/Diameter
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






