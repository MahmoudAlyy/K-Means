import matplotlib.pyplot as plt
from mnist import MNIST
import numpy as np
import random
import copy
import pickle

yes = {'yes', 'y', 'ye', ''}
no = {'no', 'n'}

print("Do u want to use defaults values (y/n) ? (k=10, iteration=20, length of data=5,000)")

choice = input().lower()
if choice in yes:
    k = 10
    iteration = 20
    len_data =  5000
elif choice in no:

    k = int( input("Enter k: ") )
    iteration = int(input("Enter number of iteration: ") )
    len_data = int (input("Enter length of data used for trainning (MAX 60,000): ") )


mndata = MNIST('samples')
images, labels = mndata.load_training()

images = images[0:len_data]

clusters = {i: [] for i in range(k)}
old_clusters = {i: [] for i in range(k)}
centroids = []


### ASSIGNING CENTROIDS
figc = plt.figure(num='centroids',figsize=(8, 3))
for i in range(k):
    index = random.randint(0, len_data-1)
    centroids.append(images[index])

original_centroids = copy.deepcopy(centroids)

for itt in range(iteration):

     ### reset cluster
    clusters = {i: [] for i in range(k)}

    print("iteration "+str(itt+1)+"/"+str(iteration))

    old_clusters = copy.deepcopy(clusters) ### deep copy to check for conversion
    
    for i in range (len_data):   
        min = 10000000
        for ic in range(len(centroids)):
            diff = np.asarray(centroids[ic])-np.asarray(images[i])
            t_min = np.linalg.norm(diff)
            #t_min = helper.diff(centroids[ic],images[i])
            if t_min < min :
                min = t_min
                f_ic = ic
        clusters[f_ic].append(i)

    if old_clusters == clusters :
        
        print("converged")
        break
    
    ### UPDATING CENTROIDS
    for i in range(k):
        centroids[i] = np.mean([images[index] for index in clusters[i]] , axis=0 , dtype=int)
        #centroids[i] = helper.sum( [images[index] for index in clusters[i]] )

### Save original_centroids,centroids,clusters
with open('objs.pkl', 'wb') as f:
        pickle.dump( [original_centroids,centroids,clusters], f)
