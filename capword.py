sentence = input("Enter the string: ")
words = sentence.split()
capitalized_words = []

for word in words:
    if word:  # Check if word is not empty
        capitalized_word = word[0].upper() + word[1:] #first letter capital cheyyunnu   
        capitalized_words.append(capitalized_word) #capitalized word arrayil store cheyyunnu    

result = " ".join(capitalized_words)
print(f"Capitalized string: {result}")