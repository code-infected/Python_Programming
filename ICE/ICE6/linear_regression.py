import matplotlib.pyplot as plt
import numpy as np


x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([1,3,2,5,7,8,8,9,10,12])

m_X = np.mean(x)
m_Y = np.mean(y)

B1 = np.sum((x - m_X) * (y - m_Y)) / np.sum(np.square(x - m_X))

B0 = m_Y - B1 * m_X

Xs = np.reshape(x, (len(x), 1))  # converting to matrix of n X 1
Ys = np.reshape(y, (len(y), 1))
plt.scatter(x, y, color='yellow')
z = [B1*i + B0 for i in x]
plt.plot(x, z)
plt.title(B1)
plt.show()