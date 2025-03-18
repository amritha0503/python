
import matplotlib.pyplot as plt
import numpy as np
cat=[]
amt=[]
try:
    with open ('expenses.txt','r') as f:
        for line in f:
            categories,amount=line.strip().split()
            cat.append(categories)
            amt.append(float(amount))
    total=np.sum(amt)
   
    plt.figure(figsize=(10,5))
    plt.bar(cat,amt,color='blue')
    plt.xlabel('Categories')
    plt.ylabel('Amount')
    print("Total expenses: ",total)
    plt.show()
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)
