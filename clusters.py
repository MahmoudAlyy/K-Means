import matplotlib.pyplot as plt
from mnist import MNIST
import numpy as np
import random
import helper
import copy
import pickle



####################
k = 10
iteration = 100
len_data =  1000
####################

mndata = MNIST('Desktop\ENG\Term 7\Ai\samples')
images, labels = mndata.load_training()

images = images[0:len_data]

###################
#list of centroid of actaul point
#dict : keys 0-9 , list value
#################


#PRINT DATA
#figt = plt.figure(num='data',figsize=(8, 5))
#for i in range(len_data):
 #   imaget = np.reshape(images[i], (28, 28))
  #  figt.add_subplot(2, 10, i+1)
   # plt.gca().set_title(i)

    
    #plt.imshow(imaget)
#plt.show(block=False)

### ERROR GRAPH
#error_list = []



clusters = {i: [] for i in range(k)}
old_clusters = {i: [] for i in range(k)}


centroids = []

### ASSIGNING CENTROIDS AND DISPLAYING THEM
figc = plt.figure(num='centroids',figsize=(8, 3))
for i in range(k):
    #index = random.randint(0, len_data-1)
    for c in range(len(labels)) :
        if (labels[c] == i):
            break
    
    centroids.append(images[c])
   # imagec = np.reshape(images[index], (28, 28))
    #figc.add_subplot(2, 5, i+1)
    #plt.imshow(imagec)

#plt.show(block=False)

original_centroids = copy.deepcopy(centroids)


for itt in range(iteration):

  #  error = 0

     ### reset cluster
    clusters = {i: [] for i in range(k)}

    print("iteration "+str(itt+1)+"/"+str(iteration))

    old_clusters = copy.deepcopy(clusters) ### deep copy to check for conversion
    
    for i in range (len_data):   
        min = 10000000
        for ic in range(len(centroids)):
            t_min = helper.diff(centroids[ic],images[i])
            if t_min < min :
                min = t_min
                f_ic = ic
       # error = error + min
        clusters[f_ic].append(i)

    #error_list.append(error)

    if old_clusters == clusters :
        
        print("converged")
        break
    
    ### UPDATING CENTROIDS
    for i in range(k):
        centroids[i] = helper.sum( [images[index] for index in clusters[i]] )

### Save original_centroids,centroids,clusters
with open('objs.pkl', 'wb') as f:
        pickle.dump( [original_centroids,centroids,clusters], f)





### printing  centroids
#figc = plt.figure('final centroids', figsize=(8, 3))
#for i in range(k):
 #   imagec = np.reshape(centroids[i], (28, 28))
  #  figc.add_subplot(2, 5, i+1)
   # plt.imshow(imagec)
#plt.show()


#plt.show()
    
