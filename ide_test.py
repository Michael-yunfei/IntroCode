# This is my test file for building python IDE on Atom
# It will show how the code run on Atom with packages
# try to setup the whole environment


import pandas as pd
import numpy as np  # it looks like importing package is very slow
import matplotlib.pyplot as plt

testarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
testdata = pd.DataFrame(data=testarray, columns=['a', 'b', 'c'])


print("Hello World")


2+2

# Show plot
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
