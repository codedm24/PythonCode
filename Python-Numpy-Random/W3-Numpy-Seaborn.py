# numpy random seaborn module
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

print('plotting a distplot with histogram')
sns.histplot([0,1,2,3,4,5],kde=True)
plt.show()

sns.displot([0,1,2,3,4,5],kind='kde')
plt.show()

print('plotting a distplot without histogram')
sns.displot([0,1,2,3,4,5])
plt.show()


print('Generate a distplot of 2-D array')
x = random.choice([3,5,7,9],p=[0.1,0.3,0.4,0.2],size=(3,5))
print(x)
sns.displot(x,kind='hist')
plt.show()

sns.displot(x,kind='kde')
plt.show()

sns.histplot(x,kde=True)
plt.show()