import pygame
import os
import keyboard
from pathlib import Path

os.chdir(__file__[:-7])
pygame.init()

screen = pygame.display.set_mode((450,450))
pygame.display.set_caption("Jogo da Velha!")
background = pygame.image.load("background.png")
vitory = 0
circle = pygame.image.load("circle.png").convert_alpha()
x = pygame.image.load("x.png").convert_alpha()

pygame.display.set_icon(background)

places = [ 0, 0, 0,
           0, 0, 0, 
           0, 0, 0]

squares = []

class SQUARE():
    def __init__(self, num):
        x = num % 3 * 150
        y = num // 3 * 150
        
        squares.append(pygame.rect.Rect(x, y, 150, 150))


        pass

for i in range(0,9):
    SQUARE(i)



#1 == O; 2 == X
fois = 1

running = True
jogando = True


while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: running = False

    MOUSE_POS = pygame.mouse.get_pos()
    MOUSE_CLICKED = any(pygame.mouse.get_pressed())
    screen.blit(background, (0,0)) 

    for i in range(0,9):
        if places[i] == 1: screen.blit(circle, squares[i])
        if places[i] == 2: screen.blit(x, squares[i])
    
    if keyboard.is_pressed("r"):
        for i in range(0,9):
            places[i] = 0
        jogando = True
        vitory = 0
        pygame.display.set_caption("Jogo da Velha!")

    if places[3] == places[4] == places[5] and vitory == 0: vitory = places[3]
    if places[0] == places[1] == places[2] and vitory == 0: vitory = places[0]
    if places[6] == places[7] == places[8] and vitory == 0: vitory = places[6]
    
    if places[0] == places[3] == places[6] and vitory == 0: vitory = places[0]
    if places[1] == places[4] == places[7] and vitory == 0: vitory = places[1]
    if places[2] == places[5] == places[8] and vitory == 0: vitory = places[2]

    if places[0] == places[4] == places[8] and vitory == 0: vitory = places[0]
    if places[6] == places[4] == places[2] and vitory == 0: vitory = places[2]

    if 0 not in places and vitory == 0:
        for i in range(0,9):
            jogando = False; pygame.display.set_caption("Jogo da Velha! [EMPATE] [CLIQUE R]" )
    if jogando:
        for i in squares:
            if i.collidepoint(MOUSE_POS) and MOUSE_CLICKED:
                if places[squares.index(i)] == 0:
                    places[squares.index(i)] = fois
                    print(places)
                    if fois == 1: fois = 2
                    else: fois = 1


    if vitory == 1: print("CIRCULOS GANHAA"); jogando = False; pygame.display.set_caption("Jogo da Velha! [CIRCULO GANHOU] [CLIQUE R]" )
    if vitory == 2: print("X GANHAAS")    ; jogando = False; pygame.display.set_caption("Jogo da Velha! [X GANHOU] [CLIQUE R]")

    pygame.display.flip()