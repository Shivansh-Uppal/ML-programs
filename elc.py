import numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.exceptions import ConvergenceWarning

train=pd.read_csv(r"C:\programming languages\AI ML\electric.csv")

x_train=train['production']
y_train=train['electricity']

plt.scatter(x_train,y_train,c='blue')

train_x=sum(x_train)
train_y=sum(y_train)

a=b=0
lr=0.0000001
m=len(x_train)
cost=(1/(2*m))*numpy.sum(numpy.power(numpy.subtract(numpy.dot(x_train,2),y_train),2))
print(cost)


#theta1 = 0.49629
#theta0 = 0.42145
theta0=1
theta1=1
while(theta0/theta1!=0):
 theta0=theta0-lr*(1/m)*numpy.sum(numpy.subtract(numpy.dot(x_train,2),y_train))
 theta1=theta1-lr*(1/m)*numpy.sum(numpy.subtract(numpy.dot(x_train,2),y_train)*x_train)

print(theta0)
print(theta1)

predicted = theta0 + theta1*x_train
plt.scatter(x_train,y_train,c='magenta')
plt.plot(x_train,predicted,'-y')
plt.show()
