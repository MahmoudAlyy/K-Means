import matplotlib.pyplot as plt
import pickle
import numpy as np
from mnist import MNIST
import math

mndata = MNIST('samples')
images, labels = mndata.load_training()


with open('objs.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
    original_centroids, centroids, clusters  = pickle.load(f)

k = len(centroids)
w = 5
h = math.ceil(k/w)

### PLOT ORIGINAL CENTROIDS
figc = plt.figure('original centroids', figsize=(8, 3))
for i in range(k):
    imagec = np.reshape(original_centroids[i], (28, 28))
    figc.add_subplot(w, h, i+1)
    plt.imshow(imagec)
plt.show(block =False)

### PLOT FINAL CENTROIDS
figc = plt.figure('final centroids', figsize=(8, 3))
for i in range(k):
    imagec = np.reshape(centroids[i], (28, 28))
    figc.add_subplot(w, h, i+1)
    plt.imshow(imagec)
plt.show(block = False)


dict = {i:0 for i in range(k)}
centroid_labels =[]

### ASSIGNING LABELS FOR CLUSTERS
for i in range(len(clusters)) :
    for j in range(len(clusters[i])):
        dict[labels[clusters[i][j]]] = dict[labels[clusters[i][j]]] + 1
    max = -1
    for key in dict.keys():
        if dict[key] > max:
            max = dict[key]
            t_key = key
    centroid_labels.append(t_key)

    dict = {i: 0 for i in range(k)}
        

print(centroid_labels)


### PRINT IMAGES CONTAINED IN 1ST CLUSTER
figc = plt.figure('1st Cluster images', figsize=(8, 3))
imagec = np.reshape( centroids[0] , (28, 28))
figc.add_subplot(2, 9, 5)
plt.imshow(imagec)
for i in range(9):
    imagec = np.reshape(images [ clusters[0][i] ], (28, 28))
    figc.add_subplot(2, 9, i+10)
    plt.imshow(imagec)
plt.show(block = False)


acc = 0
### CALCULATE ACCURACY
for i in range(10000):

    min = 10000000
    for ic in range(len(centroids)):
        diff = np.asarray(centroids[ic])-np.asarray(images[i])
        t_min = np.linalg.norm(diff)
        if t_min < min:
            min = t_min
            f_ic = ic

    if (centroid_labels[f_ic] == labels[i]):
        acc = acc + 1

print(acc/10000)


plt.show()
