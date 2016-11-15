
def euclidean_dist(pointA, pointB):
    """Calculates Euclidean distance between two points and returns float"""

    sum = 0.0
    for a, b in zip(pointA, pointB):
        diff = a-b
        diff = diff ** 2
        sum = sum + diff

    return sum ** 0.5


plist = []
with open("data.txt") as ipfile:
    for line in ipfile:
        words = line.split()
        plist.append((float(words[1]), float(words[2]), 0))

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

for i in range(1, k+1):
    centroid.append((min_x + (i * mean_x), min_y + (i * mean_y)))

print euclidean_dist(plist[0], plist[1])
