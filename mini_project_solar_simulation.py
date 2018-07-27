
import pygame as g
import sys
import math


g.font.init()
screen = g.display.set_mode((1300, 700))
background = (0, 0, 0)#(59, 69, 84)
labelFont = g.font.Font(None, 15)
center = (int(1300/2), int(700/2))

class CelestialBody:
    def __init__(self, name,  width, color, speed, rad, orbit, orbit_around):
        self.name = name
        self.width = width
        self.color = color
        self.speed = speed
        self.orbit = orbit
        self.orbit_around = orbit_around
        self.position = [orbit_around[0]+orbit,orbit_around[1]]
        self.rad = rad  # todo static rad for all(pos)/ recalculate pos based on rad
       

    def draw(self):
        g.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.width)
		#g.draw.circle(screen, [255,255,255], self.orbit_around ,  self.width)
		
    def move(self):
        self.rad += self.speed
        
        self.position[0] = self.orbit_around[0] + self.orbit * math.cos(self.rad)
        self.position[1] = self.orbit_around[1]+ self.orbit * math.sin(self.rad)

def round_list(l):
    return [int(round(i, 4)) for i in l]


Sun = CelestialBody("Sun", 40, (255, 255, 255), 0, 0, 0, center)
Mercury = CelestialBody("Mercury", 8, (198, 158, 13), 0.0005, 0, 80, center)
Venus = CelestialBody("Venus", 9, (198, 158, 13), 0.001, 0, 100, center)
Earth = CelestialBody("Earth", 12, (41, 118, 242), 0.001, 0, 150, center)
Mars = CelestialBody("Mars", 9, (244, 176, 66), 0.0009, 0, 200, center)
Jupiter = CelestialBody("Jupiter", 23, (255, 193, 50), 0.0005, 0, 250, center)
Saturn = CelestialBody("Saturn", 20, (255, 210, 137), 0.0004, 0, 300, center)
Uranus = CelestialBody("Uranus", 18, (79, 171, 221), 0.0003, 0, 350, center)
Neptune = CelestialBody("Neptune", 15, (1, 124, 191), 0.0002, 0, 400, center)
Moon = CelestialBody("Moon", 1, (158, 158, 158), 0.005, 0, 50, Earth.position)
Enceladus = CelestialBody("Enceladus",1,(240,240,240),0.001,0,30,Saturn.position)
labels = True

while True:
    screen.fill(background)
    Sun.draw()
    Earth.move()
    Moon.orbit_around = Earth.position
    Moon.move()
    Moon.draw()
    Earth.draw()
    Mercury.move()
    Mercury.draw()
    Venus.move()
    Venus.draw()
    Mars.move()
    Mars.draw()
    Jupiter.move()
    Jupiter.draw()
    Saturn.move()
    Saturn.draw()
    Uranus.move()
    Uranus.draw()
    Neptune.move()
    Neptune.draw()
  
    g.draw.circle(screen, [84,84,84], center, 80, 1)
    g.draw.circle(screen, [84,84,84], center, 100, 1)
    g.draw.circle(screen, [84,84,84], center, 150, 1)
    g.draw.circle(screen, [84,84,84], center, 200, 1)
    g.draw.circle(screen, [84,84,84], center,250, 1)
    g.draw.circle(screen, [84,84,84], center, 300, 1)
    g.draw.circle(screen, [84,84,84], center, 350, 1)
    g.draw.circle(screen, [84,84,84], center, 400, 1)
  
    
    g.display.update()

    # Close
    for event in g.event.get():
        if event.type == g.QUIT:
            g.quit()
sys.exit()
