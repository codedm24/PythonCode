#Scipy Significance Tests
import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import kstest
from scipy.stats import describe
from scipy.stats import kurtosis, skew
from scipy.stats import normaltest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('T-Test')
v1 = np.random.normal(size=100)
#print("v1",v1)

v2 = np.random.normal(size=100)
#print("v2",v2)

res = ttest_ind(v1, v2)
pvalue = ttest_ind(v1, v2).pvalue

print('res', res)
print('pvalue', pvalue)

dataset = {
    "V1" : v1,
    "V2" : v2 
}

df = pd.DataFrame(dataset)

df.plot(x="V1",y="V2",kind='scatter',marker='o')

plt.title('V1 vs V2')
plt.xlabel('X cordinate')
plt.ylabel('Y coordinate')
plt.show()

print('KS-Test')

v = np.random.normal(size=100)

res = kstest(v,'norm')

print(res)

data = describe(v)
print(data)

sns.histplot(v,kde=True)
plt.show()

print('Normality Tests')

v = np.random.normal(size=100)

print('skew')
print(skew(v))
print('kurtosis')
print(kurtosis(v))
print('normaltest')
print(normaltest(v))


