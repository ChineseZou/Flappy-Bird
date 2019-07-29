import pygame



class Pipeline(object):
    def __init__(self):
        self.wallx = 400
        self.pipeUp = pygame.image.load("p27869235.jpg")
        self.pipeDown = pygame.image.load("p27869234.jpg")
        
    def updatePipeline(self):
        self.wallx -= 5
       
        if self.wallx < -50:
            global score
            score += 1

            self.wallx = 400  #此处可用random
            
        #global 全局变量在模块内有效，因此目前我只能将Pipeline类在main.py中定义
        
        
