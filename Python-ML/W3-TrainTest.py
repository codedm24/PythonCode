#Machine Learning - TrainTest
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

np.random.seed(2)
x = np.random.normal(3,1,100)
y = np.random.normal(150,40,100) / x

print(f'x:{x}')
print(f'y:{y})')

plt.scatter(x,y)
plt.show()

#plt.hist(x)
#plt.show()

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

#print(f'train_x:{train_x}')
#print(f'train_y:{train_y}')

#Display training set
plt.scatter(train_x,train_y)
plt.title('Training set')
plt.xlabel('train_x')
plt.ylabel('train_y')
plt.show()

#Display test set
plt.scatter(test_x,test_y)
plt.title('Test set')
plt.xlabel('test_x')
plt.ylabel('test_y')
plt.show()

model = np.poly1d(np.polyfit(train_x,train_y,4))

myline = np.linspace(min(train_x), max(train_x),100)

plt.scatter(train_x,train_y)
plt.plot(myline,model(myline))
plt.title('Polynomial regression of training dataset')
plt.show()

#R2 score
predicted_y = model(train_x)
r2score = r2_score(train_y, predicted_y)
print(f'R2 score of training dataset: {r2score}')

fig,axs = plt.subplots(2,2)

axs[0,0].scatter(train_x, train_y, color='r') 
axs[0,0].set_title('Training DataSet')
axs[0,0].set_xlabel ('train_x')
axs[0,0].set_ylabel('train_y')

axs[0,1].scatter(test_x, test_y, color='g')
axs[0,1].set_title('Test DataSet')
axs[0,1].set_xlabel('test_x')
axs[0,1].set_ylabel('test_y')

axs[1,0].scatter(train_x, train_y, color='b')
axs[1,0].plot(myline, model(myline), color='b')
axs[1,0].set_title('Polynomial regression of training dataset')
axs[1,0].set_xlabel('myline')
axs[1,0].set_ylabel('model(myline)')

fig.tight_layout()

plt.show()

print(f'time spend: 5 minutes, predicted spend:{model(5)}')