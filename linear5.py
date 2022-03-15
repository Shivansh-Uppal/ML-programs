import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc("font", size=14)

sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

data=pd.read_csv(r"https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv",header=0)
data=data.dropna()

print(data.shape)
print(list(data.columns))
data.head()

data['education'].unique()

data['education']=np.where(data['education'] =='basic.9y', 'Basic', data['education'])
data['education']=np.where(data['education'] =='basic.6y', 'Basic', data['education'])
data['education']=np.where(data['education'] =='basic.4y', 'Basic', data['education'])

data['y'].value_counts()

sns.countplot(x='y',data=data,palette='hls')

plt.show()
plt.savefig('count_plot')

count_no_sub = len(data[data['y']==0])
count_sub = len(data[data['y']==1])
pct_of_no_sub = count_no_sub/(count_no_sub+count_sub)

print("percentage of no subscription is", pct_of_no_sub*100)
pct_of_sub = count_sub/(count_no_sub+count_sub)

print("percentage of subscription", pct_of_sub*100)
print(data.groupby('y').mean())
data.groupby('y').mean()

y = data['y']
x = data['duration']

sns.regplot(x=x,y=y,data=data,logistic=True,ci=None)
plt.show()