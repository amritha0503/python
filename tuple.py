t=() #initializing tuple
eventup=()
oddtup=()
n=int(input("Enter the limit: "))
print("Enter the elements")
for i in range(n):
    a=int(input())
    t=t+(a,) #adding elements to tuple
for i in t:
    if i%2==0:
         eventup=eventup+(i,) #adding even elements to eventup tuple
    else:
        oddtup=oddtup+(i,)
print("Even Numbers: ",eventup)
print("Odd numbers: ",oddtup)