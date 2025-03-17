n=int(input("Enter the limit :"))
list1=[]
list2=[]
for i in range(n):
    a=int(input("Enter the element "))
    list1.append(a)
for i in  list1: #list1 il ulla oro elementsinem edukkunnuu check cheyyunnu
    if i not in list2:
        list2.append(i)
print("Without Duplicates ",list2)