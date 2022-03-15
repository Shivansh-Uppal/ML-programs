import pandas as pd
import math as mt
import matplotlib.pyplot as plt

train=pd.read_csv(r"C:\programming languages\AI ML\USA_Housing.csv")

x_train=train['Avg. Area Income']
y_train=train['Price']

plt.scatter(x_train,y_train,c='blue')
plt.xlabel('House Price')
plt.ylabel('Average Income')

def val(x_train,y_train):
  theta1=theta0=0
  a=len(x_train)
  itr=1000
  lr=0.0000000001
  for i in range(itr):
    y_pre=theta1*x_train + theta0
    P = list((y_train - y_pre))
    cost=(1/a) *sum([mt.pow(j,2) for j in P])
    cd= -(2/a) *sum(y_train-y_pre)
    md=-(2/a) *sum(x_train*(y_train-y_pre))
    theta1=theta1-lr*md
    theta0=theta0-lr*cd

  print(f"i = {i} \t theta0 = {'%.3f'%theta0} \t theta1 = {'%.3f'%theta1} \t cost = {'%.3f'%cost}")
  return theta1,theta0

plt.scatter(x_train,y_train,c='blue')
plt.xlabel('house price')
plt.ylabel('average income')

theta1,theta0=val(x_train,y_train)
predicted = theta0 + theta1*x_train
plt.scatter(x_train,y_train,c='blue')
plt.plot(x_train,predicted,'-y')
plt.xlabel('house price')
plt.ylabel('average income')
plt.show()
