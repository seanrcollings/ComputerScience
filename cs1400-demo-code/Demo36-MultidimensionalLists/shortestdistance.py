from random import randint
def main():
    #create list of random points
    points = []
    for i in range(20):
        points.append([randint(-50, 50), randint(-50, 50)])


    print(points)

    p1, p2 = nearestPoints(points)

    print("The nearest points are (" + str(points[p1][0]) + ", " + str(points[p1][1]) + ") and ("
          + str(points[p2][0]) + ", " + str(points[p2][1]) + ")")


def nearestPoints(points):
    p1, p2 = 0, 1
    minDistance = distance(points[p1][0], points[p1][1], points[p2][0], points[p2][1])

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            tmpDist = distance(points[i][0], points[i][1], points[j][0], points[j][1])

            if tmpDist < minDistance:
                minDistance = tmpDist
                p1, p2 = i, j

    return p1, p2



def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


main()