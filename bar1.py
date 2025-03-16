import matplotlib as mpl
import matplotlib.pyplot as plt


programminglang=['c++','java','python','c#','php','javascript']
popularity=[10,22,24,8,16,14]
colors=['red','blue','green','yellow','orange','purple']
plt.figure(figsize=(10,5))
plt.bar(programminglang,popularity,color=colors)

plt.title('Programming Language Usage')
plt.xlabel('Programming Language')
plt.ylabel('Popularity')

plt.show()