#
import pandas as pd
import numpy as np
from scipy import stats

# Sample data
data = {'value': [10, 12, 13, 12, 1000, 11, 13, 12, 14, 15]}
df = pd.DataFrame(data)

print(type(data))

print(type(df))

# Calculate z-scores
df['z_score'] = np.abs(stats.zscore(df['value']))

# Define a threshold to identify outliers
threshold = 1

# Filter out outliers
df_no_outliers = df[df['z_score'] < threshold]

print(df_no_outliers)

import matplotlib.pyplot as plt

#plt.boxplot(df['value'])
plt.boxplot(df_no_outliers['value'])
plt.title('Box Plot')
plt.show()
