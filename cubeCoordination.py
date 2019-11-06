# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:45:37 2019

@author: Sampad Acharya
"""

#X, Y and Z are the three coordinates of a cuboid.

#Now X=1,Y=1, Z=1 and N=2.

#I have to generate a list of all possible coordinates on a 3D
# grid where the sum of Xi + Yi + Zi is not equal to N. If X=2, 
#the possible values of Xi can be 0, 1 and 2. The same applies to Y and Z.

if __name__ == '__main__':
   

    def coordination(x,y,z,n):
        SS=[]
        for i in range(x+1):
            for j in range(y+1):
                for k in range(z+1):
                    coordinate=[i,j,k]
                    if (i+j+k)!=n:
                       SS.append(coordinate)


        return SS
#      x = 1
#      y = 1
#      z = 1
#      n = 2
print(coordination(1,1,1,2))