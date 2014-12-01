#004BB1#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Disco Defense
Open source game by Ferris(FerrisofVienna) Bartak
and Paolo "Broccolimaniac" Perfahl
using python3 and pygame
"""

#the next line is only needed for python2.x and not necessary for python3.x
from __future__ import print_function, division
import random
import pygame
import time as t

class Game(object):
    LIVES=20
    FORCE_OF_GRAVITY=3
    ACTORSPEEDMAX=20
    ACTORSPEEDMIN=10
    DISCTHROWERRANGE=150
    DISCMAXSPEED=100
    SPAWNRATE =1.05
    SECURITYSPAWNRATE = 0.005
#rebalance
    def __init__(self):

        Monster.images.append(pygame.image.load("data/discodudel.png")) # 0
        Monster.images[0].set_colorkey((255,0,182))
        Monster.images.append(pygame.image.load("data/discodudel4.png")) # 1
        Monster.images[1].set_colorkey((255,0,182))
        Monster.images.append(pygame.image.load("data/discodudel.png")) # 2
        Monster.images[2].set_colorkey((255,0,182))
        Monster.images.append(pygame.image.load("data/discodudel2.png")) # 3
        Monster.images[3].set_colorkey((255,0,182))
        Monster.images.append(pygame.image.load("data/discodudel3.png")) # 4
        Monster.images[4].set_colorkey((255,0,182))
        Monster.images.append(pygame.image.load("data/discodudel2.png")) # 5
        Monster.images[5].set_colorkey((255,0,182))
        Monster.images[0].convert_alpha()
        Monster.images[1].convert_alpha()
        Monster.images[2].convert_alpha()
        Monster.images[3].convert_alpha()
        Monster.images[4].convert_alpha()
        Monster.images[5].convert_alpha()
        
        
        #Monster_rare.images.append(pygame.image.load("data/walkll1.png")) # 0
        #Monster_rare.images[0].set_colorkey((255,0,182))
        #Monster_rare.images.append(pygame.image.load("data/walkll2.png")) # 1
        #Monster_rare.images[1].set_colorkey((255,0,182))
        #Monster1.images.append(pygame.image.load("data/walkll3.png")) # 2
        #Monster1.images[2].set_colorkey((255,0,182))
        #Monster1.images.append(pygame.image.load("data/walkll1.png")) # 3
        #Monster1.images[3].set_colorkey((255,0,182))
        #Monster1.images.append(pygame.image.load("data/walkll2.png")) # 4
        #Monster1.images[4].set_colorkey((255,0,182))
        #Monster1.images.append(pygame.image.load("data/walkll3.png")) # 5
        #Monster1.images[5].set_colorkey((255,0,182))
        #Monster1.images[0].convert_alpha()
        #Monster1.images[1].convert_alpha()
        #Monster1.images[2].convert_alpha()
        #Monster1.images[3].convert_alpha()
        #Monster1.images[4].convert_alpha()
        #Monster1.images[5].convert_alpha()
        
        Security.images.append(pygame.image.load("data/securityw1.png")) # 0
        Security.images[0].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securityw2.png")) # 1
        Security.images[1].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securityw1.png")) # 2
        Security.images[2].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securityw2.png")) # 3
        Security.images[3].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securityw1.png")) # 4
        Security.images[4].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securityw2.png")) # 5
        Security.images[5].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securityw2.png")) # 5
        Security.images[6].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securitywa1.png")) #6
        Security.images[7].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securitywa2.png")) #7
        Security.images[8].set_colorkey((255,0,182))
        
        
        Security.images[0].convert_alpha()
        Security.images[1].convert_alpha()
        Security.images[2].convert_alpha()
        Security.images[3].convert_alpha()
        Security.images[4].convert_alpha()
        Security.images[5].convert_alpha()
        Security.images[6].convert_alpha()
        Security.images[7].convert_alpha()

        self.h= [pygame.image.load("data/h0.png"),
                 pygame.image.load("data/h1.png"),
                 pygame.image.load("data/h2.png"),
                 pygame.image.load("data/h3.png"),
                 pygame.image.load("data/h4.png"),
                 pygame.image.load("data/h5.png")]
        self.h[0].set_colorkey((255,0,182))
        self.h[1].set_colorkey((255,0,182))
        self.h[2].set_colorkey((255,0,182))
        self.h[3].set_colorkey((255,0,182))
        self.h[4].set_colorkey((255,0,182))
        self.h[5].set_colorkey((255,0,182))
        self.p= pygame.image.load("data/p.png")
        self.p.set_colorkey((255,0,182))
        self.e= pygame.image.load("data/protect.png")
        self.p.set_colorkey((255,0,182))
        self.i= [pygame.image.load("data/i0.png"),
                 pygame.image.load("data/i1.png"),
                 pygame.image.load("data/i2.png"),
                 pygame.image.load("data/i3.png"),
                 pygame.image.load("data/i4.png"),
                 pygame.image.load("data/i5.png")]
        self.i[1].set_colorkey((255,0,182))
        self.i[2].set_colorkey((255,0,182))
        self.i[3].set_colorkey((255,0,182))
        self.i[4].set_colorkey((255,0,182))
        self.i[5].set_colorkey((255,0,182))
        self.i[0].set_colorkey((255,0,182))
        self.d= [pygame.image.load("data/d0.png"),
                 pygame.image.load("data/d1.png"),
                 pygame.image.load("data/d2.png"),
                 pygame.image.load("data/d3.png"),
                 pygame.image.load("data/d4.png"),
                 pygame.image.load("data/d5.png")]
        self.g= [pygame.image.load("data/g0.png"),
                 pygame.image.load("data/g1.png"),
                 pygame.image.load("data/g2.png"),
                 pygame.image.load("data/g3.png"),
                 pygame.image.load("data/g4.png"),
                 pygame.image.load("data/g5.png")]
        self.v= [pygame.image.load("data/discodiscgunf.png"),
                 pygame.image.load("data/discodiscgunl.png"),
                 pygame.image.load("data/discodiscgunb.png"),
                 pygame.image.load("data/discodiscgunr.png"),
                 pygame.image.load("data/discodiscgunr.png"),
                 pygame.image.load("data/discodiscgunr.png")]
        self.k= [pygame.image.load("data/konfettif.png"),
                 pygame.image.load("data/konfettir.png"),
                 pygame.image.load("data/konfettib.png"),
                 pygame.image.load("data/konfettil.png"),
                 pygame.image.load("data/konfettil.png"),
                 pygame.image.load("data/konfettil.png")]
        self.w= [pygame.image.load("data/discogunf.png"),
                 pygame.image.load("data/discogunr.png"),
                 pygame.image.load("data/discogunb.png"),
                 pygame.image.load("data/discogunl.png"),
                 pygame.image.load("data/discogunl.png"),
                 pygame.image.load("data/discogunl.png")]         
        self.w[1].set_colorkey((255,0,182))
        self.w[2].set_colorkey((255,0,182))
        self.w[3].set_colorkey((255,0,182))
        self.w[4].set_colorkey((255,0,182))
        self.w[5].set_colorkey((255,0,182))
        self.w[0].set_colorkey((255,0,182))
        self.anim=0
        self.o= [pygame.image.load("data/discoball.png"),
                 pygame.image.load("data/discoball2.png")]
        self.o[0].set_colorkey((255,0,182))
        self.o[1].set_colorkey((255,0,182))
        self.anim=0         
        self.level=["hpppppoppppppwppppope",
                    "ihpppppppppihippppppe",
                    "idddgddddddhidvddddde",
                    "ddddgddddddddddddddde",
                    "gdddgddgdvddddkddddve",
                    "ddddgddddddddggddddde",
                    "ddddgdddddddddvddddde",
                    "gggggggdgggdggdggggge"]
        anim = 0
        self.legende={"h":self.h[anim],#towertop
                      "p":self.p,#nothing
                      "i":self.i[anim],#dirt
                      "g":self.g[anim],#lava
                      "d":self.d[anim], #grass
                      "v":self.v[anim], #discodiscgun
                      "w":self.w[anim], #discogun
                      "k":self.k[anim], #konfettigun
                      "e":self.e, #end of world
                      "o":self.o[anim] #discoball
                      }


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
            pygame.draw.circle(self.image, (random.randint(20,230),random.randint(20,230),random.randint(20,230)), (5,5),
                                            random.randint(3,10))
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
                self.dy += Game.FORCE_OF_GRAVITY # gravity suck fragments down
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)

class DiscoLaserCannon(pygame.sprite.Sprite):
    #a laser gun
    gravity= False
    image=pygame.image.load("data/discogun.png")
    number = 0
    
    def __init__(self,x,y, screen):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.hitpoints = 300.0
        self.hitpointsfull = 300.0
        self.reload_time = 0.2
        self.reload_time_full = 0.2#
        self.image = DiscoLaserCannon.image
        #efor  in images:
        self.image.set_colorkey((255,0,182))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.x = x
        self.y = y
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.lasermaxburntime =  random.random()*2+2
        self.laserburntime = 0
        self.beam = False
        self.opfernummer = None
        self.number = DiscoLaserCannon.number
        DiscoLaserCannon.number += 1
        #DiscoLaserCannonCannon.number += 1           # increase the number for next Bird
        #DiscoLaserCannon.DiscoLaserCannons[self.number] = self
        Healthbar(self)
        
        
    def update(self,seconds):
        self.reload_time += seconds
        if self.hitpoints < 1:
            self.kill()
        if self.reload_time > self.reload_time_full:
            # choose new target
            #opfernummer = None
            if len(Monster.monsters) > 0:
                      self.opfernummer = random.choice(list(Monster.monsters.keys()))
                      self.opfer = Monster.monsters[self.opfernummer]  
                      #lasertimer = 4 #rebalance
             
            if self.beam: 
                self.laserburntime += seconds
                if self.laserburntime > self.lasermaxburntime:
                      self.reload_time = 0
                      self.laserburntime = 0
                      self.beam = False

                #lasertimer -= seconds
            # gibt es ein Opfer?
            if self.opfernummer != None:
                    #existiert das Opfer noch in der Monstergruppe ?
                    if self.opfernummer in Monster.monsters:
                                                # tödlicher weißer laser
                        pygame.draw.line(self.screen,
                             (random.randint(200,255),
                              random.randint(200,255),
                              random.randint(200,255)),
                             (self.x,self.y),
                             (self.opfer.pos[0], self.opfer.pos[1]),7)
                        self.opfer.hitpoints-= 1.0
                        self.opfer.burntime = 4.0
                        #opfer.pos[0] -= 3
                        self.beam = True
                       
        
        
 
class DiscProjectile(pygame.sprite.Sprite):
        """a projectile of a Disc gun"""
        gravity = False # fragments fall down ?
        image=pygame.image.load("data/disc.png")
        def __init__(self, startpos=(random.randint(640,1024),random.randint(100,300)),
                           targetpos=(random.randint(640,1024),random.randint(100,300))):
            #         dx=random.randint(-Game.DISCMAXSPEED,Game.DISCMAXSPEED),
            #         dy=random.randint(-Game.DISCMAXSPEED,Game.DISCMAXSPEED)):
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.pos = [0.0,0.0]
            self.startpos = startpos
            self.targetpos = targetpos
            distancex = -self.startpos[0] + self.targetpos[0]
            distancey = -self.startpos[1] + self.targetpos[1]
            distance = (distancex**2 + distancey**2)**0.5
            if distance > Game.DISCTHROWERRANGE:
                self.kill()
            self.dx = distancex / distance                              
            self.dy = distancey / distance
            self.dx *= Game.DISCMAXSPEED
            self.dy *= Game.DISCMAXSPEED
            self.hitpoints = 10
            self.pos[0] = startpos[0]
            self.pos[1] = startpos[1]
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
            #self.dx = dx
            #self.dy = dy

        def update(self, seconds):
            self.time += seconds
            if self.time > self.lifetime:
                self.kill()
            if self.hitpoints <= 0:
                self.kill()
                 
             
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds
            #if Fragment.gravity:
             #   self.dy += FORCE_OF_GRAVITY # gravity suck fragments down
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)

class Flame (pygame.sprite.Sprite):
    images = []
    images.append(pygame.image.load("data/flamme.png"))
    images.append(pygame.image.load("data/flamme2.png"))
    for img in images:
        img.set_colorkey((255,0,182))
        #img.convert_alpha()
        
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.image = random.choice(Flame.images)
        self.rect = self.image.get_rect()
        self.x  = x
        self.y  = y
        self.rect.centerx = x
        self.rect.centery = y
    
    def update(self, seconds):
        self.kill()
        
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



class Monster(pygame.sprite.Sprite):
        """Generic Monster"""
        images=[]  # list of all images
        # not necessary:
        monsters = {} # a dictionary of all monsters
        number = 0

        def __init__(self, level, startpos=(0,200), hitpointsfull=600):
        #rebalance

            pygame.sprite.Sprite.__init__(self, self.groups ) #call parent class. NEVER FORGET !
            self.burntime = 0.0
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
            self.dy= random.randint(-70,70)#rebalance
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
            #--- not necessary:
            self.number = Monster.number # get my personal Birdnumber
            Monster.number+= 1           # increase the number for next Bird
            Monster.monsters[self.number] = self #
            Healthbar(self)
        def getChar(self):
            #Tile = 50*50
            x=int(self.pos[0]/50)
            y=int(self.pos[1]/50)+0 # correction value to get the tile under the feet doesn't actually work :\
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
            for _ in range(random.randint(7,20)):
                Fragment(self.pos)
            #Monster.monsters[self.number] = None # kill Bird in sprite dictionary
            del(Monster.monsters[self.number]) 
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
                #self.hitpoints-=1 #lava?
                self.burntime += 1.0
            if self.getChar()=="?":
                self.hitpoints=0
            if self.getChar()=="e":
                self.hitpoints=0
                Game.LIVES-=1
            if self.getChar()=="h":
                self.nomove = True
            self.dy=random.randint(-10, 10)
            self.dx= 20#random.randint(10,10)
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
            #--- calculate new position on screen -----
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
            #--- loose hitpoins
            #if self.crashing:
             #self.hitpoints -=1
            
            if self.burntime > 0 :
                self.hitpoints -= 1.0
                # reduce burntime
                self.burntime -= 0.4
                Flame(self.rect.centerx, self.rect.centery)
            
            if self.hitpoints <= 0:
                self.kill()

class Security(pygame.sprite.Sprite):
        """Generic Monster"""
        images=[]  # list of all images
        # not necessary:
        securitys = {} # a dictionary of all monsters
        number = 0

        def __init__(self, level, startpos=(-1,200), hitpointsfull=1200):


            pygame.sprite.Sprite.__init__(self, self.groups ) #call parent class. NEVER FORGET !
            self.burntime = 0.0
            if startpos[0]== -1:
                startpos=(Viewer.screenwidth, random.randint(150,250))
            self.z = 0 # animationsnummer
            self.duration = 0.0 # how long was the current animation visible in seconds
            self.level=level
            self.nomove = False
            #startpos=(0,screen.get_rect().center[1])
            startpos=(Viewer.screenwidth,random.randint(100,350))
            self.pos = [float(startpos[0]),float (startpos[1])] # dummy values to create a list
            #self.pos[0] = float(startpos[0]) # float for more precise calculation
            #self.pos[1] = float(startpos[1])
           # self.area = screen.get_rect()
            self.area = pygame.Rect(0,100,1024,300)
            self.image = Security.images[self.z]
            self.hitpointsfull = float(hitpointsfull) # maximal hitpoints , float makes decimal
            self.hitpoints = float(hitpointsfull) # actual hitpoints
            self.rect = self.image.get_rect()
            self.radius = max(self.rect.width, self.rect.height) / 2.0
            self.dx= random.random()*-10+20
            self.dy= random.randint(-70,70)
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0) 
            #self.newspeed()
            #self.cleanstatus()
            #self.catched = False
            #self.crashing = False
            #--- not necessary:
            self.taser = False
            self.number = Security.number # get my personal Birdnumber
            Security.number+= 1           # increase the number for next Bird
            Security.securitys[self.number] = self #
            Healthbar(self)


        #def newspeed(self):
            # new birdspeed, but not 0
            #speedrandom = random.choice([-1,1]) # flip a coin
            #self.dx = random.random() * ACTORSPEEDMAX * speedrandom + speedrandom
            #self.dy = random.random() * ACTORSPEEDMAX * speedrandom + speedrandom
        def getChar(self):
            #Tile = 50*50
            x=int(self.pos[0]/50)
            y=int(self.pos[1]/50)+0 # correction value to get the tile under the feet doesn't actually work :\
            try:
                char=self.level[y][x]
            except:
                char="?"
            return char


        def kill(self):
            for _ in range(random.randint(10,30)):
                Fragment(self.pos)
            Security.securitys[self.number] = None # kill Bird in sprite dictionary

            pygame.sprite.Sprite.kill(self) # kill the actual Bird

        def update(self, seconds):
            self.duration += seconds
            if self.duration > 0.5:
                self.duration= 0
                self.z  +=1
                if self.z >= len(Security.images):
                    self.z = 0
                self.image=Security.images[self.z]

            #-------
            #if self.getChar()=="g":
                #self.hitpoints-=1 #lava?
                #self.burntime += 1.0
            if self.getChar()=="?":
                self.hitpoints=0
            #if self.getChar()=="e":
                #self.hitpoints=0
                #Game.LIVES-=1
            if self.getChar()=="h":
                self.nomove = True
            else:
                self.nomove = False
            self.dy=random.randint(-50, 50)
            self.dx= -25#random.randint(10,10)
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
            #if self.burntime > 0 :
                #self.hitpoints -= 1.0
                # reduce burntime
                #self.burntime -= 0.4
                #Flame(self.rect.centerx, self.rect.centery)
            
            if self.hitpoints <= 0:
                self.kill()


class Viewer(object):

     screenwidth = 1025
     screenheight = 400
     
     def __init__(self, width=0, height=0, fps=30):
        """Initialize pygame, window, background, font,...
           default arguments
        """

        pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        if self.width == 0:
            self.width = Viewer.screenwidth
        else:
            Viewer.screenwidth = width
        if self.height == 0:
            self.height = Viewer.screenheight
        else:
            Viewer.screenheight = self.height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        #self.background.fill((255,255,255)) # fill background white
        self.background.fill((1,75,176))     # fill the background white (red,green,blue)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 24, bold=True)

        # sprite groups
        self.playergroup = pygame.sprite.LayeredUpdates()
        self.bargroup = pygame.sprite.Group()
        self.stuffgroup = pygame.sprite.Group()
        self.fragmentgroup = pygame.sprite.Group()
        self.allgroup = pygame.sprite.LayeredUpdates()
        self.projectilegroup = pygame.sprite.Group()
        self.cannongroup = pygame.sprite.Group()

        self.monstergroup=pygame.sprite.Group()
        self.allgroup=pygame.sprite.LayeredUpdates()
        self.bargroup = pygame.sprite.Group()
        self.fragmentgroup = pygame.sprite.Group()
        self.securitygroup= pygame.sprite.Group()

        DiscProjectile.groups = self.allgroup, self.projectilegroup
        DiscoLaserCannon.groups = self.allgroup, self.cannongroup
        Monster.groups =  self.allgroup, self.monstergroup
        Fragment.groups = self.allgroup, self.fragmentgroup
        Healthbar.groups = self.allgroup, self.bargroup
        Flame.groups = self.allgroup      
        Security.groups = self.allgroup, self.securitygroup
        self.game = Game()
        
     def paint(self):
        # paint the level of self.game
        x=0
        y=0
        self.game.fleckanim=[]
        for zeile in self.game.level:
          for fleck in zeile:
               self.game.fleckanim.append(0)
               self.background.blit(self.game.legende[fleck],(x,y))
               x+=50
          y+=50
          x=0
        DiscoLaserCannon(500,100, self.screen) 
        #DiscoLaserCannon(700,100, self.screen) 
        #DiscoLaserCannon(600,100, self.screen) 
        #DiscoLaserCannon(400,100, self.screen) 
        #DiscoLaserCannon(900,100, self.screen) 
        #DiscoLaserCannon(500,200, self.screen) 
        #DiscoLaserCannon(700,350, self.screen) 
        #DiscoLaserCannon(600,350, self.screen) 
        #DiscoLaserCannon(400,450, self.screen) 
        #DiscoLaserCannon(900,550, self.screen) 
        #DiscoLaserCannon()
        
          
     def run(self):
        """The mainloop
        """
        lasertimer = 0.0 # ....klasse !!
        opfernummer = None
        self.paint()
        running = True
        millis = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key==pygame.K_F2:
                        for px in range (0,5):
                            Security(self.game.level, hitpointsfull = 2000)
                    # ------CHEAT KEY----------
                    #if event.key==pygame.K_F1:
                       #for px in range (0,240):
                           #DiscProjectile(pos=(random.randint(540,1024),random.randint(100,400)))12

            milliseconds = self.clock.tick(self.fps)
            millis += milliseconds
            seconds=milliseconds /1000.0
            self.playtime += milliseconds / 1000.0
            self.playtime += milliseconds / 1000.0
            self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
                           self.clock.get_fps(), " "*5, self.playtime))

            pygame.display.flip()
            self.screen.blit(self.background, (0, 0)) # alles löschen
            # level aufbauen

            # monster spawn
            if random.random()<self.game.SPAWNRATE:
               Monster(self.game.level)
               
               
            if random.random()<self.game.SECURITYSPAWNRATE:
               Security(self.game.level)

            # spritecollide
            
            if millis > 500: # jede halbe sekunde neue animation
                millis=0
                z=0
                x=0
                y=0
                for zeile in self.game.level:
                    for fleck in zeile:
                        if fleck == "d" and self.game.fleckanim[z] == 0:      
                            if random.random() < 0.005:
                                self.game.fleckanim[z] += 1
                        elif fleck == "g" and self.game.fleckanim[z] == 0:
                            if random.random() < 0.5:
                                self.game.fleckanim[z] += 1
                        else:
                            self.game.fleckanim[z] += 1 # normaler fleck
                        if fleck == "v":
                            targetlist=[]
                            for target in self.monstergroup:
                                #pass # pythagoras distanz ausrechnen
                                #ziel wird gesucht reichweite getestet
                                #zufälliges ziel wird abgeschossen
                                distx=abs(target.pos[0]-x)
                                disty=abs(target.pos[1]-y)
                                dist=(distx**2+disty**2)**0.5
                                if dist<self.game.DISCTHROWERRANGE:
                                    targetlist.append(target)
                            if len(targetlist)>0:
                                target=random.choice(targetlist)
                                print("taget found{}".format(target.pos) )
                                #schuss
                                #  fliegt nur nach rechts unten
                                if target.pos[0]> x:
                                    xsign = 1
                                else:
                                    xsign = -1
                                if target.pos[1]> y:
                                    ysign = 1
                                else:
                                    ysign = -1
                                DiscProjectile((x,y),(target.pos[0], target.pos[1]))
                            else:
                                print("No target found")
                        if self.game.fleckanim[z] > 5:
                            self.game.fleckanim[z] = 0       
                        z+=1
                        x+=50
                    y+=50
                    x=0
                 
            
            # monster take damage from discs
            for mymonster in self.monstergroup:
                crashgroup = pygame.sprite.spritecollide(mymonster, self.projectilegroup, False)
                for myprojectile in crashgroup:
                      mymonster.hitpoints-=0.25
                      #mymonster.pos[0] -= 5 # test for collision with bullet
                      myprojectile.hitpoints-=0.25
            for mymonster in self.monstergroup:
                crashgroup = pygame.sprite.spritecollide(mymonster, self.cannongroup, False)
                for mycannon in crashgroup:
                      #mymonster.hitpoints-=0.25
                      #mymonster.pos[0] -= 5 # test for collision with bullet
                      mycannon.hitpoints-=0.25
            #and securitys
            for mysecurity in self.securitygroup:
                crashgroup = pygame.sprite.spritecollide(mysecurity, self.monstergroup, False)
                mysecurity.taser = False
                for mymonster in crashgroup:
                      mymonster.hitpoints-=4 # test for collision with bullet
                      mymonster.pos[0]-=random.randint(5,20)
                      mysecurity.hitpoints-=5
                      mysecurity.pos[0]+=random.randint(1,7)
                      mysecurity.taser = True
            # laser # soll eine Klasse werden!!!

                #pygame.draw.line #rebalance
                
            # bunter lichtlaser
            #pygame.draw.line(self.screen,(random.randint(0,255),random.randint(0,255),
                             #random.randint(0,255)),(925,25),(random.randint(0,950),
                             #random.randint(0,500)),random.randint(5,15))
            # bunter lichtlaser
            #pygame.draw.line(self.screen,(random.randint(0,255),random.randint(0,255),
                             #random.randint(0,255)),(325,25),(random.randint(0,950),
                             #random.randint(0,500)),random.randint(5,15))
            
         
            #allgroup.clear(screen, background)
            self.allgroup.update(seconds)
            self.allgroup.draw(self.screen)



        pygame.quit()


     def draw_text(self, text):
        """Center text in window
        """
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(surface, (25,5))





## code on module level
if __name__ == '__main__':

    # call with width of window and fps
    Viewer().run()





