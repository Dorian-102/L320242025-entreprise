list1 = [1, 2, 3]
list2 = [4, 5, 6]

listfinale = (
    tuple((x,y,x+y) for x in list1 for y in list2 if (x+y)%2==0),
    tuple((x,y,x+y) for x in list1 for y in list2 if (x+y)%2!=0)
    )

print(listfinale)