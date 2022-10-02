import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

from numpy import array, linspace
def cast_list(test_list, data_type):
    return list(map(data_type, test_list))

def polynomial(p,x):

    y = []
    for num in x:
        deg = len(p) - 1
        for co in p:
            y.append(sum(co*pow(x[num], deg)))
            deg-=1
    return y



df = pd.read_csv('output_pauses.csv', index_col=0)
cast_list = list(df.index[0:])
cast_list.sort()

#print(cast_list)
cast_float = [float(i) for i in cast_list]
cast_int = [int(i) for i in cast_float]
#print(cast_int)

cast_int.sort()
#print(cast_int)

density = []
timerange = []

for i in range(1,300):
    timerange.append(i)


for i in range (0,max(cast_int)):
    density.append(0)
    for num in (cast_int):
        if (i == num):
            density[i]+=1



zero_index = []
for i in range(len(density)):
    if (density[i] == 0):
        zero_index.append(i)



# for i in zero_index:  //remove 0 values
#     timerange[i]=0
#
# for i in range(len(zero_index)):
#     density.remove(0)
#     timerange.remove(0)


#print(timerange)
#print(density)

#print(len(density))
#print(len(timerange))

x = range(0, len(density))
y = density

rs = [0,0,0,0,0]
deg = [2,4,6,8,10]
equations = []

for d in deg:

    fit = numpy.polyfit(x, y, d)
    equations.append(fit)

    p = numpy.poly1d(fit)
    yhat = p(x)
    ybar = numpy.sum(y)/len(y)
    ssreg = numpy.sum((yhat - ybar)**2)  # or sum([ (yihat - ybar)2 for yihat in yhat])
    sstot = numpy.sum((y - ybar)**2)  # or sum([ (yi - ybar)2 for yi in y])
    rs[int(d/2-1)] = ssreg / sstot

#print(rs)
#print(equations)

#print(equations[2])
deriv = numpy.poly1d(equations[2]).deriv()
#print(deriv)
crits = numpy.roots(deriv)

minmaxes = []
for value in crits:
    minmaxes.append(numpy.polyval(equations[2],value))


index_neg = 0
for i in range(len(crits)-1):
    if(crits[i] < 0):
        index_neg = i

index_neg+=1

crits_positive = []
new_minmaxes = []

for i in range(index_neg, len(crits)):
    crits_positive.append(crits[i])

for i in range(index_neg, len(minmaxes)):
    new_minmaxes.append(minmaxes[i])

index_neg = 0
for i in range(len(new_minmaxes)-1):
    if(new_minmaxes[i] < 0):
        index_neg = i
index_neg+=1

minmaxes_positive = []
positive_time = []

for i in range(index_neg, len(new_minmaxes)):
    minmaxes_positive.append(new_minmaxes[i])

for i in range(index_neg, len(crits_positive)):
    positive_time.append(crits_positive[i])

print("Time:")
print(positive_time)
print("Frequncy:")
print(minmaxes_positive)

maxes = []
maxes_times = []

if(minmaxes_positive[0]>minmaxes_positive[1]):
    max_index = 0
else:
    max_index = 1

#print(len(minmaxes_positive))
for i in range(max_index, len(minmaxes_positive), 2):
    maxes.append(minmaxes_positive[i])
    maxes_times.append(int(positive_time[i]))


print("Max times:")
print(maxes_times)




coeff = numpy.polyfit(timerange, density, deg = 4)

onedco = numpy.poly1d(coeff)


newx = []
newy = []
for i in range(len(density)):
    newx.append(i+1)
    calc = onedco(i+1)
    newy.append(calc)

plt.plot(newx, newy)

plt.plot(timerange,density)
plt.title('Student Pauses')
plt.xlabel('time')
plt.ylabel('frequency')
plt.show()

