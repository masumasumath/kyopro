import math
T = int(input())
L,X,Y = map(int,input().split())
Q = int(input())
for _ in range(Q):
    E = int(input())
    #角度は2Pi*omega/T
    omega = E%T
    theta = 2*math.pi*omega/T
    #y = (L/2)*math.cos(theta - math.pi/2)
    #z = -(L/2)*math.sin(theta - math.pi/2)+(L/2)
    y = -(L/2)*math.sin(theta)
    z = -(L/2)*math.cos(theta) + (L/2)

    d = ( (X**2 + abs(Y-y)**2)**0.5 ) 
    angle = 360*(math.atan2(z,d))/(2*math.pi)
    print(angle)