import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from numpy import array, linspace
#from sklearn.neighbors.kde import KernelDensity
#from matplotlib.pyplot import plot


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


with open("Time stamps twin peak.txt", "r") as filestream:
    with open("answers.txt", "w") as filestreamtwo:
        for line in filestream:
            currentline = line.split(",")
            print(currentline)
            cast_float = cast_list(currentline, float)
            cast_int = cast_list(cast_float, int)
            print(cast_int)


cast_int.sort()
print(cast_int)

density = []
timerange = []

for i in range(1,300):
    timerange.append(i)


for i in range (0,max(cast_int)):
    density.append(0)
    for num in (cast_int):
        if (i == num):
            density[i]+=1



#for i in density:
#    if (density[i] == 0):
#        temp = time_range[:i]+[0]+time_range[i+1:]
#        time_range = temp
zero_index = []
for i in range(len(density)):
    if (density[i] == 0):
        zero_index.append(i)



# for i in zero_index:
#     timerange[i]=0
#
# for i in range(len(zero_index)):
#     density.remove(0)
#     timerange.remove(0)


print(timerange)
print(density)

print(len(density))
print(len(timerange))

coeff = numpy.polyfit(timerange, density, deg = 4)

y = numpy.poly1d(coeff)


newx = []
newy = []
for i in range(len(density)):
    newx.append(i+1)
    calc = y(i+1)
    newy.append(calc)

plt.plot(newx, newy)

plt.plot(timerange,density)
plt.title('Student Pauses')
plt.xlabel('time')
plt.ylabel('frequency')
plt.show()

