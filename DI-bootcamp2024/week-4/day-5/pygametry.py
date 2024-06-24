import pygame

pygame.init()

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('BattleShip')
icon = pygame.image.load('ship.png')
pygame.display.set_icon(icon)

image = pygame.image.load('background.jpg')
def bk(image):
    size  = pygame.transform.scale(image, (600, 800))
    screen.blit(size, (0,0))   

player_icon = pygame.image.load('pirate1.png')
player_iconX = 40
player_iconZ = 40

def player():
    screen.blit(player_icon, (player_iconX, player_iconZ))
    
    
run = True
while run:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    screen.fill((0, 0, 0))             
    bk(image)
    
    player()
    pygame.display.update()
