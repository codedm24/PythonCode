#Machine Learning - K-nearest neighbors
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

#Create a dataset
x = [4,5,10,4,3,10,12,8,10,12]
y = [21,19,24,17,16,25,24,22,21,21]
classes = [0,0,1,0,0,1,1,0,1,1]

#visualize data
plt.scatter(x, y, c=classes)
plt.show()

#create dataset for model
data = list(zip(x,y))

print(f"Data: {data}")

model = KNeighborsClassifier(n_neighbors=5)
model.fit(data, classes)

#data for prediction
new_x = 8
new_y = 21
new_point = [(new_x, new_y)]

#predict result
predicted = model.predict(new_point)

plt.scatter(x + [new_x], y + [new_y], c = classes + [predicted[0]])
plt.text(x=new_x-1.7, y = new_y-0.7, s=f"new point, class={predicted[0]}")
plt.show()
plt.close()