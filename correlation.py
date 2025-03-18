import numpy as np 

hand_size=[17,15,19,17,21]
height=[150,154,169,172,175]
a=np.array(hand_size)
b=np.array(height)
corr_coeff=np.corrcoef(a,b)[0,1]
print(corr_coeff)
if(corr_coeff>0):
 print("Positive correlation")
elif(corr_coeff<0):
  print("Negative correlation")
else:
  print("No correlation between handsize and height")
  