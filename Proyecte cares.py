
import pygame, sys
from pygame.locals import *
BLUE = 0,166,214
AMPLE = 1024
ALT = 1024
TAMANY = (AMPLE,ALT)
NEGRE = (0,0,0)
VERMELL = (255,0,0,0)
BLANC = (255,255,255)
RED = (255,0,0)
YELLOW =(255,255,0)
WHITE = (255,255,255)
VERDE = (0,255,0)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Rectangle')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANC)
    RECTANGULO = pygame.Rect(265,500,500,800)

    pygame.draw.ellipse(pantalla, BLUE,(180,500,700,700) )
    pygame.draw.ellipse(pantalla, WHITE, (320, 500, 400, 400))


    pygame.draw.circle(pantalla,BLUE,(512,250),300,111150)
    pygame.draw.circle(pantalla,WHITE,(512,250),230,100000)

    pygame.draw.line(pantalla,NEGRE,(300,360),(450,340),10)

    pygame.draw.line(pantalla, NEGRE, (300, 270), (450, 270),10 )

    pygame.draw.line(pantalla, NEGRE, (300, 180), (450, 240),10 )

    # ceja
    pygame.draw.line(pantalla,NEGRE,(550,100),(640,90),10)
    pygame.draw.line(pantalla,NEGRE,(390,90),(500,100),10)

    pygame.draw.circle(pantalla,RED,(512,300),60)
    pygame.draw.line(pantalla,NEGRE,(570,240),(700,180),10)
    pygame.draw.line(pantalla, NEGRE, (570, 270), (700, 270), 10)
    pygame.draw.line(pantalla, NEGRE, (570, 340), (700, 360), 10)
    pygame.draw.line(pantalla,BLUE,(300,680),(10,800),100)
    pygame.draw.line(pantalla, BLUE, (800, 680), (1012, 800), 100)



    pygame.draw.ellipse(pantalla,NEGRE ,((360,100),(100,100)),)
    pygame.draw.ellipse(pantalla, NEGRE, ((560, 100), (100, 100)), )

    mouth_rect = pygame.Rect(440, 360, 100, 50)  # Rectángulo donde estará la boca
    pygame.draw.arc(pantalla, NEGRE, mouth_rect, 0, 3.14, 5)

    pygame.display.update()
