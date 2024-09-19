# numpy random multinomial distribution
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6],size=16)
print(x)
sns.displot(x,kind='kde')
plt.show()