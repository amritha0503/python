str=input("Enter the string: ")
words=str.lower().split()
palindrome=[]
for word in words:
    if word==word[::-1]:
        palindrome.append(word)
palindrome.sort()
if  palindrome:#palindrome empty allenkil
    for word in palindrome:
         print(word)
else:
    print("No palindromes found")
#print(f"Palindrome words are: {palindrome}")