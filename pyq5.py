import numpy as np
import scipy.stats as stats
n=8
p=0.5
p_of_less_4=stats.binom.cdf(3,n,p)
print(p_of_less_4)
p_more_5=1-stats.binom.cdf(5,n,p)
print(p_more_5)