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

def create_SWFN_LET_Skj(Lw,Ew,Tw, Swcr,Sorw,Krwmax,Cw,Co,Aw,Ao):
    string = "\nSWFN\n"
    lines=30
    Swmax = 1 - Sorw
    firsttime = True 
    string +="-- SW\tKRW\tPCw\n"
    
    for r in range(0,lines) : 	
        Sw=float(r)/lines
        if ((Sw - Swcr) < 0.0) :
               continue
        elif (Sw >= Swmax):
            break
        elif (firsttime):
              Sw = Swcr
              Krw = 0
              firsttime = False
	      SwPcw=Sw/ (1-Sw-Sorw)
              Pc =str(Cw/SwPcw**Aw)
    	else:
         Swn=(Sw-Swcr) / (1-Sorw-Swcr)
         SwPco=(1-Sw-Sorw) / (1-Sorw)
         SwPcw=Sw/ (1-Sw-Sorw)
         Krw = Krwmax * Swn**Lw / (Swn**Lw+Ew*(1-Swn)**Tw)
         Pc = Cw/SwPcw**Aw

        string +=" \t"+str(('%.2f' % Sw))+"\t"+str(Krw)+"\t"+str(Pc)+"\n"

    string +=" \t1.00\t1.000000\t0\n"
    string +=" \t/\n"
    
    
    return string
    
def create_SWFN_Corey_Skj(Swcr,Sorw,Krwmax,Nw,Cw,Co,Aw,Ao):
    string = "\nSWFN\n"
    lines=30
    Swmax = 1 - Sorw
    firsttime = True 
    string +="-- SW\tKRW\tPCw\n"
    
    for r in range(0,lines) : 	
        Sw=float(r)/lines
        if ((Sw - Swcr) < 0.0) :
               continue
        elif (Sw >= Swmax):
            break
        elif (firsttime):
              Sw = Swcr
              Krw = 0
              firsttime = False
              SwPcw=(Sw-Swir) / (1-Swir)
              Pc = 1
    	else:
         Swn=(Sw-Swcr) / (1-Sorw-Swcr)
         SwPco=(1-Sw-Sorw) / (1-Sorw)
         SwPcw=(Sw-Swir) / (1-Swir)
         Krw = Krwmax * Swn**Nw
         Pc = Cw/SwPcw**Aw-Co/SwPco**Ao

        string +=" \t"+str(('%.2f' % Sw))+"\t"+str(Krw)+"\t"+str(Pc)+"\n"

    string +=" \t1.00\t1.000000\t0\n"
    string +=" \t/\n"
    
    
    return string
    
def create_SGFN_LET(Lg,Eg,Tg, Sgcr,Swcr,Sorg,Krgmax):
    string = "\nSGFN\n"
    lines=30
    Sgmax = 1 - Sorg-Swcr
    firsttime = True 
    string +="-- SG\tKRW\tPCg\n"
    
    for r in range(0,lines) : 	
        Sg=float(r)/lines
        if ((Sg - Sgcr) < 0.0) :
               continue
        elif (Sg >= Sgmax):
            break
        elif (firsttime):
              Sg = 0
              Krg = 0
              firsttime = False
              Pc = 0
    	else:
         Sgn=Sg / (1-Sorg-Swcr)
         Krg = Krgmax * Sgn**Lg / (Sgn**Lg+Eg*(1-Sgn)**Tg)
         Pc = "0"

        string +=" \t"+str(('%.2f' % Sg))+"\t"+str(('%.6f' % Krg))+"\t"+str(Pc)+"\n"

    string +=" \t1.00\t1.000000\t0\n"
    string +=" \t/\n"
    
    return string

def create_SOF2_LET(Low,Eow,Tow,Swcr,Sorw):

    string = "\nSOF2\n"
    lines=30
    
    firsttime = True
    
    string +="-- SO\tKROW\tKROG\n"
    
    
    for r in range(0,lines) :
    	
        So=float(r) / lines
        if (So >= (1-Swcr)):
            break
        elif (firsttime):
            So = 0
            Krow = 0
            firsttime = False
        else:
    		if ((So - Sorw) < 0.0):
    			Krow=0
    		else: 
                 Son=(So-Sorw) / (1-Sorw-Swcr)
                 Krow = Son**Low / (Son**Low+Eow*(1-Son)**Tow)

    
    
        string +=" \t"+str(('%.2f' % So))+"\t"+str(('%.6f' % Krow))+"\n"
    
    So=1-Swcr
    string +=" \t"+str(('%.2f' % So))+"\t1.000000\n"
    string +=" \t/\n"
    return string

def create_SOF2_Corey(No,Swcr,Sorw):

    string = "\nSOF2\n"
    lines=30
    
    firsttime = True
    
    string +="-- SO\tKROW\tKROG\n"
    
    
    for r in range(0,lines) :
    	
        So=float(r) / lines
        if (So >= (1-Swcr)):
            break
        elif (firsttime):
            So = 0
            Krow = 0
            firsttime = False
        else:
    		if ((So - Sorw) < 0.0):
    			Krow=0
    		else: 
                 Son=(So-Sorw) / (1-Sorw-Swcr)
                 Krow = Son**No

    
    
        string +=" \t"+str(('%.2f' % So))+"\t"+str(('%.6f' % Krow))+"\n"
    
    So=1-Swcr
    string +=" \t"+str(('%.2f' % So))+"\t1.000000\n"
    string +=" \t/\n"
    return string
 
def RunEclipse(CASE):
    FNULL = open(os.devnull, 'r+')
    args = ("runeclipse","-i", CASE)
    subprocess.call(args, stdout=FNULL)
    
def WriteString(string,FILE):
    f=open(FILE,"w").close()
    f=open(FILE,"r+")
    f.write(string)
    f.close()

def WriteDATAfile(nblocks,nblocks_z,Lw,Ew,Tw, Swcr,Sorw,Krwmax,Low,Eow,Tow,Cw,Co,Aw,Ao):
    stringlist=[]
    size_x=round(Crop_pct/10/float(nblocks),2)
    size_z=round((1000-int(Inputs.filter[4])-int(Inputs.filter[5]))/10/float(nblocks_z),2)
    Cellnb=nblocks*nblocks*(nblocks_z )
    
    if Orientation=="Vertical":
        stringlist="RUNSPEC\nTITLE\nCoreSimulation\nDIMENS\n"+str(nblocks)+"\t"+str(nblocks)+"\t"+str(nblocks_z)+"/\n"
        stringlist+="OIL\nWATER\nLAB\nEQLDIMS\n1 100 10 0 0 /\n"
        stringlist+="TABDIMS\n1 1 50 15 0 15/\n"
        stringlist+="REGDIMS\n0 0 0 0/\n"
        stringlist+="WELLDIMS\n3 100 1 3/\n"
        stringlist+="NSTACK\n50/\n"
        stringlist+="START\n12 OCT 2015/\n"
        stringlist+="UNIFOUT\n"
        stringlist+="GRID\nINIT\nGRIDFILE\n0 1/\n"
        stringlist+="DX\n"+str(Cellnb)+"*"+str(size_x)+"/\n"
        stringlist+="DY\n"+str(Cellnb)+"*"+str(size_x)+"/\n"
        stringlist+="DZ\n"+str(Cellnb)+"*"+str(size_z)+"/\n"
        stringlist+="TOPS\n"
        for i in range(nblocks_z,0,-1):
        	stringlist+=str(nblocks**2)+"*"+str(i*size_z)+"\n"
        stringlist+="/\n"
        stringlist+="INCLUDE\n'PORO.INC' /\nINCLUDE\n'PERMX.INC' /\nINCLUDE\n'ACTNUM.INC' /\nCOPY\nPERMX PERMY /\nPERMX PERMZ /\n/\n"
        stringlist+="EDIT\n"
        stringlist+="PROPS\n"
        stringlist+=create_SWFN_LET_Skj(Lw,Ew,Tw, Swcr,Sorw,Krwmax,Cw,Co,Aw,Ao)+create_SOF2_LET(Low,Eow,Tow,Swcr,Sorw)
        stringlist+="DENSITY\n"+str(Oil_density)+"\t"+str(Water_density)+"/\n"
        stringlist+="PVCDO\n1\t1\t"+str(Oil_compressibility)+"\t"+str(Oil_viscosity)+"\n/\n"
        stringlist+="PVTW\n1\t1\t"+str(Water_compressibility)+"\t"+str(Water_viscosity)+"\n/\n"
        stringlist+="ROCK\n5801.5         2.8e-6   /\n"
        stringlist+="REGIONS\n"
        stringlist+="SOLUTION\n"
        stringlist+="PRESSURE\n"+str(Cellnb)+"*1 /\nSWAT\n"+str(Cellnb)+"*"+str(Swir)+"/\n"
        stringlist+="SUMMARY\n"
        stringlist+="FOPT\nFWPT\nFOIT\nFWIT\nBPR \n "+str(int(float(nblocks)/2)+1)+"\t"+str(int(float(nblocks)/2)+1)+" 1 /\n"+str(int(float(nblocks)/2)+1)+"\t"+str(int(float(nblocks)/2)+1)+"\t"+str(nblocks_z)+" /\n/\nRUNSUM\n"
        stringlist+="SCHEDULE\n"
        stringlist+="RPTSCHED\n'FIP=3' 'RESTART=2'  'WELLS=5'  'SUMMARY=2' 'RS' 'SGAS'  'SOIL'  'SWAT' 'PRESSURE' 'CPU=1' 'NEWTON=1'/\n"
        if Method=="USS":
            stringlist+="WELSPECS\nINJ1 G "+str(int(float(nblocks)/2)+1)+"\t"+str(int(float(nblocks)/2)+1)+" 1* WATER  /\nPROD1 G "+str(int(float(nblocks)/2)+1)+"\t"+str(int(float(nblocks)/2)+1)+" 1* OIL  /\n/\n"
            stringlist+="COMPDAT\nINJ1 2*   1 1 OPEN 2* 0.01 3* Z /\nPROD1 2* "+str(nblocks_z)+" \t"+str(nblocks_z)+" OPEN 2* 0.01 3* Z /\n/\n"
            stringlist+="WCONPROD\nPROD1 OPEN BHP 5* 1 /\n/\nWCONINJE\nINJ1 WATER OPEN RATE "+str(WaterRate)+" /\n/\nTSTEP\n100*0.017/\n"
        else:
            stringlist+="WELSPECS\nINJ1 G "+str(int(float(nblocks)/2)+1)+"\t"+str(int(float(nblocks)/2)+1)+" 1* WATER  /\nINJ2 G "+str(int(float(nblocks)/2)+1)+"\t"+str(int(float(nblocks)/2)+1)+" 1* OIL  /\nPROD1 G "+str(int(float(nblocks)/2)+1)+"\t"+str(int(float(nblocks)/2)+1)+" 1* OIL  /\n/\n"
            stringlist+="COMPDAT\nINJ1 2*   1 1 OPEN 2* 0.01 3* Z /\nINJ2 2*   1 1 OPEN 2* 0.01 3* Z /\nPROD1 2* "+str(nblocks_z)+" \t"+str(nblocks_z)+" OPEN 2* 0.01 3* Z /\n/\n"
            stringlist+="WCONPROD\nPROD1 OPEN BHP 5* 1 /\n/\nWCONINJE\nINJ1 WATER OPEN RATE "+str(WaterRate)+" /\nINJ2 OIL OPEN RATE "+str(WaterRate)+" /\n/\n"
            for i in range(1,nCycle):
                stringlist+="WCONPROD\nPROD1 OPEN BHP 5* 1 /\n/\nWCONINJE\nINJ1 WATER OPEN RATE "+str(WaterRate*(i/float(nCycle)))+" /\nINJ2 OIL OPEN RATE "+str(WaterRate*(nCycle-i)/float(nCycle))+" /\n/\n"
                stringlist+="TSTEP\n"+str(clength)+"*0.017/\n"
    else:
        stringlist="RUNSPEC\nTITLE\nCoreSimulation\nDIMENS\n"+str(nblocks_z)+"\t"+str(nblocks)+"\t"+str(nblocks)+"/\n"
        stringlist+="OIL\nWATER\nLAB\nEQLDIMS\n1 100 10 0 0 /\n"
        stringlist+="TABDIMS\n1 1 50 15 0 15/\n"
        stringlist+="REGDIMS\n0 0 0 0/\n"
        stringlist+="WELLDIMS\n3 100 1 3/\n"
        stringlist+="NSTACK\n50/\n"
        stringlist+="START\n12 OCT 2015/\n"
        stringlist+="UNIFOUT\n"
        stringlist+="GRID\nINIT\nGRIDFILE\n0 1/\n"
        stringlist+="DX\n"+str(Cellnb)+"*"+str(size_z)+"/\n"
        stringlist+="DY\n"+str(Cellnb)+"*"+str(size_x)+"/\n"
        stringlist+="DZ\n"+str(Cellnb)+"*"+str(size_x)+"/\n"
        stringlist+="TOPS\n"
        for i in range(nblocks,0,-1):
        	stringlist+=str(nblocks_z*nblocks)+"*"+str(i*size_x)+"\n"
        stringlist+="/\n"
        stringlist+="INCLUDE\n'PORO.INC' /\nINCLUDE\n'PERMX.INC' /\nINCLUDE\n'ACTNUM.INC' /\nCOPY\nPERMX PERMY /\nPERMX PERMZ /\n/\n"
        stringlist+="EDIT\n"
        stringlist+="PROPS\n"
        stringlist+=create_SWFN_LET_Skj(Lw,Ew,Tw, Swcr,Sorw,Krwmax,Cw,Co,Aw,Ao)+create_SOF2_LET(Low,Eow,Tow,Swcr,Sorw)
        stringlist+="DENSITY\n"+str(Oil_density)+"\t"+str(Water_density)+"/\n"
        stringlist+="PVCDO\n1\t1\t"+str(Oil_compressibility)+"\t"+str(Oil_viscosity)+"\n/\n"
        stringlist+="PVTW\n1\t1\t"+str(Water_compressibility)+"\t"+str(Water_viscosity)+"\n/\n"
        stringlist+="ROCK\n5801.5         2.8e-6   /\n"
        stringlist+="REGIONS\n"
        stringlist+="SOLUTION\n"
        stringlist+="PRESSURE\n"+str(Cellnb)+"*1 /\nSWAT\n"+str(Cellnb)+"*"+str(Swir)+"/\n"
        stringlist+="SUMMARY\n"
        stringlist+="FOPT\nFWPT\nFOIT\nFWIT\nBPR \n 1 "+str(int(float(nblocks)/2)+1)+"\t"+str(int(float(nblocks)/2)+1)+" /\n"+str(nblocks_z)+"\t"+str(int(float(nblocks)/2)+1)+"\t"+str(int(float(nblocks)/2)+1)+" /\n/\nRUNSUM\n"
        stringlist+="SCHEDULE\n"
        stringlist+="RPTSCHED\n'FIP=3' 'RESTART=2'  'WELLS=5'  'SUMMARY=2' 'RS' 'SGAS'  'SOIL'  'SWAT' 'PRESSURE' 'CPU=1' 'NEWTON=1'/\n"
        if Method=="USS":
            stringlist+="WELSPECS\nINJ1 G 1 "+str(int(float(nblocks)/2)+1)+" 1* WATER  /\nPROD1 G "+str(int(float(nblocks_z)))+"\t"+str(int(float(nblocks)/2)+1)+" 1* OIL  /\n/\n"
            stringlist+="COMPDAT\nINJ1 2*   "+str(int(float(nblocks)/2)+1)+" \t"+str(int(float(nblocks)/2)+1)+" OPEN 2* 0.01 3* Z /\nPROD1 2* "+str(int(float(nblocks)/2)+1)+" \t"+str(int(float(nblocks)/2)+1)+" OPEN 2* 0.01 3* Z /\n/\n"
            stringlist+="WCONPROD\nPROD1 OPEN BHP 5* 1 /\n/\nWCONINJE\nINJ1 WATER OPEN RATE "+str(WaterRate)+" /\n/\nTSTEP\n100*0.017/\n"
        else:
            stringlist+="WELSPECS\nINJ1 G 1 "+str(int(float(nblocks)/2)+1)+" 1* WATER  /\nINJ2 G 1 "+str(int(float(nblocks)/2)+1)+" 1* OIL  /\nPROD1 G "+str(int(float(nblocks_z)))+"\t"+str(int(float(nblocks)/2)+1)+" 1* OIL  /\n/\n"
            stringlist+="COMPDAT\nINJ1 2*   "+str(int(float(nblocks)/2)+1)+" \t"+str(int(float(nblocks)/2)+1)+" OPEN 2* 0.01 3* Z /\nINJ2 2*   "+str(int(float(nblocks)/2)+1)+" \t"+str(int(float(nblocks)/2)+1)+" OPEN 2* 0.01 3* Z /\nPROD1 2* "+str(int(float(nblocks)/2)+1)+" \t"+str(int(float(nblocks)/2)+1)+" OPEN 2* 0.01 3* Z /\n/\n"
            
            for i in range(1,nCycle-1):
                stringlist+="WCONPROD\nPROD1 OPEN BHP 5* 1 /\n/\nWCONINJE\nINJ1 WATER OPEN RATE "+str(WaterRate*(float(i)/nCycle))+" /\nINJ2 OIL OPEN RATE "+str((nCycle-i)/float(nCycle))+" /\n/\n"
                stringlist+="TSTEP\n"+str(clength)+"*0.017/\n"
    
    string="".join(stringlist)
    WriteString(string,"CORE_TEST.DATA")

def PlotEclipseResults(CASE):
    summary = ecl.EclSum(CASE)
    if Method=="USS":  
        FOPT=summary["FOPT"]
        FWPT=summary["FWPT"]
    
            
        if Orientation=="Vertical":
            BPR_IN=summary["BPR:"+str(int(float(nblocks)/2)+1)+","+str(int(float(nblocks)/2)+1)+","+str(nblocks_z)]
            BPR_OUT=summary["BPR:"+str(int(float(nblocks)/2)+1)+","+str(int(float(nblocks)/2)+1)+",1"]
        else:
            BPR_IN=summary["BPR:1,"+str(int(float(nblocks)/2)+1)+","+str(int(float(nblocks)/2)+1)]
            BPR_OUT=summary["BPR:"+str(nblocks_z)+","+str(int(float(nblocks)/2)+1)+","+str(int(float(nblocks)/2)+1)]
                            
        BPR_IN_init=BPR_IN.first.value
        BPR_OUT_init=BPR_OUT.first.value
        FOPT_values=[]
        FWPT_values=[]
        DIFF=[]
        
        for node1,node2,node3,node4 in zip(FOPT,FWPT,BPR_IN,BPR_OUT):
                FOPT_values+=[node1.value]
                FWPT_values+=[node2.value]
                DIFF+=[abs(node3.value-node4.value)/abs(BPR_IN_init/BPR_OUT_init)]
    
    else:
        FOPT=summary["FOPT"]
        FWPT=summary["FWPT"]
        FOIT=summary["FOIT"]
        FWIT=summary["FWIT"]

        if Orientation=="Vertical":
            BPR_IN=summary["BPR:"+str(int(float(nblocks)/2)+1)+","+str(int(float(nblocks)/2)+1)+","+str(nblocks_z)]
            BPR_OUT=summary["BPR:"+str(int(float(nblocks)/2)+1)+","+str(int(float(nblocks)/2)+1)+",1"]
        else:
            BPR_IN=summary["BPR:1,"+str(int(float(nblocks)/2)+1)+","+str(int(float(nblocks)/2)+1)]
            BPR_OUT=summary["BPR:"+str(nblocks_z)+","+str(int(float(nblocks)/2)+1)+","+str(int(float(nblocks)/2)+1)]
                            
        BPR_IN_init=BPR_IN.first.value
        BPR_OUT_init=BPR_OUT.first.value
        FOPT_values=[]
        FWPT_values=[]
        DIFF=[]
        
        for node1,node2,node3,node4,node5,node6 in zip(FOPT,FWPT,BPR_IN,BPR_OUT,FOIT,FWIT):
                FOPT_values+=[node1.value-node5.value]
                FWPT_values+=[node2.value-node6.value]
                DIFF+=[abs(node3.value-node4.value)/abs(BPR_IN_init/BPR_OUT_init)]
    
    plt.plot(FOPT_values,'g',DIFF,'r')
    plt.show()
  




