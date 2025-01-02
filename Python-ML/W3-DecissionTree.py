#Machine Learning - DecissionTree
import pandas as pd
import os
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib
import matplotlib.pyplot as plt
import sys

matplotlib.use("Agg")

print(os.getcwd())
os.chdir('Python-ML')
print(os.getcwd())

#Read the data
df = pd.read_csv('data - decissiontree.csv')
#Print the first 5 rows of the dataframe.
print(df.head())
#Print the statistics of the dataframe.
print(df.describe())

#Change str values to int
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
print(df.head())

#Split the data into features and target
features = ['Age','Experience','Rank','Nationality']

X = df[features]
y = df['Go']

print(X)
print(y)

model = DecisionTreeClassifier()
model = model.fit(X, y)

tree.plot_tree(model, feature_names=features)

plt.savefig('decissiontree.png')
#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()

#predict the value

def GetVal(dict,val):
    return [k for k, v in dict.items() if v == val]

test_data = {
    'Age': [40],
    'Experience': [10],
    'Rank': [7],
    'Nationality': [1]
}

#predicted = model.predict([[40,10,7,1]])
predicted = model.predict(pd.DataFrame(test_data))
#predicted = model.predict(pd.DataFrame([[40,10,7,1]],columns=[features]))
print(f"Age:40,Experience:10,Rank:7,Nationality:USA,predicted:{GetVal(d,predicted)}")
#change the rank to 6
test_data['Rank'] = [6]
predicted = model.predict(pd.DataFrame(test_data))
#predicted = model.predict(pd.DataFrame([[40,10,6,1]],columns=[features]))
print(f"Age:40,Experience:10,Rank:6,Nationality:USA,predicted:{GetVal(d,predicted)}")