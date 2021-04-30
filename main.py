import BruteForceApproach as bfa
import Kadane as kda
import DivideEtImpera as dei
import numpy as np
import matplotlib.pyplot as plt

bigArray = np.random.randint(-200, 200, size=1000)



'''Uncomment one of these to run time analysis'''
BFATime = bfa.AlgorithmRunningTimeBFA()
DEITime = dei.AlgorithmRunningTimeDivideEtImpera()
KDATime = kda.AlgorithmRunningTimeKadane()


'''Uncomment this to get the maximum subarray for random arrays'''
#bfa.BruteForce(bigArray,N)
#kda.KadaneAlgorithm(bigArray,N)
#dei.DivideEtImpera(bigArray,N)
#dei.MaxSubarray(bigArray)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['Brute Force', 'Divide and Conquer', 'Kadane']
times = [BFATime, DEITime, KDATime]
ax.bar(langs, times)
plt.show()

