import numpy as np
midpoints=[5,15,25,35,45,55,65,75]
frequency=[5,10,20,40,30,20,10,5]
mean=np.sum(np.array(frequency)*np.array(midpoints))/np.sum(frequency)
variance=np.sum(frequency*(midpoints-mean)**2)/np.sum(frequency)
sd=np.sqrt(variance)
coeff_var=sd/mean
print(sd)
print(coeff_var)
