list1= [1,2,3,4,5,5,6,7,8,8,8,9,9,9,9,10]
unique=[]
for x in list1:
    if x not in unique:
        unique.append(x)
print(unique)