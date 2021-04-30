
import timeit
import tracemalloc

#print(bigArray)

def BruteForce(array):
    maxInt = 0
    N = len(array)
    for i in range(N):
        currInt = 0
        for j in range(i,N):
            currInt += array[j]
            if currInt > maxInt:
                maxInt = currInt
    return maxInt




#tracemalloc.start()


def AlgorithmRunningTimeBFA():
    mySetup = '''
import numpy as np
bigArray = np.random.randint(-200, 200, size=10000)
N = len(bigArray)
'''
    myCode = '''
def BruteForce(array):
    maxInt = 0
    for i in range(N):
        currInt = 0
        for j in range(N):
            currInt += array[j]
            if currInt > maxInt:
                maxInt = currInt
    print(maxInt)

BruteForce(bigArray)
'''
    result = timeit.timeit(setup=mySetup, stmt=myCode, number=10)
    print("Time taken for Brute Force is: {0} seconds".format(result))
    return result

#current, peak = tracemalloc.get_traced_memory()
#print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
#tracemalloc.stop()