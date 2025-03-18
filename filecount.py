try:
    with open('file.txt','r')as f:
        text=f.read()
    
    wordcount=0
    sentencecount=0
    uppercase=0
    lowercase=0
    specialchar=0
    
    words=text.split()
    wordcount=len(words)

    for char in text:
        if char.isupper():
             uppercase+=1
        elif char.islower():
            lowercase+=1
        elif char in ['.','!','?']:
            sentencecount+=1
        elif char in ['@','#','$','%','^','&','*','(',')','_','+','-','/','\\','|','<','>',';',':','[',']','{','}','=']:
            specialchar+=1
    print(f"Word count: {wordcount}")
    print(f"Sentence count: {sentencecount}")
    print(f"Uppercase count: {uppercase}")
    print(f"Lowercase count: {lowercase}")
    print(f"Special character count: {specialchar}")
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
        