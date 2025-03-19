import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,400)
ch=0
while True:
    print("1.y=x^2")
    print("2.y=2x")
    print("3.y=e^x")
    print("4.y=sqrtx")
    print("5.Exit")

    ch=int(input("Enter your choice:"))
    if ch==1:
        y1=x**2
        plt.figure(figsize=(6,4))
        plt.plot(x,y1,label='y=x^2',color='red')
        plt.title('y=x^2')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
    elif ch==2:
        y2=2*x
        plt.figure(figsize=(6,4))
        plt.plot(x,y2,label='y=2x',color='red')
        plt.title('y=2x')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
    elif ch==3:
        y3=np.exp(x)
        plt.figure(figsize=(6,4))
        plt.plot(x,y3,label='y=e^x',color='red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('y=e^x')
        plt.grid(True)
        plt.show()
    elif ch==4:
        y4=np.sqrt(x)
        plt.figure(figsize=(6,4))
        plt.plot(x,y4,label='y=sqrtx',color='red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('y=sqrtx')
        plt.grid(True)
        plt.show()
    elif ch==5:
        break
    else:
        print("Invalid choice")
    
