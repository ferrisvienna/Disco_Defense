#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Open source game by Ferris(FerrisofVienna) Bartak
and Paolo "Broccolimaniac" Perfahl
"""

#the next line is only needed for python2.x and not necessary for python3.x
from __future__ import print_function, division
import random
import pygame
import time as t
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
screen=pygame.display.set_mode((1024,400))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))     # fill the background white (red,green,blue)
background = background.convert()  # faster blitting
ballsurface = pygame.Surface((50,50))     # create a rectangular surface for the ball
#------- blit the surfaces on the screen to make them visible
screen.blit(background, (0,0))     # blit the background on the screen (overwriting all)
#screen.blit(ballsurface, (ballx, bally))  # blit the topleft corner of ball surface at pos (ballx, bally)
clock = pygame.time.Clock()
mainloop = True
FPS = 30 # desired framerate in frames per second. try out other values !
playtime = 0.0
#p=nothing,h=high block,i=wall,d=walkable platform,g=hazard
FORCE_OF_GRAVITY=3
ACTORSPEEDMAX=20
ACTORSPEEDMIN=10
DISCTHROWERRANGE=150
DISCMAXSPEED=100


playergroup = pygame.sprite.LayeredUpdates()
bargroup = pygame.sprite.Group()
stuffgroup = pygame.sprite.Group()
fragmentgroup = pygame.sprite.Group()
allgroup = pygame.sprite.LayeredUpdates()
projectilegroup = pygame.sprite.Group()
class Fragment(pygame.sprite.Sprite):
        """a fragment of an exploding Bird"""
        gravity = True # fragments fall down ?
        def __init__(self, pos):
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.pos = [0.0,0.0]
            self.pos[0] = pos[0]
            self.pos[1] = pos[1]
            self.image = pygame.Surface((10,10))
            self.image.set_colorkey((0,0,0)) # black transparent
            pygame.draw.circle(self.image, (random.randint(1,255),0,0), (5,5), 
                                            random.randint(2,5))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos #if you forget this line the sprite sit in the topleft corner
            self.lifetime = 1 + random.random()*5 # max 6 seconds
            self.time = 0.0
            self.fragmentmaxspeed = 200  # try out other factors !
            self.dx = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)
            self.dy = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)
            
        def update(self, seconds):
            self.time += seconds
            if self.time > self.lifetime:
                self.kill() 
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds
            if Fragment.gravity:
                self.dy += FORCE_OF_GRAVITY # gravity suck fragments down
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
            
            
class DiscProjectile(pygame.sprite.Sprite):
        """a projectile of a Disc gun"""
        gravity = False # fragments fall down ?
        image=pygame.image.load("disc.png")
        def __init__(self, pos=(random.randint(640,1024),random.randint(100,300)),
                     dx= random.randint(-DISCMAXSPEED,DISCMAXSPEED),
                     dy=random.randint(-DISCMAXSPEED,DISCMAXSPEED)):
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.pos = [0.0,0.0]
            self.pos[0] = pos[0]
            self.pos[1] = pos[1]
            self.image = DiscProjectile.image
            self.image.set_colorkey((255,0,182)) # black transparent
            #pygame.draw.circle(self.image, (random.randint(1,255),0,0), (5,5), 
                                            #random.randint(2,5))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos #if you forget this line the sprite sit in the topleft corner
            self.lifetime = 1 + random.random()*5 # max 6 seconds
            self.time = 0.0
            #self.fragmentmaxspeed = 200  # try out other factors !
            self.dx = dx
            self.dy = dy
            
        def update(self, seconds):
            self.time += seconds
            if self.time > self.lifetime:
                self.kill() 
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds
            #if Fragment.gravity:
             #   self.dy += FORCE_OF_GRAVITY # gravity suck fragments down
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
            
            
class Healthbar(pygame.sprite.Sprite):
    """shows a bar with the hitpoints of a Bird sprite"""
    def __init__(self, boss):
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.boss = boss
        self.image = pygame.Surface((self.boss.rect.width,7))
        self.image.set_colorkey((3,3,3)) # black transparent
        pygame.draw.rect(self.image, (1,1,1), (0,0,self.boss.rect.width,7),1)
        self.rect = self.image.get_rect()
        self.oldpercent = 0
        self.bossnumber = self.boss.number # the unique number (name)
        
    def update(self, time):
        self.percent = self.boss.hitpoints / self.boss.hitpointsfull * 1.0
        if self.percent != self.oldpercent:
            pygame.draw.rect(self.image, (77,77,77), (1,1,self.boss.rect.width-2,5)) # fill black
            pygame.draw.rect(self.image, (222,22,2), (1,1,
                int(self.boss.rect.width * self.percent),5),0) # fill green
        self.oldpercent = self.percent
        self.rect.centerx = self.boss.rect.centerx
        self.rect.centery = self.boss.rect.centery - self.boss.rect.height /2 - 10
        #check if boss is still alive if not
        if self.boss.hitpoints<1:
            self.kill()
         #   self.kill() # kill the hitbar
            
            
            
class Monster(pygame.sprite.Sprite):
        """Generic Monster"""
        images=[]  # list of all images
        # not necessary:
        monsters = {} # a dictionary of all monsters
        number = 0
  
        def __init__(self, level, startpos=screen.get_rect().center, hitpointsfull=600):
  
      
            pygame.sprite.Sprite.__init__(self, self.groups ) #call parent class. NEVER FORGET !
            self.z = 0 # animationsnummer
            self.duration = 0.0 # how long was the current animation visible in seconds
            self.level=level
            self.nomove = False
            #startpos=(0,screen.get_rect().center[1])
            startpos=(0,random.randint(100,350))
            self.pos = [float(startpos[0]),float (startpos[1])] # dummy values to create a list
            #self.pos[0] = float(startpos[0]) # float for more precise calculation
            #self.pos[1] = float(startpos[1])
           # self.area = screen.get_rect()
            self.area = pygame.Rect(0,100,1024,300)
            self.image = Monster.images[self.z]
            self.hitpointsfull = float(hitpointsfull) # maximal hitpoints , float makes decimal
            self.hitpoints = float(hitpointsfull) # actual hitpoints
            self.rect = self.image.get_rect()
            self.radius = max(self.rect.width, self.rect.height) / 2.0
            self.dx= random.random()*10+20
            self.dy= random.randint(-70,70)
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0) #kackabraun
            #self.newspeed()
            #self.cleanstatus()
            #self.catched = False
            #self.crashing = False
            #--- not necessary:
            self.number = Monster.number # get my personal Birdnumber
            Monster.number+= 1           # increase the number for next Bird
            Monster.monsters[self.number] = self # 
            Healthbar(self)
            
            
        #def newspeed(self):
            # new birdspeed, but not 0
            #speedrandom = random.choice([-1,1]) # flip a coin
            #self.dx = random.random() * ACTORSPEEDMAX * speedrandom + speedrandom 
            #self.dy = random.random() * ACTORSPEEDMAX * speedrandom + speedrandom 
        def getChar(self):
            #Tile = 50*50
            x=int(self.pos[0]/50)
            y=int(self.pos[1]/50)+0# correction value to get the tile under the feet doesn't actually work :\
            try:
                char=self.level[y][x]
            except:
                char="?"
            return char        
        
        
        
        def kill(self):
            """because i want to do some special effects (sound, dictionary etc.)
            before killing the Bird sprite i have to write my own kill(self)
            function and finally call pygame.sprite.Sprite.kill(self) 
            to do the 'real' killing"""
            #cry.play()
            #print Bird.birds, "..."
            for _ in range(random.randint(3,15)):
                Fragment(self.pos)
            Monster.monsters[self.number] = None # kill Bird in sprite dictionary
            
            pygame.sprite.Sprite.kill(self) # kill the actual Bird 

        
        def update(self, seconds):
            # friction make birds slower
            #if abs(self.dx) > ACTORSPEEDMIN and abs(self.dy) > BIRDSPEEDMIN:10.000
             #   self.dx *= FRICTION
              #  self.dy *= FRICTION
            # spped limit
            #if abs(self.dx) > BIRDSPEEDMAX:
             #   self.dx = BIRDSPEEDMAX * self.dx / self.dx
            #if abs(self.dy) > BIRDSPEEDMAX:
             #   self.dy = BIRDSPEEDMAX * self.dy / self.dy
            # new position
            #------ check if lava
            #Animation#
            # 6 bilder sind in Monster.images []
            self.duration += seconds
            if self.duration > 0.5:
                self.duration= 0
                self.z  +=1
                if self.z >= len(Monster.images):
                    self.z = 0
                self.image=Monster.images[self.z]
            
            #-------
            if self.getChar()=="g":
                self.hitpoints-=1
            if self.getChar()=="?":
                self.hitpoints=0
            if self.getChar()=="h":
                self.nomove = True
            self.dy=random.randint(-10, 10)
            self.dx= 25#random.randint(10,10)
            if self.nomove:
                self.dx = 0
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds
            # -- check if Bird out of screen
            if not self.area.contains(self.rect):
                #self.crashing = True # change colour later
                # --- compare self.rect and area.rect
                if self.pos[0] + self.rect.width/2 > self.area.right:
                    self.pos[0] = self.area.right - self.rect.width/2
                if self.pos[0] - self.rect.width/2 < self.area.left:
                    self.pos[0] = self.area.left + self.rect.width/2
                if self.pos[1] + self.rect.height/2 > self.area.bottom:
                    self.pos[1] = self.area.bottom - self.rect.height/2
                if self.pos[1] - self.rect.height/2 < self.area.top:
                    self.pos[1] = self.area.top + self.rect.height/2
                #self.newspeed() # calculate a new direction
            #--- calculate actual image: crasing, catched, both, nothing ?
            #self.image = Bird.image[self.crashing + self.catched*2]
            #--- calculate new position on screen -----
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
            #--- loose hitpoins
            #if self.crashing:
             #self.hitpoints -=1
            #--- check if still alive if not, then let a juicy fart off
            if self.hitpoints <= 0:
                self.kill()

monstergroup=pygame.sprite.Group()
allgroup=pygame.sprite.LayeredUpdates()
bargroup = pygame.sprite.Group()
fragmentgroup = pygame.sprite.Group()

DiscProjectile.groups = allgroup, projectilegroup
Monster.groups =  allgroup, monstergroup
Fragment.groups=allgroup, fragmentgroup
Healthbar.groups=allgroup, bargroup

Monster.images.append(pygame.image.load("discodudel.png")) # 0
Monster.images[0].set_colorkey((255,0,182))
Monster.images.append(pygame.image.load("discodudel4.png")) # 1
Monster.images[1].set_colorkey((255,0,182))
Monster.images.append(pygame.image.load("discodudel.png")) # 2
Monster.images[2].set_colorkey((255,0,182))
Monster.images.append(pygame.image.load("discodudel2.png")) # 3
Monster.images[3].set_colorkey((255,0,182))
Monster.images.append(pygame.image.load("discodudel3.png")) # 4
Monster.images[4].set_colorkey((255,0,182))
Monster.images.append(pygame.image.load("discodudel2.png")) # 5
Monster.images[5].set_colorkey((255,0,182))
Monster.images[0].convert_alpha() 
#paolo=Monster(level) 

h= [pygame.image.load("h0.png"),pygame.image.load("h1.png"),pygame.image.load("h2.png"),pygame.image.load("h3.png"),    pygame.image.load("h4.png"),pygame.image.load("h5.png")]
h[0].set_colorkey((255,0,182))
h[1].set_colorkey((255,0,182))
h[2].set_colorkey((255,0,182))
h[3].set_colorkey((255,0,182))
h[4].set_colorkey((255,0,182))
h[5].set_colorkey((255,0,182))
p= pygame.image.load("p.png")
p.set_colorkey((255,0,182))

i= [pygame.image.load("i0.png"),pygame.image.load("i1.png"),pygame.image.load("i2.png"),pygame.image.load("i3.png"),    pygame.image.load("i4.png"),pygame.image.load("i5.png")]
i[1].set_colorkey((255,0,182))
i[2].set_colorkey((255,0,182))
i[3].set_colorkey((255,0,182))
i[4].set_colorkey((255,0,182))
i[5].set_colorkey((255,0,182))
i[0].set_colorkey((255,0,182))
d= [pygame.image.load("d0.png"),pygame.image.load("d1.png"),pygame.image.load("d2.png"),pygame.image.load("d3.png"),    pygame.image.load("d4.png"),pygame.image.load("d5.png")]
g= [pygame.image.load("g0.png"),pygame.image.load("g1.png"),pygame.image.load("g2.png"),pygame.image.load("g3.png"),    pygame.image.load("g4.png"),pygame.image.load("g5.png")]
v= [pygame.image.load("discodiscgunf.png"),pygame.image.load("discodiscgunl.png"),pygame.image.load("discodiscgunb.png"),pygame.image.load("discodiscgunr.png"),pygame.image.load("discodiscgunr.png"),pygame.image.load("discodiscgunr.png")]
k= [pygame.image.load("konfettif.png"),pygame.image.load("konfettir.png"),pygame.image.load("konfettib.png"),pygame.image.load("konfettil.png"),    pygame.image.load("konfettil.png"),pygame.image.load("konfettil.png")]
w= [pygame.image.load("discogunf.png"),pygame.image.load("discogunr.png"),pygame.image.load("discogunb.png"),pygame.image.load("discogunl.png"),    pygame.image.load("discogunl.png"),pygame.image.load("discogunl.png")]
w[1].set_colorkey((255,0,182))
w[2].set_colorkey((255,0,182))
w[3].set_colorkey((255,0,182))
w[4].set_colorkey((255,0,182))
w[5].set_colorkey((255,0,182))
w[0].set_colorkey((255,0,182))
anim=0
level=["hppppppppppppwpppppp",
       "ihpppppppppihipppppp",
       "iddddddddddhivdddddd",
       "dddddvdddddddddddddd",
       "ddddvvdgwggddvkddddd",
       "dddddvdddddddggddddd",
       "ddddgddddddddddddddd",
       "gggggggdgggdggdggggg"]
legende={"h":h[anim],#towertop
         "p":p,#nothing
         "i":i[anim],#dirt
         "g":g[anim],#lava
         "d":d[anim], #grass
         "v":v[anim], #discodiscgun
         "w":w[anim], #discogun
         "k":k[anim] #konfettigun
         }
x=0
y=0
fleckanim=[]
for zeile in level:
     for fleck in zeile:
           fleckanim.append(0)
           background.blit(legende[fleck],(x,y))
           x+=50
     y+=50
     x=0







spawnrate=0.02
Monster(level)
millis = 0
while mainloop:
    milliseconds = clock.tick(FPS) # do not go faster than this frame rate and that
    seconds=milliseconds /1000.0
    playtime += milliseconds / 1000.0
    millis += milliseconds
    
    if random.random()<spawnrate:
        Monster(level)
    
    if millis > 500: # jede halbe sekunde neue animation
        millis=0
        z=0
        x=0
        y=0
        for zeile in level:
            for fleck in zeile:
                if fleck == "d" and fleckanim[z] == 0:      
                    if random.random() < 0.005:
                        fleckanim[z] += 1
                elif fleck == "g" and fleckanim[z] == 0:
                    if random.random() < 0.5:
                        fleckanim[z] += 1
                else:
                    fleckanim[z] += 1 # normaler fleck
                if fleck == "v":
                    targetlist=[]
                    for target in monstergroup:
                        #pass # pythagoras distanz ausrechnen
                        #ziel wird gesucht reichweite getestet
                        #zufälliges ziel wird abgeschossen
                        distx=abs(target.pos[0]-x)
                        disty=abs(target.pos[0]-y)
                        dist=(distx**2+disty**2)**0.5
                        if dist<DISCTHROWERRANGE:
                            targetlist.append(target)
                    if len(targetlist)>0:
                        target=random.choice(targetlist)
                        print("taget gefunden{}".format(target.pos) )
                        #schuss
                        DiscProjectile((x,y),DISCMAXSPEED*(target.pos[0]-x)/dist,DISCMAXSPEED*(target.pos[1]-y)/dist)
                    else:
                        print("No target found")
                if fleckanim[z] > 5:
                    fleckanim[z] = 0       
                z+=1
                x+=50
            y+=50
            x=0
        x=0
        y=0
        z=0
        for zeile in level:
             for fleck in zeile:
                legende={"h":h[anim],#towertop
                        "p":p,#nothing
                        "i":i[anim],#dirt
                        "g":g[anim],#lava
                        "d":d[anim], #grass
                        "v":v[anim], #discodiscgun
                        "w":w[anim], #discogun
                        "k":k[anim]  #konfetti
                        }
                z+=1
                background.blit(legende[fleck],(x,y))
                x+=50
             y+=50
             x=0
             

    # blitten
    screen.blit(background, (0,0))    
    allgroup.draw(screen)
    
    
    # ----- event handler -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # pygame windows closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # user pressed ESC
            if event.key==pygame.K_F1:
                for px in range (0,240):
                    DiscProjectile(pos=(random.randint(540,1024),random.randint(100,400)))
    pygame.display.set_caption("Frame rate: %.2f frames per second. Playtime: %.2f seconds" % (clock.get_fps(),playtime))
    pygame.display.flip()          # flip the screen like in a flipbook
    #sprite collide_________________________________________________________
    for mymonster in monstergroup:
         crashgroup = pygame.sprite.spritecollide(mymonster, projectilegroup, False)  # true würde disc löschen
         for myprojectile in crashgroup:
               mymonster.hitpoints-=0.50 # test for collision with bullet
                                                
                        
    #allgroup.clear(screen, background)
    allgroup.update(seconds)
    allgroup.draw(screen)
    
    
    
print( "this 'game' was played for %.2f seconds" % playtime)
