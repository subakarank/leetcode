'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''
import math
def k_closet(points: list, k: int):
    distances = [(math.sqrt(x**2 + y**2), (x,y)) for x, y in points]
    distances.sort()
    closest_points = [point for _, point in distances[:k]]
    return closest_points


points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 1
print(f"Input: [[1, 3], [-2, 2], [5, 8], [0, 1]] : output is {k_closet(points, k )}")

