def reverse(givenList):
   reverseList=[]
   for i in range(len(givenList)):
      newList= givenList[((len(givenList))-1)-i]
      reverseList.append(newList)
      print(newList)
   return reverseList

print(reverse([11,2,33,4,50]))
