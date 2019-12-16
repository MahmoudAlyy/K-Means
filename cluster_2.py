import matplotlib.pyplot as plt
import pickle
import numpy as np
from mnist import MNIST

mndata = MNIST('Desktop\ENG\Term 7\Ai\samples')
images, labels = mndata.load_training()


k = 10
w=5
h = k/w

with open('objs.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
#with open('len_data=1,000 & k=10 & itera=2,000.pkl', 'rb') as f:  # Python 3: open(..., 'rb')

#with open('len_data=60,000 & k=10 & itera=20.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
#with open('len_data=60,000 & k=10 & itera=20 #2.pkl', 'rb') as f:  # Python 3: open(..., 'rb')

#with open('len_data=60,000 & k=15 & itera=20.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
#with open('len_data=60,000 & k=25 & itera=20.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
#with open('len_data=60,000 & k=30 & itera=20.pkl', 'rb') as f:  # Python 3: open(..., 'rb')


    original_centroids, centroids, clusters  = pickle.load(f)



figc = plt.figure('original centroids', figsize=(8, 3))
for i in range(k):
    imagec = np.reshape(original_centroids[i], (28, 28))
    figc.add_subplot(w, h, i+1)
    plt.imshow(imagec)
plt.show(block =False)


figc = plt.figure('final centroids', figsize=(8, 3))
for i in range(k):
    imagec = np.reshape(centroids[i], (28, 28))
    figc.add_subplot(w, h, i+1)
    plt.imshow(imagec)
plt.show(block = False)


dict = {i:0 for i in range(k)}
centroid_labels =[]

for i in range(len(clusters)) :
    for j in range(len(clusters[i])):
        dict[labels[clusters[i][j]]] = dict[labels[clusters[i][j]]] + 1
    max = -1
    for key in dict.keys():
        if dict[key] > max:
            max = dict[key]
            t_key = key
    centroid_labels.append(t_key)


    #print(dict)
    dict = {i: 0 for i in range(k)}
        

print(centroid_labels)

figc = plt.figure('1st Cluster images', figsize=(8, 3))
imagec = np.reshape( centroids[0] , (28, 28))
figc.add_subplot(2, 9, 5)
plt.imshow(imagec)
for i in range(9):
    imagec = np.reshape(images [ clusters[0][i] ], (28, 28))
    figc.add_subplot(2, 9, i+10)
    plt.imshow(imagec)
plt.show(block = False)


if __name__ == "__main__":
    plt.show()


