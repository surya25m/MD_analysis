##!/usr/bin/env python3
#Need em_charge.dat, atom.dat and alcl4_charge.dat files for calculating the charge
import os
import numpy as np
from itertools import repeat
import sys
no_em_atoms=int(input("Enter the number of atoms in a Cation molecule: "))
no_em_mol=int(input("Enter the number of cation molecules: "))
no_alcl4_atoms=5
no_alcl4_mol=int(input("Enter the number of AlCl4 molecules: "))
#no_em=19
#no_mol=9
new_file=[]
em_file_name='urea_chg.dat'
alcl_file_name='alcl4_charge.dat'
file_list=[]
file_list.extend(repeat(em_file_name,no_em_mol))
file_list.extend(repeat(alcl_file_name,no_alcl4_mol))
#print(file_list)
with open('combined_charge.dat', 'w') as outfile:
    for names in file_list:
        with open(names) as infile:
            outfile.write(infile.read())
with open('atom.dat','r') as m,open('combined_charge.dat','r') as n:
    with open('final.dat','w') as c:
        new_file=[]
        m=m.readlines()
        n=n.readlines()
        for i,line in enumerate(m):
            if "Atoms # full" in line:
                m_line_1=i+2
            if "Bonds" in line:
                m_line_2=i-1
        for i in range(m_line_1,m_line_2):
            new_file.append(m[i])
        for i,j in zip(new_file,n):
            i=i.split()
            j=j.split()
            i[3]=j[2]
            c.write('\t'.join(i))
            c.write('\n')
with open('final.dat','r') as f:
    sum=0
    f=f.readlines()
    for line in f:
        line=line.split()
        sum+=float(line[3])
    print("Total Charge = {}".format(round(sum,6)))
