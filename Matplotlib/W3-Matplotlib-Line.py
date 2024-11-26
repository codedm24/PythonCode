#Matplotlib line

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

#marker line style dotted
# plt.plot(ypoints,linestyle='dotted')
# plt.show()

#marker linestyle dashed
# plt.plot(ypoints,'or',linestyle='dashed')
# plt.show()

#marker linestyle shortform
# plt.plot(ypoints,'or',ls='-.')
# plt.show()

#marker line color
# plt.plot(ypoints,'or',ls='-.', color='g')
# plt.show()

#marker line color shortform
# plt.plot(ypoints,'or',ls='-', c='#4CAF50')
# plt.show()

#marker line width
# plt.plot(ypoints,'or',ls='-', c='b', linewidth='20.5')
# plt.show()

#multiple plot call for multiple lines
ypoints2= np.array([6, 2, 7, 11])

# plt.plot(ypoints)
# plt.plot(ypoints2)
# plt.show()

#single plot call for multiple lines
x1 = np.array([0,1,2,3])
x2 = np.array([0,1,2,3])
plt.plot(x1,ypoints,x2,ypoints2)
plt.show()

