import numpy as np
import scipy.stats as stats
n=16
pop_mean=20
sam_mean=22
sd=3
alpha=0.05
t=(sam_mean-pop_mean)/(sd/np.sqrt(n))
dof=n-1
t_critical=stats.t.ppf(1-alpha,dof)
print(f"value of t is {t}")
print(f"value of t_critical is {t_critical}")
if t>t_critical:
    print("reject ho")
else:
    print("accept ho")