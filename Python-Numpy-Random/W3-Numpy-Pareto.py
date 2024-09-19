# numpy random pareto distribution
import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

x = random.pareto(a=2,size=100)
print(x)
sns.displot(x,kind='kde')
plt.show()