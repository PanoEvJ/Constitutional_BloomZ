import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("toxicity.csv")
df = pd.DataFrame(data)
print(df.head())

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

X = list(reversed(X))
Y = list(reversed(Y))

X[0] = 'GPT-2'
X[1] = 'GPT-2 mild RLAIF'
X[2] = 'GPT-2 severe RLAIF'

plt.bar(X, Y, color='g')
plt.title("mean toxicity")

plt.show()

Y = list(df.iloc[:, 2])
Y = list(reversed(Y))

plt.bar(X, Y, color='b')
plt.title("std toxicity")

plt.show()