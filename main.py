import BruteForceApproach as bfa
import Kadane as kda
import DivideEtImpera as dei
import numpy as np


bigArray = np.random.randint(-200, 200, size=1000)



'''Uncomment one of these to run time analysis'''
#BFATime = bfa.AlgorithmRunningTimeBFA()
DEITime = dei.AlgorithmRunningTimeDivideEtImpera()
KDATime = kda.AlgorithmRunningTimeKadane()


'''Uncomment this to get the maximum subarray for random arrays'''
#bfa.BruteForce(bigArray,N)
#kda.KadaneAlgorithm(bigArray,N)
#dei.DivideEtImpera(bigArray,N)
#print(dei.MaxSubarray(bigArray))



