str=input("Enter the string: ")
dele=input("Enter the string to be replaced ")
rep=input("Enter a string to replace ")
arr=str.split()#stringine split cheythu words aakkii arrayil store cheythu
repcount=0
for i in range(0,len(arr)):
    if arr[i]==dele:
        arr[i]=rep
        repcount=repcount+1
finalstring=" ".join(arr)       
print(f"replaced string is : \n {finalstring}")
