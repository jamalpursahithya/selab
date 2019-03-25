import numpy as np
from matplotlib import pyplot as plt

# Straight line
# You can change the parameters here to get various straight lines
m = np.random.random() * 10
c = np.random.random() * 10

x = np.linspace(1, 100, 120)
y = m * x + c

plt.axis((0, 100, 0, 100))
plt.plot(x, y, 'r.')
plt.show()


# Let's add some noise to the data
y += 10 * np.random.randn(len(y))

# Initialize weights
w = 5 * np.random.random()
b = 5 * np.random.random()

# Augmented vector
x_ = np.asarray(list(zip(x, np.ones_like(x))))
beta = np.asarray([w, b])

deltas = np.ones_like(x)
plt.axis((-10, 100, -10, 100))
plt.plot(x, y, 'r.')
plt.axis((-10, 100, -10, 100))
plt.plot(x, w*x, 'b-')
plt.show()

# vector notation, Why this shape?
deltas = np.ones((2,))
lr = 0.0001

# If you want randomness, use the following lines 
# w = 5 * np.random.random()
# b = 5 * np.random.random()
# beta = np.asarray([w, b])

beta = np.asarray([2, 1])
x_ = np.asarray(list(zip(x, np.ones_like(x))))

while(np.abs(np.mean(deltas)) > 0.0001):
    deltas[0] = lr * np.mean((y - np.dot(x_, beta)) * x_[:, 0])
    deltas[1] = lr * np.mean(y - np.dot(x_, beta))
    beta += deltas
    print(deltas)
    plt.axis((-10, 100, -10, 100))
    plt.plot(x, y, 'r.')
    plt.axis((-10, 100, -10, 100))
    plt.plot(x, np.dot(x_, beta), 'b-')
    plt.show()
