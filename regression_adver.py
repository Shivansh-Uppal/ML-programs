import pandas as pd
import numpy as np
import matplotlib.pyplot as py


df = pd.read_csv(r"C:\programming languages\AI ML\advertising.csv")

y_train = df[['Sales']]
x_train = df[['TV']]

theta0 = 0.013
theta1 = 0.03

predicted = theta0 + theta1*x_train+4.630

py.scatter(x_train,y_train,c='magenta')

py.plot(x_train,predicted,'-y')

py.xlabel('TV SELL')

py.ylabel('SALES')

py.show()
