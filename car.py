import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Load and play background music
pygame.mixer.music.load('carm.mp3')
pygame.mixer.music.play(-1)

# Set up the display window
wn = pygame.display.set_mode((800, 584))
pygame.display.set_caption('Car Game')

# Initialize score and font
score_value = 0
font = pygame.font.Font(None, 32)  # Use default font
score_x = 590
score_y = 250

# Position for crash message
crash_x = 290
crash_y = 290

# Load and set the game icon
try:
    logo = pygame.image.load('rrrr.jpg')
    pygame.display.set_icon(logo)
except pygame.error as e:
    print(f"Failed to load image: {e}")
    pygame.quit()
    sys.exit()

# Game state variable
game_exit = False

# Load background image
bg = pygame.image.load('bgf2.jpg')

# Load main car image and initialize its position
maincar = pygame.image.load('car1.png')
maincar_x = 290
maincar_y = 398
maincar_xchange = 0

# Load enemy cars images and initialize their positions
car1 = pygame.image.load('m1.png')
car1_x = random.randint(220, 480)
car1_y = -100
car1_ychange = 0.50

car2 = pygame.image.load('m2.png')
car2_x = random.randint(220, 480)
car2_y = -300
car2_ychange = 0.50

car3 = pygame.image.load('m3.png')
car3_x = random.randint(220, 480)
car3_y = -500
car3_ychange = 0.50

# Function to display the main car
def picture(x, y):
    wn.blit(maincar, (x, y))

# Functions to display enemy cars
def picture1(x, y):
    wn.blit(car1, (x, y))

def picture2(x, y):
    wn.blit(car2, (x, y))

def picture3(x, y):
    wn.blit(car3, (x, y))

# Collision detection function
def iscollision(maincar_x, maincar_y, car_x, car_y):
    distance = math.sqrt((math.pow(maincar_x - car_x, 2) + math.pow(maincar_y - car_y, 2)))
    return distance < 50

# Function to display the score
def show_score(x, y):
    font_score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    wn.blit(font_score, (x, y))

# Function to display crash message
def show_crash(x, y):
    font_crash = font.render("Car Crashed!", True, (255, 255, 0))
    wn.blit(font_crash, (x, y))

# Main game loop
while not game_exit:
    wn.blit(bg, (0, 0))  # Draw background image

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                maincar_xchange = 0.3
            if event.key == pygame.K_LEFT:
                maincar_xchange = -0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                maincar_xchange = 0

    # Update car positions
    maincar_x += maincar_xchange
    car1_y += car1_ychange
    car2_y += car2_ychange
    car3_y += car3_ychange

    # Boundary checking for main car
    if maincar_x <= 150:
        maincar_x = 150
    elif maincar_x >= 590:
        maincar_x = 590

    # Respawn enemy cars and increase score
    if car1_y > 600:
        car1_y = -100
        car1_x = random.randint(220, 480)
        score_value += 1
        print(score_value)

    if car2_y > 600:
        car2_y = -100
        car2_x = random.randint(220, 480)
        score_value += 1
        print(score_value)

    if car3_y > 600:
        car3_y = -100
        car3_x = random.randint(220, 480)
        score_value += 1
        print(score_value)

    # Check for collisions
    collision1 = iscollision(maincar_x, maincar_y, car1_x, car1_y)
    collision2 = iscollision(maincar_x, maincar_y, car2_x, car2_y)
    collision3 = iscollision(maincar_x, maincar_y, car3_x, car3_y)

    # Draw elements on the screen
    picture(maincar_x, maincar_y)
    show_score(score_x, score_y)
    picture1(car1_x, car1_y)
    picture2(car2_x, car2_y)
    picture3(car3_x, car3_y)

    # Handle collisions
    if collision1 or collision2 or collision3:
        pygame.mixer.music.stop()
        Sound_crash = pygame.mixer.Sound('carc.mp3')
        Sound_crash.play()
        wn.fill((255, 0, 255))  # Screen color change on crash
        car1_ychange = 0
        car2_ychange = 0
        car3_ychange = 0
        maincar_xchange = 0
        show_crash(crash_x, crash_y)
        show_score(310, 330)
    
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
quit()
