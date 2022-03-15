import statistics

entry=[]

for i in range(0,10):
    entry.append(int(input(f"enter the nth number {i+1}: ")))

summ=len(entry)
median=0

meann=sum(entry)/summ
print("mean is: ",meann)

entry.sort()
print("sorted entry is: ",entry)

if(summ%2!=0):
    median=entry[int(summ/2)]

else:
 median=(entry[int((summ-1)/2)] + entry[int((summ+1)/2)])/2
print("median is: ",median)  

def mode2(number):
    mode=max(number, key=number.count)
    return mode

mode=mode2(entry)
print("mode is: ",mode)

print("the mean through library function is: ",statistics.mean(entry))
print("the median through library function is: ",statistics.median(entry))
print("the mode through library function is: ",statistics.mode(entry))