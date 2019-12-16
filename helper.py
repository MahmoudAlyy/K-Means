import matplotlib.pyplot as plt
from mnist import MNIST
import numpy as np
import random

# old 54 sec data = 600 , itt =20 
# diff 33 sec
# diff & sum 18 sec

def diff(x, y):

    n = np.asarray(x)-np.asarray(y)

    return np.linalg.norm(n)

   # error = 0
    #for i in range(784):
     #   error = error + abs(x[i]-y[i])

    #return error



def sum(cluster):

    #print(np.mean(cluster, axis=0, dtype=int))
          
    #if len(cluster) == 1:
     #   return cluster
    return (np.mean(cluster, axis=0, dtype=int))

    summed = [0] * 784
    #print(cluster)
    if len(cluster) == 0 :
        return -1
    for item in cluster:
        for i in range(784):
            summed[i] = summed[i] + item[i]
    for i in range(784):
        summed[i] = int(summed[i] / len(cluster))
        if(summed[i]>300):
            print("55555555555555555555555555555555555555555555555555555555555555555555555")


    return summed
