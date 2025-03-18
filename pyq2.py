import scipy.stats as stats
import numpy as np
observed=np.array([[200,150,50],[250,300,50]])
alpha=0.05
chi2,p_value,dof,expected=stats.chi2_contingency(observed)
tablechi2=stats.chi2.ppf(1- alpha, dof)
print("Chi2 value: ",chi2)
print("Table value: ",tablechi2)
print("P value: ",p_value)
print("Degree of freedom: ",dof)
print("Expected value: ",expected)
if chi2>tablechi2:
    print("voting preferences are differ. Reject ho")
else:
    print("same. not reject ho")