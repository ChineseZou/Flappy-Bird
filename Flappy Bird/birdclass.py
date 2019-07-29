import pygame


class Bird(object):
    def __init__(self):
        self.birdRect=pygame.Rect(65,50,50,50)
        self.birdStatus=[pygame.image.load("0.png"),
                         pygame.image.load("1.png"),
                         pygame.image.load("dead.png")]
        self.status=0
        self.birdX=120
        self.birdY=350
        
        self.jump=False
        self.dead=False
        self.jumpSpeed=10
        self.gravity=2

    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed-=1
            self.birdY-=self.jumpSpeed
        else:
            self.gravity+=0.05
            self.birdY += self.gravity
        self.birdRect[1] = self.birdY
