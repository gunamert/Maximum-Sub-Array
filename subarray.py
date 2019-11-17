# Authors: Mert Günay 


import numpy as np
import sys
import matplotlib.pyplot as plt
from time import perf_counter


def maxCrossingSum (arr, l, m, h): # function for nlogn time

    sm = 0;
    left_sum = -10000

    for i in range(m, l - 1, -1):
        sm = sm + arr[i]

        if (sm > left_sum):
            left_sum = sm


    sm = 0;
    right_sum = -1000
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]

        if (sm > right_sum):
            right_sum = sm

    return left_sum + right_sum;

def maxSubArraySum (arr, l, h): # function for nlogn time

    if (l == h):
        return arr[l]

    m = (l + h) // 2
    return max(maxSubArraySum(arr, l, m),
               maxSubArraySum(arr, m + 1, h),
               maxCrossingSum(arr, l, m, h))

def timeNworks (arr):

    sum = arr[0]

    bestSum = sum

    nI = len(arr)

    for value in arr[1:]:

        random = value + sum
        sum = max(value, random)
        bestSum = max(sum , bestSum)


    return bestSum

def timeNsquare(arr):

    bestSum = -sys.maxsize -1

    fork = 0

    for start in arr:

        sum = start

        bestSum = max(sum, bestSum)

        fork = fork + 1

        for end in arr[fork:]:

            sum = sum + end
            bestSum = max(sum,bestSum)

    return bestSum

valuesx = range(1,101)

values = []

values2 = []

values3 = []

for i in range(1,101):

    arr = np.random.random_integers(-100, 100, i)

    n = len(arr)

    start = perf_counter()
    max_sum = maxSubArraySum(arr, 0, n - 1)
    stop = perf_counter()

    values.append(stop-start)

    start2 = perf_counter()
    min_sum = timeNworks(arr)
    stop2 = perf_counter()

    values2.append(stop2-start2)

    start3 = perf_counter()
    average = timeNsquare(arr)
    stop3 = perf_counter()

    values3.append(stop3-start3)

average1 = sum(values)/ 100
average2 = sum(values2)/ 100
average3 = sum(values3)/ 100



plt.plot(valuesx, values, label = "nlogn")
plt.plot(valuesx, values2, label = "n")
plt.plot(valuesx, values3, label = "n^2")

plt.gcf().text(0.13, 0.50, 'nlogn :', fontsize=9)
plt.gcf().text(0.17, 0.55, 'n :', fontsize=9)
plt.gcf().text(0.14, 0.6, 'n^2 :', fontsize=9)


plt.gcf().text(0.2, 0.50, average1, fontsize=7)
plt.gcf().text(0.2, 0.55, average2, fontsize=7)
plt.gcf().text(0.2, 0.6, average3, fontsize=7)

plt.gcf().text(0.2, 0.65, 'Average times', fontsize=10)


plt.xlabel('array size')
plt.ylabel('time')
plt.title('Maximum Subarray Sum')

plt.legend()

plt.show()


'''
arr = np.random.random_integers(-100, 100, 100)

#arr = [13,- 3,-25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

n = len(arr)

start = perf_counter()
max_sum = maxSubArraySum(arr, 0, n - 1)
stop = perf_counter()

values.append(stop - start)

start2 = perf_counter()
min_sum = timeNworks(arr)
stop2 = perf_counter()

values2.append(stop2 - start2)

start3 = perf_counter()
average = timeNsquare(arr)
stop3 = perf_counter()

values3.append(stop3 - start3)

print("Maximum contiguous sum for nlogn time average", average1)
print("Maximum contiguous sum for n time average", average2)
print("Maximum contiguous sum for n^2 time average", average3)


print("Array length: ", n,'\n')

print("Maximum contiguous sum for nlogn time ", max_sum)

print('Time: ', stop - start,'\n')

print("Maximum contiguous sum for n time ", min_sum)

print('Time: ', stop2 - start2,'\n')

print("Maximum contiguous sum for n^2 time ", average)

print('Time: ', stop3 - start3)

'''