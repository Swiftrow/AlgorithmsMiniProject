import numpy as np
import timeit
import tracemalloc


def DivideEtImpera(array,N):
    currFromLeft = 0
    leftSum = 0
    currFromRight = 0
    rightSum = 0

    for i in range(N):
        currFromLeft += array[i]
        if currFromLeft > leftSum:
            leftSum = currFromLeft

    for i in range(N):
        currFromRight += array[i]
    if currFromRight > rightSum:
        rightSum = currFromRight

    print(rightSum+leftSum)

def AlgorithmRunningTimeDivideEtImpera():
    mySetup = '''
import numpy as np
bigArray = np.random.randint(-200, 200, size=10000)
N = len(bigArray)
        '''

    myCode = '''
def DivideEtImpera(array):
    currFromLeft = 0
    leftSum = 0
    currFromRight = 0
    rightSum = 0

    for i in range(N):
        currFromLeft += array[i]
        if currFromLeft > leftSum:
            leftSum = currFromLeft

    for i in range(N):
        currFromRight += array[i]
    if currFromRight > rightSum:
        rightSum = currFromRight

    print(rightSum+leftSum)

DivideEtImpera(bigArray)
'''
    print("Time taken for Divide and Conquer force is: " + str(timeit.timeit(setup = mySetup,stmt = myCode,number = 10)) + "seconds" )