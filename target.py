def findingInts(l,target):
    for i in range(len(l)):
        for j in range(len(l)):
          if l[i] + l[j] == target:
              return [l[i],l[j]]
              
              
print(findingInts([1,2,2,5,2,6],4))
