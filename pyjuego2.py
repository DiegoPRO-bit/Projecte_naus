import time , random
from pygame.locals import *
import pygame


guanyador = 0
RED = (255,0,0)
AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/fons.png'
MUSICA_FONS = 'assets/music.mp3'
WHITE = (255,255,255)
videsantes = 0


#pantalles
#pantalla1 = Menu
#pantalla 2 = Credits
#PANTALLA 3 = JOX
#PANTALLA4  = GAMEOVERww
pantalla_actual = 1

# Jugador 1:
player_image = pygame.image.load('assets/nau.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 4

# Jugador 2:
player_image2 = pygame.image.load('assets/nau2.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 500))
velocitat_nau2 = 4

# Bala rectangular blanca:
bala_imatge2 = pygame.image.load("assets/balaroja.png")
bala_imatge = pygame.image.load("assets/bala.png") #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
# bala_imatge.fill(WHITE) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 12
temps_entre_bales = 1000 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2


pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Arcade")

# Control de FPS
clock = pygame.time.Clock()
fps = 30

# vides:
vides1 = 3
vides2 = 3
vida_image = pygame.image.load('assets/cor.png')
vida1_jugador1 = vida_image.get_rect(midbottom=(650,100))
vida2_jugador1 = vida_image.get_rect(midbottom=(700,100))
vida3_jugador1 = vida_image.get_rect(midbottom=(750,100))

vida1_jugador2 = vida_image.get_rect(midbottom=(100,580))
vida2_jugador2 = vida_image.get_rect(midbottom=(150,580))
vida3_jugador2 = vida_image.get_rect(midbottom=(200,580))

def escudo1(vides1):
    videsantes = vides1

    vides1 = 100
    print("escudo activado")
    time.sleep(4)
    vides1 = videsantes
    print("escudo desactiva")


def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))
def mostrar_menu():
    imprimir_pantalla_fons('assets/INCIO.png')

    font1 = pygame.font.SysFont(None, 200)
    fontmenu = pygame.font.SysFont(None, 40)

    img2 = fontmenu.render("1.JUGAR",True,RED)
    img3 = fontmenu.render("2.CREDITS", True, RED)
    img4 = fontmenu.render("3.SORTIR", True, RED)



    pantalla.blit(img2, (325, 270))
    pantalla.blit(img3, (325, 370))
    pantalla.blit(img4, (325, 480))

def mostrar_credits():
    fontcredit = pygame.font.SysFont(None, 30)
    fontcredit2 = pygame.font.SysFont(None, 80)
    CREDIT = fontcredit.render("PROGRAMACIO: DIEGO SÁNCHEZ",True,RED)
    CREDIT2 = fontcredit.render("GRAFICS: DIEGO SÁNCHEZ", True, RED)
    CREDIT3 = fontcredit.render("MÚSICA: IN PROGRESS ", True, RED)
    SONS = fontcredit.render("SO: FREESOUND I MYINSTANTS", True, RED)
    

    pantalla.blit(CREDIT, (200, 320))
    pantalla.blit(CREDIT2, (200, 380))
    pantalla.blit(CREDIT3, (200, 440))
    pantalla.blit(SONS, (200, 500))



    pass

while True:
    #contador
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if pantalla_actual == 1:
            if event.type == KEYDOWN:
                if event.key == K_1:

                    pantalla_actual = 3

                if event.key == K_2:
                    pantalla_actual = 2


                if event.key == K_3:
                    pygame.quit()


        # controlar trets de les naus






        if pantalla_actual == 1:
            mostrar_menu()

            pygame.mixer.music.load('assets/menumusic.mp3')
            pygame.mixer.music.play()

        if pantalla_actual == 4:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pantalla_actual = 1

        if pantalla_actual == 2:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pantalla_actual = 1

            imprimir_pantalla_fons('assets/CREDITS.png')
            mostrar_credits()

        if pantalla_actual == 3:
            if event.type == KEYDOWN:
                #jugador 1
                if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                    bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                    temps_ultima_bala_jugador1 = current_time


                    pygame.mixer.music.load('assets/BLASTER.wav')
                    pygame.mixer.music.play()
                # jugador 2
                if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                    bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                    temps_ultima_bala_jugador2 = current_time
                    pygame.mixer.music.load('assets/rename.wav')
                    pygame.mixer.music.play()

    if pantalla_actual == 4:
        vides1 = 3
        vides2 = 3
        for i in bales_jugador1:
            bales_jugador1.remove(i)
        for i in bales_jugador2:
            bales_jugador2.remove(i)

        imprimir_pantalla_fons('assets/gameover.png')
        font = pygame.font.SysFont( None,100)
        text = "Player" + str(guanyador) +  "Wins!"
        img = font.render(text,True,RED)
        pantalla.blit(img,(100,450))

    if pantalla_actual == 3:
        # Moviment del jugador 1
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            player_rect.x -= velocitat_nau
        if keys[K_d]:
            player_rect.x += velocitat_nau
        # Moviment del jugador 2
        if keys[K_LEFT]:
            player_rect2.x -= velocitat_nau2
        if keys[K_RIGHT]:
            player_rect2.x += velocitat_nau2

        imprimir_pantalla_fons('assets/gameover.png')

        ambient_music = pygame.mixer.Sound('assets/juegomusic.wav')
        ambient_music.play()


        # Mantenir al jugador dins de la pantalla:
        player_rect.clamp_ip(pantalla.get_rect())
        player_rect2.clamp_ip(pantalla.get_rect())

        #dibuixar el fons:
        imprimir_pantalla_fons(BACKGROUND_IMAGE)

        #Actualitzar i dibuixar les bales del jugador 1:
        for bala in bales_jugador1:  # bucle que recorre totes les bales
            bala.y -= velocitat_bales  # mou la bala
            if bala.bottom < 0 or bala.top > ALTURA:  # comprova que no ha sortit de la pantalla
                bales_jugador1.remove(bala)  # si ha sortit elimina la bala
            else:
                pantalla.blit(bala_imatge, bala)  # si no ha sortit la dibuixa
            # Detectar col·lisions jugador 2:
            if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 1!")
                bales_jugador1.remove(bala)  # eliminem la bala
                vides2 = vides2 - 1
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1
                pygame.mixer.music.load('assets/explosion.wav')
                pygame.mixer.music.play()

        # Actualitzar i dibuixar les bales del jugador 2:
        for bala in bales_jugador2:
            bala.y += velocitat_bales
            if bala.bottom < 0 or bala.top > ALTURA:
                bales_jugador2.remove(bala)
            else:
                pantalla.blit(bala_imatge2, bala)
            # Detectar col·lisions jugador 1:
            if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 2!")
                bales_jugador2.remove(bala)  # eliminem la bala
                vides1 = vides1 - 1
                pygame.mixer.music.load('assets/roblox-death-sound-effect.mp3')
                pygame.mixer.music.play()
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        #dibuixar els jugadors:
        pantalla.blit(player_image, player_rect)
        pantalla.blit(player_image2, player_rect2)

        # dibuixar vides:
        if vides1 >= 1:
            pantalla.blit(vida_image, vida1_jugador1)


        if vides1 >= 2:
            pantalla.blit(vida_image, vida2_jugador1)

        if vides1 == 3:
            pantalla.blit(vida_image, vida3_jugador1)


        if vides2 >= 1:
            pantalla.blit(vida_image, vida1_jugador2)
        if vides2 >= 2:
            pantalla.blit(vida_image, vida2_jugador2)
        if vides2 == 3:
            pantalla.blit(vida_image, vida3_jugador2)

        if vides1 <= 0 or vides2<= 0:
            pantalla_actual = 4
            guanyador = 1
            pygame.mixer.music.load('assets/gameover.wav')
            pygame.mixer.music.play()

            if vides1 <= 0:
                guanyador = 2

    pygame.display.update()
    clock.tick(fps)
