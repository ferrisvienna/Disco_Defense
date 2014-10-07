#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
003_static_blit.py
static blitting and drawing
url: http://thepythongamebook.com/en:part2:pygame:step003
author: horst.jens@spielend-programmieren.at
licence: gpl, see http://www.gnu.org/licenses/gpl.html

Blitting a surface on a static position
Drawing a filled circle into ballsurface.
Blitting this surface once.
introducing pygame draw methods
The ball's rectangular surface is black because the background
color of the ball's surface was never defined nor filled."""


#the next line is only needed for python2.x and not necessary for python3.x
from __future__ import print_function, division

import pygame
pygame.init()
screen=pygame.display.set_mode((1024,624))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))     # fill the background white (red,green,blue)
background = background.convert()  # faster blitting
ballsurface = pygame.Surface((50,50))     # create a rectangular surface for the ball
#pygame.draw.circle(Surface, color, pos, radius, width=0) # from pygame.org documentation
pygame.draw.circle(ballsurface, (0,0,255), (25,25),25) # draw blue filled circle on ball surface
ballsurface = ballsurface.convert()              # faster blitting
ballx = 320
bally = 240
#------- try out some pygame draw functions --------
# pygame.draw.rect(Surface, color, Rect, width=0): return Rect
pygame.draw.rect(background, (0,255,0), (50,50,100,25)) # rect: (x1, y1, width, height)
# pygame.draw.circle(Surface, color, pos, radius, width=0): return Rect
pygame.draw.circle(background, (0,200,0), (200,50), 35)
# pygame.draw.polygon(Surface, color, pointlist, width=0): return Rect
pygame.draw.polygon(background, (0,180,0), ((250,100),(300,0),(350,50)))
# pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=1): return Rect
pygame.draw.arc(background, (0,150,0),(400,10,150,100), 0, 3.14) # radiant instead of grad
#------- blit the surfaces on the screen to make them visible
screen.blit(background, (0,0))     # blit the background on the screen (overwriting all)
screen.blit(ballsurface, (ballx, bally))  # blit the topleft corner of ball surface at pos (ballx, bally)
clock = pygame.time.Clock()
mainloop = True
FPS = 30 # desired framerate in frames per second. try out other values !
playtime = 0.0
#p=nothing,h=high block,i=wall,d=walkable platform,g=hazard



h= pygame.image.load("h.png")
h.set_colorkey((255,0,182))
p= pygame.image.load("p.png")
p.set_colorkey((255,0,182))
i= pygame.image.load("i.png")
i.set_colorkey((255,0,182))
d= pygame.image.load("d.png")
g= pygame.image.load("g.png")

level=["hpppppppppppphpppppp",
       "ihpppppppppphipppppp",
       "iihddhdddddhiidddddd",
       "dddddddddddddddddddd",
       "dddddddgdggddddddddd",
       "ddddddhddddddggddddd",
       "ddddgddddddddddddddd",
       "ddddddiddddddddddddd"]
legende={"h":h,
         "p":p,
         "i":i,
         "g":g,
         "d":d} 
x=0
y=0
for zeile in level:
     for fleck in zeile:
           
           background.blit(legende[fleck],(x,y))
           x+=50
     y+=50
     x=0
print("paolo ist geil"*1000)







while mainloop:
    milliseconds = clock.tick(FPS) # do not go faster than this frame rate
    playtime += milliseconds / 1000.0
    # blitten
    screen.blit(background, (0,0))    
    
    
    
    # ----- event handler -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # user pressed ESC
    pygame.display.set_caption("Frame rate: %.2f frames per second. Playtime: %.2f seconds" % (clock.get_fps(),playtime))
    pygame.display.flip()          # flip the screen like in a flipbook
print( "this 'game' was played for %.2f seconds" % playtime)
