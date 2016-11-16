import numpy as np
import random
import matplotlib.pyplot as plt


def euclidean_dist(pointA, pointB):
    """Calculates Euclidean distance between two points and returns float"""

    sum = 0.0
    for a, b in zip(pointA, pointB):
        diff = a-b
        diff = diff ** 2
        sum = sum + diff

    return sum ** 0.5


def assign_cluster(pointL, centroidL, k):
    clust_indexl = [0] * 20
    clusterl = [[] for i in range(k)]
    for pindex, point in enumerate(plist):

        min_dist = euclidean_dist(centroid[0], point)
        clust_indexl[pindex] = 0

        for index, center in enumerate(centroid[1:]):

            if (euclidean_dist(center, point) < min_dist):
                min_dist = euclidean_dist(center, point)
                clust_indexl[pindex] = index + 1
        clusterl[clust_indexl[pindex]].append(point)
    return clusterl, clust_indexl


plist = []
with open("data.txt") as ipfile:
    for line in ipfile:
        words = line.split()
        plist.append([float(words[1]), float(words[2])])

k = input("Enter number of clusters: ")

# Calculate min, max and mean of first component for initialising centroids.
min_x = min(plist, key=lambda x: x[0])[0]
max_x = max(plist, key=lambda x: x[0])[0]
mean_x = (max_x - min_x) / (k+1)

# Calculate min, max and mean of second component for initialising centroids.
min_y = min(plist, key=lambda x: x[1])[1]
max_y = max(plist, key=lambda x: x[1])[1]
mean_y = (max_y - min_y) / (k+1)

centroid = []

# A different initialization approach--
# for i in range(1, k+1):
# centroid.append([min_x + (i * mean_x), min_y + (i * mean_y)])

# Initialize Centroids
rand = random.sample(range(20), k)
for a in rand:
    centroid.append(plist[a])

cluster, cluster_index = assign_cluster(plist, centroid, k)

for i in range(500):
    for index, clust in enumerate(cluster):
            centroid[index] = np.mean(clust, 0).tolist()

    cluster, cluster_index = assign_cluster(plist, centroid, k)

print "Cluster Index of points:", cluster_index

x = []
y = []
for pt in plist:
    x.append(pt[0])
    y.append(pt[1])

fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(x, y, c=cluster_index, s=50)
plt.show()
