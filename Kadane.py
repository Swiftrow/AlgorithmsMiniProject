import numpy as np
import timeit
import tracemalloc


def KadaneAlgorithm(array):
    maxInt = 0
    currentMaxInt = 0
    N = len(array)
    for i in range(N):
        currentMaxInt += array[i]
        if currentMaxInt < 0:
            currentMaxInt = 0
        if maxInt < currentMaxInt:
            maxInt = currentMaxInt
    print(maxInt)

def AlgorithmRunningTimeKadane():
    mySetup = '''
import numpy as np
bigArray = np.random.randint(-200, 200, size=10000)
N = len(bigArray)
'''

    myCode = '''
def KadaneAlgorithm(array):
    maxInt = 0
    currentMaxInt = 0
    for i in range(N):
        currentMaxInt += array[i]
        if currentMaxInt < 0:
            currentMaxInt = 0
        if maxInt < currentMaxInt:
            maxInt = currentMaxInt
    print(maxInt)


KadaneAlgorithm(bigArray)
'''
    result = timeit.timeit(setup=mySetup, stmt=myCode, number=10)
    print("Time taken for Kadane is: {0} seconds".format(result))
    return result