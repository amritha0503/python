r1=int(input("Enter no.of rows in matrix1"))
c1=int(input("Enter no.of columns in matrix1"))
r2=int(input("Enter no.of rows in matrix2"))
c2=int(input("Enter no.of columns in matrix2"))
if (r1!=r2 and c1!=c2):
    print("Matrix addition is not possible")
    exit()
mat1=[]
mat2=[]
print("Enter the elements of matrix1")
for i in range(0,r1):
    row=[]
    for j in range(0,c1):
      element=int(input())
      row.append(element)
    mat1.append(row)
print("Enter the elements of matrix2")
for i in range(0,r2):
    row=[]
    for j in range(0,c2):
        element=int(input())
        row.append(element)
    mat2.append(row)

result=[]

for i in range(0,r1):
    row=[]
    for j in range(0,c1):
        row.append(mat1[i][j]+mat2[i][j])
    result.append(row)
print("The sum of two matrices is: \n")

for i in range (0,r1):
    for j in range(0,c1):
        print(result[i][j],end="")
    print()