plist = []
with open("data.txt") as ipfile:
    for line in ipfile:
        words = line.split()
        plist.append(dict(zip(('x', 'y', 'clus'),
                              (float(words[1]), float(words[2]), 0))))

k = input("Enter number of clusters: ")

centroid = []

min_x = min(plist, key=lambda x: x['x'])['x']
max_x = max(plist, key=lambda x: x['x'])['x']
mean_x = (max_x - min_x) / (k+1)

min_y = min(plist, key=lambda x: x['y'])['y']
max_y = max(plist, key=lambda x: x['y'])['y']
mean_y = (max_y - min_y) / (k+1)

for i in range(1, k+1):
    centroid.append(dict(zip(('x', 'y'),
                    (min_x + (i * mean_x), min_y + (i * mean_y)))))
