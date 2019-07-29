import pygame
import sys
import random
from birdclass import Bird

class Pipeline(object):
    def __init__(self):
        self.wallx = 400
        self.pipeUp = pygame.image.load("p27869235.jpg")
        self.pipeDown = pygame.image.load("p27869234.jpg")
        
    def updatePipeline(self):
        self.wallx -= 5
       
        if self.wallx < -80:
            global score
            score += 1

            self.wallx = 400  #此处可用random


def creatMap():
    screen.fill((255,255,0))   #填充背景色，括号内为三原色
    screen.blit(backgroud,(0,0))

    screen.blit(Pipeline.pipeUp,(Pipeline.wallx,-200))
    screen.blit(Pipeline.pipeDown,(Pipeline.wallx,400))
    Pipeline.updatePipeline()
    
    screen.blit(font.render('score:'+str(score),-1,(255,255,255)),(100,50))
    #pygame.display.update()
    
    
    if Bird.dead:
        Bird.status=2
    elif Bird.jump:
        Bird.status=1
    screen.blit(Bird.birdStatus[Bird.status],(Bird.birdX,Bird.birdY))
    Bird.birdUpdate()
    
    pygame.display.update()

def checkDead():
    upRect=pygame.Rect(Pipeline.wallx,-250,Pipeline.pipeUp.get_width()-3,
                       Pipeline.pipeUp.get_height())
    downRect=pygame.Rect(Pipeline.wallx,450,Pipeline.pipeDown.get_width()-3,
                       Pipeline.pipeDown.get_height())
    if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):
        Bird.dead=True
    if not 0< Bird.birdRect[1] < height:
        Bird.dead=True
        return True
    else:
        return False

def getResult1():
    final_text1='Game Over'
    final_text2='Your final score is:'+str(score)
    ft1_font = pygame.font.SysFont("Arial",70)
    ft1_surf=font.render(final_text1,1,(242,3,36))
    ft2_font = pygame.font.SysFont("Arial",50)
    ft2_surf = font.render(final_text2,1,(253,177,6))

    screen.blit(ft1_surf,[screen.get_width()/2-ft1_surf.get_width()/2,100])
    screen.blit(ft2_surf,[screen.get_width()/2-ft2_surf.get_width()/2,200])
    pygame.display.flip()
    

if __name__=='__main__':
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont(None,50)
    
    size=width,height=400,600   #
    screen=pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Bird=Bird()
    Pipeline=Pipeline()
    
    score=0
    pygame.time.delay(2000)  #####让程序再开始前先暂停一会儿

    while True:
        clock.tick(60)
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN or
                event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:

                Bird.jump= True
                Bird.gravity = 3
                Bird.jumpSpeed = 10
                
        backgroud = pygame.image.load('p27869138.jpg')
        if checkDead():
            getResult1()
        else:
            creatMap()
    pygame.quit()
