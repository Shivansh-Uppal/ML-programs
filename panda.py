import pandas as pd
import matplotlib.pyplot as plt

df=pd.DataFrame({"a":[4,5,6],
                 "b":[7,8,9],
                 "c": [10,11,12]
                })
print(df)
#creating a data frame table

df=(pd.melt(df).rename(
    columns={'variable':'var','value':'val'}).query('val>=7'))
print("\n",df)
#changing columns to rows by .melt
#.query is what you want from data frame

print("\n",df['var'].value_counts())
#count no. of rows with each unique values

print("\n",len(df))
#count no. of rows in data frame

print("\n",df['val'].nunique)
#count number of distinct values in a columns

print("\n",df.describe())
#gives descriptive value of all statistical information

print("\n",df.groupby(by="var"))
#returns object by values in column named var

print("\n",df.shift(1))
#copy values and shift it by 1

print("\n",df.rank(method='dense'))
#ranks with no gaps that is replace values from 1 till end of frame

print("\n",df.rank(method='min'))
#lowest ranks in group

print("\n",df.rank(pct=True))
#ranks rescaled from [0,1]

print("\n",df.expanding())
#return object allowing summary fn to be applied cumulatively

print("\n",df.rolling(2))
#return object allowing summary fn to be applied to windows of length n

df.plot.hist()
plt.show()

df.plot.scatter(x='val',y='val')
plt.show()

