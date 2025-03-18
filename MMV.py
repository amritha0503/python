import numpy as np
data={'state':['alabama','alaska','arizona','arkansas','california','colorado','connecticut','delware'],
      'popu':[4779736,710231,6392017,2915918,37253956,5029196,3574097,897934],
      'murderrate':[5.7,5.6,4.7,5.6,4.4,2.8,2.4,5.8]}
population=np.array(data['popu'])
murderrate=np.array(data['murderrate'])
murderpop=(population*murderrate)/100000
meanpop=np.mean(murderpop)
medianpop=np.median(murderpop)
variancepop=np.var(murderpop)
print(meanpop)
print(medianpop)
print(variancepop)
