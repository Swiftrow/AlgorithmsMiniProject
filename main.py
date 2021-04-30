import BruteForceApproach as bfa
import Kadane as kda
import DivideEtImpera as dei
import numpy as np

bigArray = np.random.randint(-200, 200, size=1000)
N = len(bigArray)


'''Uncomment one of these to run time analysis'''
#bfa.AlgorithmRunningTimeBFA()
#dei.AlgorithmRunningTimeDivideEtImpera()
#kda.AlgorithmRunningTimeKadane()


'''Uncomment this to get the maximum subarray for random arrays'''
#bfa.BruteForce(bigArray,N)
#kda.KadaneAlgorithm(bigArray,N)
#dei.DivideEtImpera(bigArray,N)


