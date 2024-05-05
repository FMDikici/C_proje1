import math

def euclideanDistance(point1, point2):
    x1,y1=point1
    x2,y2=point2
    return math.sqrt((x1-x2)**2 +(y1-y2)**2)

points=[(15,26),(92,18),(10,8),(9,7),(44,62),(80,10)]

distances=[]
for i in range(len(points)):
    for j in range(i+1,len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

print("Minimum Distance :",min(distances))        