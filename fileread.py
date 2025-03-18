try:
    with open('file.txt','r') as f:
        text=f.read()
        print(text)
    with open('file.txt','a')as f:#append  modeill file open akkanam
        f.write("\nthese are the programming languages")
        print("data written successfully")
        
    with open('file.txt','r') as f:
        text=f.read()
        print(text)
except Exception as e:
    print(e)