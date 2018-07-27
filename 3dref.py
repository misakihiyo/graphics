import pygame
pygame.init()
from math import sin, cos, radians

window = pygame.display.set_mode((640,480))
pygame.display.set_caption("3D Translation")
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

window.fill(white)

def _3Dto2D(x,y,z):
 fov = 256
 viewer_distance = 4
 half_screen_width = 640 / 2
 half_screen_height = 480 / 2
 a = x * fov / (z + viewer_distance) + half_screen_width
 b = -y * fov / (z + viewer_distance) + half_screen_height
 return a,b


def ref_x(x,y,z):
 A = [[-1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]

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

def ref_y(x,y,z):
 A = [[1, 0, 0, 0],
      [0, -1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]

 B = [[x],
      [y],
      [z], 
      [1]]
 
 result = [[0],
           [0],
           [0],
           [1]]
           
def ref_z(x,y,z):
 A = [[1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, -1, 0],
      [0, 0, 0, 1]]

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

x1, y1 = _3Dto2D(a1, b1, c1)
x2, y2 = _3Dto2D(a2, b2, c2)
x3, y3 = _3Dto2D(a3, b3, c3)
x4, y4 = _3Dto2D(a4, b4, c4)
x5, y5 = _3Dto2D(a5, b5, c5)
x6, y6 = _3Dto2D(a6, b6, c6)
x7, y7 = _3Dto2D(a7, b7, c7)
x8, y8 = _3Dto2D(a8, b8, c8)

pygame.draw.polygon(window,black,((x3,y3),(x1,y1),(x2,y2),(x4,y4)),1)
pygame.draw.polygon(window,black,((x7,y7),(x5,y5),(x6,y6),(x8,y8)),1)
pygame.draw.polygon(window,black,((x3,y3),(x7,y7),(x8,y8),(x4,y4)),1)
pygame.draw.polygon(window,black,((x1,y1),(x5,y5),(x6,y6),(x2,y2)),1)

#after

a1a,b1a,c1a = ref_x(a1,b1,c1)
a2a,b2a,c2a = ref_x(a2,b2,c2)
a3a,b3a,c3a = ref_x(a3,b3,c3)
a4a,b4a,c4a = ref_x(a3,b3,c3)
a5a,b5a,c5a = ref_x(a4,b4,c4)
a6a,b6a,c6a = ref_x(a5,b5,c5)
a7a,b7a,c7a = ref_x(a6,b6,c6)
a8a,b8a,c8a = ref_x(a7,b7,c7)

x1, y1 = _3Dto2D(a1a, b1a, c1a)
x2, y2 = _3Dto2D(a2a, b2a, c2a)
x3, y3 = _3Dto2D(a3a, b3a, c3a)
x4, y4 = _3Dto2D(a4a, b4a, c4a)
x5, y5 = _3Dto2D(a5a, b5a, c5a)
x6, y6 = _3Dto2D(a6a, b6a, c6a)
x7, y7 = _3Dto2D(a7a, b7a, c7a)
x8, y8 = _3Dto2D(a8a, b8a, c8a)

pygame.draw.polygon(window,red,((x3,y3),(x1,y1),(x2,y2),(x4,y4)),1)
pygame.draw.polygon(window,red,((x7,y7),(x5,y5),(x6,y6),(x8,y8)),1)
pygame.draw.polygon(window,red,((x3,y3),(x7,y7),(x8,y8),(x4,y4)),1)
pygame.draw.polygon(window,red,((x1,y1),(x5,y5),(x6,y6),(x2,y2)),1)

a1,b1,c1 = ref_y(a1,b1,c1)
a2,b2,c2 = ref_y(a2,b2,c2)
a3,b3,c3 = ref_y(a3,b3,c3)
a4,b4,c4 = ref_y(a3,b3,c3)
a5,b5,c5 = ref_y(a4,b4,c4)
a6,b6,c6 = ref_y(a5,b5,c5)
a7,b7,c7 = ref_y(a6,b6,c6)
a8,b8,c8 = ref_y(a7,b7,c7)

x1, y1 = _3Dto2D(a1, b1, c1)
x2, y2 = _3Dto2D(a2, b2, c2)
x3, y3 = _3Dto2D(a3, b3, c3)
x4, y4 = _3Dto2D(a4, b4, c4)
x5, y5 = _3Dto2D(a5, b5, c5)
x6, y6 = _3Dto2D(a6, b6, c6)
x7, y7 = _3Dto2D(a7, b7, c7)
x8, y8 = _3Dto2D(a8, b8, c8)

pygame.draw.polygon(window,red,((x3,y3),(x1,y1),(x2,y2),(x4,y4)),1)
pygame.draw.polygon(window,red,((x7,y7),(x5,y5),(x6,y6),(x8,y8)),1)
pygame.draw.polygon(window,red,((x3,y3),(x7,y7),(x8,y8),(x4,y4)),1)
pygame.draw.polygon(window,red,((x1,y1),(x5,y5),(x6,y6),(x2,y2)),1)

a1,b1,c1 = ref_z(a1,b1,c1)
a2,b2,c2 = ref_z(a2,b2,c2)
a3,b3,c3 = ref_z(a3,b3,c3)
a4,b4,c4 = ref_z(a3,b3,c3)
a5,b5,c5 = ref_z(a4,b4,c4)
a6,b6,c6 = ref_z(a5,b5,c5)
a7,b7,c7 = ref_z(a6,b6,c6)
a8,b8,c8 = ref_z(a7,b7,c7)


x1, y1 = _3Dto2D(a1, b1, c1)
x2, y2 = _3Dto2D(a2, b2, c2)
x3, y3 = _3Dto2D(a3, b3, c3)
x4, y4 = _3Dto2D(a4, b4, c4)
x5, y5 = _3Dto2D(a5, b5, c5)
x6, y6 = _3Dto2D(a6, b6, c6)
x7, y7 = _3Dto2D(a7, b7, c7)
x8, y8 = _3Dto2D(a8, b8, c8)

pygame.draw.polygon(window,red,((x3,y3),(x1,y1),(x2,y2),(x4,y4)),1)
pygame.draw.polygon(window,red,((x7,y7),(x5,y5),(x6,y6),(x8,y8)),1)
pygame.draw.polygon(window,red,((x3,y3),(x7,y7),(x8,y8),(x4,y4)),1)
pygame.draw.polygon(window,red,((x1,y1),(x5,y5),(x6,y6),(x2,y2)),1)



while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 


 pygame.display.update()
clock.tick(100)
