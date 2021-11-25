#!/usr/bin/env python
# coding: utf-8

# ### Import Modules

# In[1]:


import math
import numpy as np


# ### Given information

# In[2]:


# Points
points = np.array([[5.9, 3.2], [4.6, 2.9], [6.2, 2.8], [4.7, 3.2], [5.5, 4.2], [5.0, 3.0], [4.9, 3.1], [6.7, 3.1], [5.1, 3.8], [6.0, 3.0]])

# Centroids
x1, y1 = 6.2, 3.2
x2, y2 = 6.6, 3.7
x3, y3 = 6.5, 3.0

# Clusters
cluster1 = []
cluster2 = []
cluster3 = []


# ### Define Euclidean Distance Function

# In[3]:


def eucDistance(a, b):
    d1 = math.sqrt((a - x1)**2 + (b - y1)**2)
    d2 = math.sqrt((a - x2)**2 + (b - y2)**2)
    d3 = math.sqrt((a - x3)**2 + (b - y3)**2)
    
    minDistance = min(d1, d2, d3)
    
    if minDistance == d1:
        cluster1.append([a, b])
    elif minDistance == d2:
        cluster2.append([a, b])
    else:
        cluster3.append([a, b])
        
for i, j in points:
    eucDistance(i, j)

print('Cluster 1:', cluster1)
print('Cluster 2:', cluster2)
print('Cluster 3:', cluster3)


# ### Centroid of Cluster 1 after 1st Iteration

# In[4]:


def findCentroid(cluster, n):
    sumX = 0
    sumY = 0
    
    if n == 0:
        centX = 0
        centY = 0
        cent = [centX, centY]
        return cent
    
    for i, j in cluster:
        sumX = sumX + i
        sumY = sumY + j
    
    centX = round(sumX / n, 3)
    centY = round(sumY / n, 3)
    cent = [centX, centY]
    return cent

cent1 = findCentroid(cluster1, len(cluster1))
cent2 = findCentroid(cluster2, len(cluster2))
cent3 = findCentroid(cluster3, len(cluster3))

print('Centroid of Cluster 1 after 1st iteration:', cent1)
print(cent2, cent3)


# ### Centroid of Cluster 2 after 2nd iteration

# In[5]:


# Clear Clusters for the next iteration
cluster1 = []
cluster2 = []
cluster3 = []

# Initialise Centroid Coordinates
x1, y1 = cent1[0], cent1[1]
x2, y2 = cent2[0], cent2[1]
x3, y3 = cent3[0], cent3[1]

# 2nd Iteration
for i, j in points:
    eucDistance(i, j)
    
print('Cluster 1:', cluster1)
print('Cluster 2:', cluster2)
print('Cluster 3:', cluster3)

# Centroid of Cluster2 after 2nd Iteration
cent1 = findCentroid(cluster1, len(cluster1))
cent2 = findCentroid(cluster2, len(cluster2))
cent3 = findCentroid(cluster3, len(cluster3))

print("\nCentroid of Cluster 2 after 2nd iteration:", cent2)
print(cent1, cent3)


# ### Iteration 3

# In[6]:


# Clear Clusters for the next iteration
cluster1 = []
cluster2 = []
cluster3 = []

# Initialise Centroid Coordinates
x1, y1 = cent1[0], cent1[1]
x2, y2 = cent2[0], cent2[1]
x3, y3 = cent3[0], cent3[1]

print(x1,y1,x2,y2,x3,y3)

# 3rd Iteration
for i, j in points:
    eucDistance(i, j)
    
print('Cluster 1:', cluster1)
print('Cluster 2:', cluster2)
print('Cluster 3:', cluster3)

# Centroid of Cluster after 3rd Iteration
cent1 = findCentroid(cluster1, len(cluster1))
cent2 = findCentroid(cluster2, len(cluster2))
cent3 = findCentroid(cluster3, len(cluster3))

print("\nCentroid of Cluster 2 after 3rd iteration:", cent2)
print(cent1, cent3)


# In[ ]:




