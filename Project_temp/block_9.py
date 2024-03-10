import numpy as np

def dist_list(*vectors):

    
    list_with_dist = []
    
    if len(vectors) == 2:
        
        list_with_dist.append(np.linalg.norm(vectors[0] - vectors[1]))
         
    else:
        for i in range(1, len(vectors)-1):
            list_with_dist.append(np.linalg.norm(vectors[0] - vectors[i]))
        list_with_dist.append(dist_list(vectors[1:len(vectors)]))
    
    return list_with_dist

def min_max_dist(*vectors):
    
    list_with_dist = dist_list(*vectors)
    
    return list_with_dist


vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])

min_max_dist(vec1, vec2, vec3)
# (5.196152422706632, 10.392304845413264)
