# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:10:34 2019

@author: SampadAcharya
"""

if __name__ == '__main__':
    n = 5
    arr = [-7,-7,-7,-7,-6]
    index=[]

 
    def indexVal(arr, maxVal,n):
        for i in range(n):
          if arr[i]==maxVal:
#            print(i)
            m=i
            index.append(m)
        return index    
    
maxVal=max(arr)          

indexRange=indexVal(arr, maxVal,n)
#print((indexRange))

for i in range(len(indexRange)):
    arr[indexRange[i]]=-200
newArr=arr
#print(newArr)

runnerUp=max(newArr)
print(runnerUp)
