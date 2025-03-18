list1=input("Enter the list elements seperated by spaces").split()
k=int(input("Enter no of positions to rotate"))
k=k%len(list1)
rotate_list=list1[-k:]+list1[:-k]
print("The rotated list is:",rotate_list)
