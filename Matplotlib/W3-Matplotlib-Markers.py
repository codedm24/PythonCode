#Matplotlib Markers
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

#marker style 1
# plt.plot(ypoints, marker='o')
# plt.show()

#marker style 2
# plt.plot(ypoints, marker='*')
# plt.show()

#marker has several more styles

#marker fmt
# plt.plot(ypoints,'o:r')
# plt.show()

#marker hyphen dot
# plt.plot(ypoints,'o-.',)
# plt.show()

#marker hyphe hypen color green
# plt.plot(ypoints,'o--g')
# plt.show()

#marker font size
# plt.plot(ypoints,'o--g', ms = 20)
# plt.show()

#marker edge color
# plt.plot(ypoints,'o-b', ms = 20, mec = 'r')
# plt.show()

#marker face color
# plt.plot(ypoints,'o-b', ms = 20, mec = 'r', mfc='y')
# plt.show()

#marker hexadecimal color
plt.plot(ypoints,'o-b', ms = 20, mec = '#4CAF50', mfc='#4CAF50')
plt.show()