import pygame
pygame.init()
from math import sin, cos, radians

window = pygame.display.set_mode((1400,800))
pygame.display.set_caption("3DRotation")
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
brown = (244,164,96)
grey = (220,220,220)

window.fill(white)

def _3Dto2Dconverter(x,y,z):
 fov = 256
 viewer_distance = 4
 half_screen_width = 1400 / 2
 half_screen_height = 800 / 2
 a = x * fov / (z + viewer_distance) + half_screen_width
 b = -y * fov / (z + viewer_distance) + half_screen_height
 return a,b


def x_rot(x,y,z,theta):
 A = [[1,            0,        0,           0],
      [0,   cos(theta),    -sin(theta),     0],
      [0,   sin(theta),     cos(theta),      0],
      [0,            0,        0,           1]]

 B = [[x],
      [y],
      [z], 
      [1]]
 
 result = [[0],
           [0],
           [0],
           [1]]

 # iterate through rows of A
 for i in range(len(A)):
   # iterate through columns of B
   for j in range(len(B[0])):
       # iterate through rows of B
       for k in range(len(B)):
           result[i][j] += A[i][k] * B[k][j]

 return result[0][0],result[1][0],result[2][0]

def y_rot(x,y,z,theta):
 A = [[cos(theta),           0,         sin(theta),        0],
      [0         ,           1,         0,                 0],
      [-sin(theta), cos(theta),         0,                 0],
      [0,                    0,         0,                 1]]

 B = [[x],
      [y],
      [z], 
      [1]]
 
 result = [[0],
           [0],
           [0],
           [1]]

 # iterate through rows of A
 for i in range(len(A)):
   # iterate through columns of B
   for j in range(len(B[0])):
       # iterate through rows of B
       for k in range(len(B)):
           result[i][j] += A[i][k] * B[k][j]

 return result[0][0],result[1][0],result[2][0]

def z_rot(x,y,z,theta):
 A = [[cos(theta),  -sin(theta),        0,        0],
      [sin(theta),   cos(theta),        0,        0],
      [0         ,   0         ,        1,        0],
      [0         ,   0         ,        0,        1]]

 B = [[x],
      [y],
      [z], 
      [1]]
 
 result = [[0],
           [0],
           [0],
           [1]]

 # iterate through rows of A
 for i in range(len(A)):
   # iterate through columns of B
   for j in range(len(B[0])):
       # iterate through rows of B
       for k in range(len(B)):
           result[i][j] += A[i][k] * B[k][j]

 return result[0][0],result[1][0],result[2][0]


#before
a1, b1, c1 = 3+0, 3+0, 3+0 
a2, b2, c2 = 3+3, 3+0, 3+0
a3, b3, c3 = 3+0, 3+3, 3+0
a4, b4, c4 = 3+3, 3+3, 3+0
a5, b5, c5 = 3+0, 3+0, 3+3
a6, b6, c6 = 3+3, 3+0, 3+3
a7, b7, c7 = 3+0, 3+3, 3+3
a8, b8, c8 = 3+3, 3+3, 3+3

x1, y1 = _3Dto2Dconverter(a1, b1, c1)
x2, y2 = _3Dto2Dconverter(a2, b2, c2)
x3, y3 = _3Dto2Dconverter(a3, b3, c3)
x4, y4 = _3Dto2Dconverter(a4, b4, c4)
x5, y5 = _3Dto2Dconverter(a5, b5, c5)
x6, y6 = _3Dto2Dconverter(a6, b6, c6)
x7, y7 = _3Dto2Dconverter(a7, b7, c7)
x8, y8 = _3Dto2Dconverter(a8, b8, c8)

pygame.draw.polygon(window,black,((x3,y3),(x1,y1),(x2,y2),(x4,y4)),1)
pygame.draw.polygon(window,black,((x7,y7),(x5,y5),(x6,y6),(x8,y8)),1)
pygame.draw.polygon(window,black,((x3,y3),(x7,y7),(x8,y8),(x4,y4)),1)
pygame.draw.polygon(window,black,((x1,y1),(x5,y5),(x6,y6),(x2,y2)),1)

#x-axis rotation
theta = radians(30)
a1,b1,c1 = x_rot(a1,b1,c1,theta)
a2,b2,c2 = x_rot(a2,b2,c2,theta)
a3,b3,c3 = x_rot(a3,b3,c3,theta)
a4,b4,c4 = x_rot(a4,b4,c4,theta)
a5,b5,c5 = x_rot(a5,b5,c5,theta)
a6,b6,c6 = x_rot(a6,b6,c6,theta)
a7,b7,c7 = x_rot(a7,b7,c7,theta)
a8,b8,c8 = x_rot(a8,b8,c8,theta)

x1, y1 = _3Dto2Dconverter(a1, b1, c1)
x2, y2 = _3Dto2Dconverter(a2, b2, c2)
x3, y3 = _3Dto2Dconverter(a3, b3, c3)
x4, y4 = _3Dto2Dconverter(a4, b4, c4)
x5, y5 = _3Dto2Dconverter(a5, b5, c5)
x6, y6 = _3Dto2Dconverter(a6, b6, c6)
x7, y7 = _3Dto2Dconverter(a7, b7, c7)
x8, y8 = _3Dto2Dconverter(a8, b8, c8)

pygame.draw.polygon(window,red,((x3,y3),(x1,y1),(x2,y2),(x4,y4)),1)
pygame.draw.polygon(window,red,((x7,y7),(x5,y5),(x6,y6),(x8,y8)),1)
pygame.draw.polygon(window,red,((x3,y3),(x7,y7),(x8,y8),(x4,y4)),1)
pygame.draw.polygon(window,red,((x1,y1),(x5,y5),(x6,y6),(x2,y2)),1)

#y-axis rotation
theta = radians(30)
a1,b1,c1 = y_rot(a1,b1,c1,theta)
a2,b2,c2 = y_rot(a2,b2,c2,theta)
a3,b3,c3 = y_rot(a3,b3,c3,theta)
a4,b4,c4 = y_rot(a4,b4,c4,theta)
a5,b5,c5 = y_rot(a5,b5,c5,theta)
a6,b6,c6 = y_rot(a6,b6,c6,theta)
a7,b7,c7 = y_rot(a7,b7,c7,theta)
a8,b8,c8 = y_rot(a8,b8,c8,theta)

x1, y1 = _3Dto2Dconverter(a1, b1, c1)
x2, y2 = _3Dto2Dconverter(a2, b2, c2)
x3, y3 = _3Dto2Dconverter(a3, b3, c3)
x4, y4 = _3Dto2Dconverter(a4, b4, c4)
x5, y5 = _3Dto2Dconverter(a5, b5, c5)
x6, y6 = _3Dto2Dconverter(a6, b6, c6)
x7, y7 = _3Dto2Dconverter(a7, b7, c7)
x8, y8 = _3Dto2Dconverter(a8, b8, c8)

pygame.draw.polygon(window,blue,((x3,y3),(x1,y1),(x2,y2),(x4,y4)),1)
pygame.draw.polygon(window,blue,((x7,y7),(x5,y5),(x6,y6),(x8,y8)),1)
pygame.draw.polygon(window,blue,((x3,y3),(x7,y7),(x8,y8),(x4,y4)),1)
pygame.draw.polygon(window,blue,((x1,y1),(x5,y5),(x6,y6),(x2,y2)),1)

#z-axis rotation
theta = radians(30)
a1,b1,c1 = z_rot(a1,b1,c1,theta)
a2,b2,c2 = z_rot(a2,b2,c2,theta)
a3,b3,c3 = z_rot(a3,b3,c3,theta)
a4,b4,c4 = z_rot(a4,b4,c4,theta)
a5,b5,c5 = z_rot(a5,b5,c5,theta)
a6,b6,c6 = z_rot(a6,b6,c6,theta)
a7,b7,c7 = z_rot(a7,b7,c7,theta)
a8,b8,c8 = z_rot(a8,b8,c8,theta)

x1, y1 = _3Dto2Dconverter(a1, b1, c1)
x2, y2 = _3Dto2Dconverter(a2, b2, c2)
x3, y3 = _3Dto2Dconverter(a3, b3, c3)
x4, y4 = _3Dto2Dconverter(a4, b4, c4)
x5, y5 = _3Dto2Dconverter(a5, b5, c5)
x6, y6 = _3Dto2Dconverter(a6, b6, c6)
x7, y7 = _3Dto2Dconverter(a7, b7, c7)
x8, y8 = _3Dto2Dconverter(a8, b8, c8)

pygame.draw.polygon(window,brown,((x3,y3),(x1,y1),(x2,y2),(x4,y4)),1)
pygame.draw.polygon(window,brown,((x7,y7),(x5,y5),(x6,y6),(x8,y8)),1)
pygame.draw.polygon(window,brown,((x3,y3),(x7,y7),(x8,y8),(x4,y4)),1)
pygame.draw.polygon(window,brown,((x1,y1),(x5,y5),(x6,y6),(x2,y2)),1)
while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 


 pygame.display.update()
clock.tick(100)
