# Clustering Algorithm

#Two initial clusters with centroids c1 and c2
initial_centroids ={'c1': (1,0), 'c2':(1,1)}


# dataset with data points
dataset = [(0,0),(1,0),(1,1),(0,1),(-1,0)]



# This function calculates the Distance.
def calculate_Distance(x1, y1, x2, y2):
    distance = (float(((x2-x1)**2)+((y2-y1)**2))**0.5)
    return distance

#  This Function computes the mean of the set of points in each cluster.

def mean(c):
    sum_x=0
    sum_y=0
    for point in c:
         sum_x += point[0]
         sum_y += point[1]
    mean_x = (sum_x)/len(c)
    mean_y = (sum_y)/len(c)
    return (mean_x,mean_y)

new_centroids = {}
# This Function computes the  distance  between  each  data  point  in  the  dataset  and  the  centroids  in  both clusters.
def point_Distance(centroid):
    c1 = []
    c2 = []
    global dataset
   
 
    for point in dataset:
    
        d1=calculate_Distance(point[0],point[1],initial_centroids['c1'][0],initial_centroids['c1'][1])
    
        d2 = calculate_Distance(point[0],point[1],initial_centroids['c2'][0],initial_centroids['c2'][1])
        if d1 < d2:
            c1.append(point)
        else:
            c2.append(point)
        
    new_c1 = mean(c1)
    new_c2=mean(c2)
    
    new_centroids['c1'] = new_c1
    new_centroids['c2'] = new_c2

    return new_centroids

new_centroid1 = point_Distance(initial_centroids)
print("new centroids after iteration 1: ",new_centroid1)
new_centroid2 = point_Distance(new_centroids)
print("new centroids after iteration 2: ",new_centroid2)




     







    









   
   


    
