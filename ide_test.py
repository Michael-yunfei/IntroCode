# This is my test file for building python IDE on Atom
# It will show how the code run on Atom with packages

print("Hello World")

2+2

import pandas as pd
import numpy as np  # it looks like importing package is very slow

testarray = np.array([[1,2,3], [4,5,6], [7,8,9]])

testdata = pd.DataFrame(data = testarray, columns = ['a', 'b', 'c'])
