'''Two arrays
Remove Duplicates arr1=[3,2]
Find Common Elements of two arrays'''
arr1=[3,1,1,2]
arr2=[4,3,3,2,1]
a1=[]
a2=[]
for i in arr1:
    if arr1.count(i)<2:
        a1.append(i)
for j in arr2:
    if arr2.count(j)<2:
        a2.append(j)
for i in a1:
    for j in a2:
        if i==j:
            print(i)
