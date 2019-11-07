# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:21:12 2019

@author: Sampad Acharya
"""
#Given the names and grades for each student in a Physics class of N  students,
# store them in a nested list and print the name(s) of 
#any student(s) having the second lowest grade.

if __name__ == '__main__':
    newName=['Harry', 'Berry', 'Tina', 'Akriti', 'Sam']
    newScore=[4,32,36,39,40]
    arr =newScore
    n=len(newScore)
    print(n)
    minValue=min(arr)
    def indexVal(arr,minValue ,n):
        index=[]
        
        for i in range(n):
          if arr[i]==minValue:
#            print(i)
            m=i
            index.append(m)
        return index    
        

indexRange=indexVal(arr, minValue,n)
#print((indexRange))
maxVal=max(arr)
for i in range(len(indexRange)):
    arr[indexRange[i]]=maxVal+100
newArr=arr
#print(newArr)
newMinValue=min(newArr)
#print(newMinValue)
newMinIndex=indexVal(newArr,newMinValue ,n)
print(newMinIndex)
runnerUp=min(newArr)
print(runnerUp)

sortedName=[]
print(len(newMinIndex))
for i in range(len(newMinIndex)):
     print(i)
     sortedName.append(newName[newMinIndex[i]])
#print(sortedName)
sortedName.sort()
print(sortedName[0])