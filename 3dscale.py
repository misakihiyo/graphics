import pygame
pygame.init()
from math import sin, cos, radians

window = pygame.display.set_mode((1300,800))

clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
brown = (244,164,96)
grey = (220,220,220)

window.fill(white)

def _3Dto2D(x,y,z):
 fov = 256
 viewer_distance = 4
 half_screen_width = 1300 / 2
 half_screen_height = 800 / 2
 a = x * fov / (z + viewer_distance) + half_screen_width
 b = -y * fov / (z + viewer_distance) + half_screen_height
 return a,b


def scaling(x,y,z, sx, sy, sz):
 A = [[sx, 0,  0,  0],
      [0,  sy, 0,  0],
      [0,  0,  sz, 0],
      [0,  0,  0,  1]]

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
a1, b1, c1 = 2+0, 2+0, 2+0 
a2, b2, c2 = 2+1, 2+0, 2+0
a3, b3, c3 = 2+0, 2+1, 2+0
a4, b4, c4 = 2+1, 2+1, 2+0
a5, b5, c5 = 2+0, 2+0, 2+1
a6, b6, c6 = 2+1, 2+0, 2+1
a7, b7, c7 = 2+0, 2+1, 2+1
a8, b8, c8 = 2+1, 2+1, 2+1

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
sx,sy,sz = 2, 2, 2
a1,b1,c1 = scaling(a1,b1,c1,sx,sy,sz)
a2,b2,c2 = scaling(a2,b2,c2,sx,sy,sz)
a3,b3,c3 = scaling(a3,b3,c3,sx,sy,sz)
a4,b4,c4 = scaling(a4,b4,c4,sx,sy,sz)
a5,b5,c5 = scaling(a5,b5,c5,sx,sy,sz)
a6,b6,c6 = scaling(a6,b6,c6,sx,sy,sz)
a7,b7,c7 = scaling(a7,b7,c7,sx,sy,sz)
a8,b8,c8 = scaling(a8,b8,c8,sx,sy,sz)

x1, y1 = _3Dto2D(a1, b1, c1)
x2, y2 = _3Dto2D(a2, b2, c2)
x3, y3 = _3Dto2D(a3, b3, c3)
x4, y4 = _3Dto2D(a4, b4, c4)
x5, y5 = _3Dto2D(a5, b5, c5)
x6, y6 = _3Dto2D(a6, b6, c6)
x7, y7 = _3Dto2D(a7, b7, c7)
x8, y8 = _3Dto2D(a8, b8, c8)

pygame.draw.polygon(window,blue,((x3,y3),(x1,y1),(x2,y2),(x4,y4)),1)
pygame.draw.polygon(window,blue,((x7,y7),(x5,y5),(x6,y6),(x8,y8)),1)
pygame.draw.polygon(window,blue,((x3,y3),(x7,y7),(x8,y8),(x4,y4)),1)
pygame.draw.polygon(window,blue,((x1,y1),(x5,y5),(x6,y6),(x2,y2)),1)


while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 


 pygame.display.update()
clock.tick(100)
