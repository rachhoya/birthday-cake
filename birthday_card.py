import pygame
import time
pygame.init()

WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("birthday card animation")

image=pygame.image.load("balloon.jpg")
image=pygame.transform.scale(image,(WIDTH,HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit
        screen.blit(image,(0,0))

        font=pygame.font.SysFont("Times New Roman",72)
        text=font.render("Happy",True,"black")
        text2=font.render("Birthday",True,"black")
        screen.blit(text,(200,100))
        screen.blit(text2,(200,200))
        pygame.display.update()