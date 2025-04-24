import pygame, sys
from pygame.locals import *
import random, time

cards = ["cards/bombardiro_crocodilo.png", "cards/brrbrrpatapim.png", "cards/lirililarila.png", "cards/tralalerotralala.png", "cards/capuchinoasasino.png", "cards/chimpanzinibananini.png", "cards/frigocamelo.png", "cards/trictracbaraboom.png", "cards/frulifrula.png", "cards/bobrittobondito.png"]
sounds = ["sounds/bombardiro-crocodilo.mp3", "sounds/brr-brr-patapim.mp3", "sounds/lirili-larila.mp3", "sounds/tralalero-tralala.mp3", "sounds/cappuccino-assassino.mp3", "sounds/chimpanzini-bananini.mp3", "sounds/47-frigo-camelo.mp3", "sounds/trictracbaraboom.mp3", "sounds/fruli frula.mp3", "sounds/bobrito-bandito-italian-brainrot.mp3"]
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

current_iteration = 0
max_iterations = 10

WHITE = (255, 255, 255)
GREY = (128,128,128)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
CASH = 1000000
font_pokemon = pygame.font.Font("fonts/Pokemon Solid.ttf", 40)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(GREY)
pygame.display.set_caption("Brainrot Pack Opener")

background = pygame.image.load("images/background.png")
sprite_image = pygame.image.load("images/pack.png")
sprite_image = pygame.transform.scale(sprite_image, (400, 500))
sprite_rect = sprite_image.get_rect()
sprite_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

DISPLAYSURF.blit(background, (0, 0))
DISPLAYSURF.blit(sprite_image, sprite_rect)


def execute_iteration(iteration):
    print(current_iteration)
    global reset_time
    print(f"Opening Card {iteration + 1}")
    ranarray = random.randint(0, 9)
    if current_iteration == 0:
        time.sleep(2)
    pygame.mixer.stop()
    card_image = pygame.image.load(cards[ranarray])
    pygame.mixer.Sound(sounds[ranarray]).play()
    print(cards[ranarray])
    card_image = pygame.transform.scale(card_image, (500, 600))
    card_rect = card_image.get_rect()
    card_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    
    DISPLAYSURF.blit(background, (0, 0))
    DISPLAYSURF.blit(card_image, card_rect)
    cash_display = font_pokemon.render(str(f"$ {CASH}"), True, WHITE)
    DISPLAYSURF.blit(cash_display, (10, 10))
    pygame.display.update()


    if iteration == max_iterations - 1:
        reset_time = pygame.time.get_ticks()

running = True
reset_time = None
pack_opened = False  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if sprite_rect.collidepoint(event.pos):
                if pack_opened:
                    reset_time = None
                    pack_opened = False
                    current_iteration = 0
                    DISPLAYSURF.blit(background, (0, 0))
                    DISPLAYSURF.blit(sprite_image, sprite_rect)
                    cash_display = font_pokemon.render(str(f"$ {CASH}"), True, WHITE)
                    DISPLAYSURF.blit(cash_display, (10, 10))
                    pygame.display.update()
                else:
                    if CASH >= 10:
                        
                        if current_iteration == 0:
                            
                            pygame.mixer.Sound("sounds/purchase.wav").play()
                            print(f"Cash deducted! Remaining: $ {CASH}")

                        if current_iteration < max_iterations - 1:
                            execute_iteration(current_iteration)
                            current_iteration += 1
                        elif current_iteration == max_iterations - 1:
                            execute_iteration(current_iteration)
                            current_iteration += 1
                            pack_opened = True
                            CASH -= 10





    cash_display = font_pokemon.render(str(f"$ {CASH}"), True, WHITE)
    DISPLAYSURF.blit(cash_display, (10, 10))
    if current_iteration == 0:
        pygame.mixer.stop()
        

    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()
