"""
Collision Course 
Problem Description
On a busy road, multiple cars are passing by. A simulation is run to see what happens if brakes fail for all cars on the road. The only way for them to be safe is if they don’t collide and pass by each other. The goal is to identify whether any of the given cars would collide or pass by each other safely around a Roundabout. Think of this as a reference point O ( Origin with coordinates (0, 0) ), but instead of going around it, cars pass through it.

Considering that each car is moving in a straight line towards the origin with individual uniform speed. Cars will continue to travel in that same straight line even after crossing origin. Calculate the number of collisions that will happen in such a scenario.

Note: Calculate collisions only at origin. Ignore the other collisions. Assume that each car continues on its respective path even after the collision without change of direction or speed for an infinite distance.

Given an array car[] which contains the co-ordinates and their speed for each element. Find the total number of collisions at origin.

Example:




Input: car[] = {(5 12 1), (16 63 5), (-10 24 2), (7 24 2), (-24 7 2)}
Output: 4
Explanation:
Let the 5 cars be A, B, C, D, and E respectively.
4 Collisions are as follows –
A & B, A & C, B & C, D & E
"""
C = int(input())

D = {}
collision = 0

for i in range(C):
    x,y,speed=list(map(int,input().split()))

    sq_time=(x**2+y**2)/(speed**2)
    # print(sq_time)

    if(D.get(sq_time)==None):
        D[sq_time]=1
    else:
        D[sq_time]=D[sq_time]+1

# print(D)
for keys in D:
    if(D[keys]!=1):
        collision=collision+(D[keys]*(D[keys]-1))/2
print(int(collision))