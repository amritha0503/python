str=input("Enter the sentence: ")
arr=str.split()

for word in arr: #word arraynn oro wordsum eduthu
    count=0 #oro worsdum count cheythitt count initalise cheyythuu
    for char in word: #wordile oro characterum edukkunnu
        count+=1
    print(f" {word} : {count}")