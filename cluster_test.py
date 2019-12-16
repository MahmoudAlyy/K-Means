from mnist import MNIST
import cluster_2
import helper
import matplotlib.pyplot as plt

mndata = MNIST('Desktop\ENG\Term 7\Ai\samples')
images, labels = mndata.load_testing()

#    original_centroids, centroids, clusters  , centroid_labels

#print(cluster_2.centroid_labels)

acc = 0


for i in range (10000):

    min = 10000000
    for ic in range(len(cluster_2.centroids)):
        t_min = helper.diff(cluster_2.centroids[ic], images[i])
        if t_min < min:
            min = t_min
            f_ic = ic

    if (cluster_2.centroid_labels[f_ic] == labels[i]):
        acc = acc + 1
    #clusters[f_ic].append(i)



    

print(acc/10000)

plt.show()
