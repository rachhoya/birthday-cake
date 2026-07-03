import pygame
import time
pygame.init()

WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("birthday card animation")

image=pygame.image.load("balloon.jpg")
image=pygame.transform.scale(image,(WIDTH,HEIGHT))

image2=pygame.image.load("present.jpg")
image2=pygame.transform.scale(image2,(WIDTH,HEIGHT))

image3=pygame.image.load("cake.jpg")
image3=pygame.transform.scale(image3,(WIDTH,HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit
        screen.blit(image,(0,0))

        font=pygame.font.SysFont("Times New Roman",72)
        text=font.render("Happy",True,"black")
        text2=font.render("Birthday",True,"black")
        screen.blit(text,(207,125))
        screen.blit(text2,(180,200))
        pygame.display.update()
        time.sleep(8)

        image2=pygame.image.load("present.jpg")
        font1=pygame.font.SysFont("Times New Roman",38)
        text3=font1.render("Wishing you a bright future ahead",True,"black")
        screen.blit(image2,(0,0))
        screen.blit(text3,(30,85))
        pygame.display.update()
        time.sleep(8)
        
        image3=pygame.image.load("cake.jpg")
        screen.blit(image3,(0,0))
        pygame.display.update()
        time.sleep(8)
