import numpy as np
import math

cordinates = np.ones((4, 1))
cordinates[0] = float(input('Enter X coordinate: '))
cordinates[1] = float(input('Enter Y coordinate: '))
cordinates[2] = float(input('Enter Z coordinate: '))
ch = 'y'
while ch == 'y':
    a = input('Enter axis for rotation: ')
    th = float(input('Enter angle of rotation: '))
    rotation = np.zeros((4, 4))
    rotation[3][3] = 1
    if a == 'x':
        rotation[0][0] = 1;
        rotation[1][1] = math.cos(math.radians(th))
        rotation[1][2] = -math.sin(math.radians(th))
        rotation[2][1] = math.sin(math.radians(th))
        rotation[2][2] = math.cos(math.radians(th))
    if a == 'y':
        rotation[0][0] = math.cos(math.radians(th))
        rotation[0][2] = math.sin(math.radians(th))
        rotation[2][0] = -math.sin(math.radians(th))
        rotation[2][2] = math.cos(math.radians(th))
        rotation[1][1] = 1
    if a == 'z':
        rotation[0][0] = math.cos(math.radians(th))
        rotation[1][0] = math.sin(math.radians(th))
        rotation[0][1] = -math.sin(math.radians(th))
        rotation[1][1] = math.cos(math.radians(th))
        rotation[2][2] = 1
    rotation[0][3] = float(input('Input translation for x axis(0 if none): '))
    rotation[1][3] = float(input('Input translation for y axis(0 if none): '))
    rotation[2][3] = float(input('Input translation for z axis(0 if none): '))
    result = np.zeros((4, 1))
    for i in range(len(rotation)):
        for j in range(len(cordinates[0])):
            for k in range(len(cordinates)):
                result[i][j] += rotation[i][k] * cordinates[k][j]
    co = result
    ch = input("Want to add another set of rotation and translation(y/n): ")

print('Coordinates w.r.t original frame are: ')
print('X: {}'.format(float(cordinates[0])))
print('Y: {}'.format(float(cordinates[1])))
print('Z: {}'.format(float(cordinates[2])))
