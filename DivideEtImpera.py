import numpy as np
import timeit
import tracemalloc


def DivideEtImpera(array):
    currFromLeft = 0
    leftSum = 0
    currFromRight = 0
    rightSum = 0
    N = len(array)

    for i in range(int((N-1)/2) + 1):
        currFromLeft += array[i]
        if currFromLeft > leftSum:
            leftSum = currFromLeft

    for i in range(int((N-1)/2) + 1, N):
        currFromRight += array[i]
        if currFromRight > rightSum:
            rightSum = currFromRight

    return rightSum+leftSum


def MaxSubarray(array):
    start = 0
    end = len(array) - 1
    if len(array) == 1:
        return array[start]
    elif len(array) == 0:
        return 0
    middle = int((start+end)/2)
    return max(MaxSubarray(array[start:middle]), MaxSubarray(array[middle+1:end]), DivideEtImpera(array))





def AlgorithmRunningTimeDivideEtImpera():
    mySetup = '''
import numpy as np
bigArray = np.random.randint(-200, 200, size=10000)
N = len(bigArray)
        '''

    myCode = '''
def MaxSubarray(array):
    start = 0
    end = len(array) - 1
    if len(array) == 1:
        return array[start]
    elif len(array) == 0:
        return 0
    middle = int((start+end)/2)
    return max(MaxSubarray(array[start:middle]), MaxSubarray(array[middle+1:end]), DivideEtImpera(array))    
    
def DivideEtImpera(array):
    currFromLeft = 0
    leftSum = 0
    currFromRight = 0
    rightSum = 0
    N = len(array)

    for i in range(int((N-1)/2) + 1):
        currFromLeft += array[i]
        if currFromLeft > leftSum:
            leftSum = currFromLeft

    for i in range(int((N-1)/2) + 1, N):
        currFromRight += array[i]
        if currFromRight > rightSum:
            rightSum = currFromRight

    return rightSum+leftSum
MaxSubarray(bigArray)
'''
    result = timeit.timeit(setup=mySetup, stmt=myCode, number=10)
    print("Time taken for Divide and Conquer force is: {0} seconds".format(result))
    return result