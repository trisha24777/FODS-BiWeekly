''' Program to find Euclidean distance between two coordinates '''
import math
x1, y1 = map(float, input("Enter first coordinate (x1 y1): ").split())
x2, y2 = map(float, input("Enter second coordinate (x2 y2): ").split())
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Euclidean Distance:", distance)
