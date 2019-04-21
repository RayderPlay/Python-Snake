import pygame
import random
import ctypes


clientWidth = 480
clientHeight = 480
snakeSize = 12
size = (clientWidth, clientHeight)
fruitX = random.randrange(0, clientWidth - 12, 12)
fruitY = random.randrange(0, clientHeight - 12, 12)
score = 0
lead_x = clientWidth // 2
lead_y = clientHeight // 2
change_pixels_of_x = 0
change_pixels_of_y = 0
mySnakeBody = []
snakeLength = 1
user32 = ctypes.windll.user32

myColor = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'white': (255, 255, 255),
    'black': (0, 0, 0)
}


# Function from check game state
def gameOver():
    ctypes.windll.user32.MessageBoxW(0, "Game Over", "Game State", 1)  # Game over MassageBox
    return False


# Function from create game grate
# def drawGrate():
#     for i in range(clientHeight):
#         if i % 12 == 0:
#             for j in range(clientWidth):
#                 pygame.draw.rect(window, myColor['black'], (i, j, 1, 1))
#     for i in range(clientWidth):
#         if i % 12 == 0:
#             for j in range(clientHeight):
#                 pygame.draw.rect(window, myColor['black'], (j, i, 1, 1))

# Function from write snake and her tail
def Snake(blockSize, snakeBody):
    for element in snakeBody:
        pygame.draw.rect(window, myColor['green'], [element[0], element[1], blockSize, blockSize])


# Pygame initialization
pygame.init()
window = pygame.display.set_mode(size)

# Write score
pygame.display.set_caption("Score: " + str(score))

# Game process
done = True
while done:
    pygame.time.delay(60)  # Game speed
    window.fill(myColor['white'])

    #  drawGrate()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        # Read KeyPres event
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            change_pixels_of_x = -snakeSize
            change_pixels_of_y = 0
        elif keys[pygame.K_RIGHT]:
            change_pixels_of_x = snakeSize
            change_pixels_of_y = 0
        elif keys[pygame.K_UP]:
            change_pixels_of_y = -snakeSize
            change_pixels_of_x = 0
        elif keys[pygame.K_DOWN]:
            change_pixels_of_y = snakeSize
            change_pixels_of_x = 0
        elif keys[pygame.K_ESCAPE]:
            done = False

    pygame.draw.rect(window, myColor['red'], (fruitX, fruitY, 12, 12))  # Draw fruit

    pygame.display.set_caption("Score: " + str(score))  # Write score

    lead_x += change_pixels_of_x
    lead_y += change_pixels_of_y

    #window.blit(mySnakeHead, (lead_x, lead_y))
    # Create new fruit after eat
    if lead_x == fruitX and lead_y == fruitY:
        fruitX = random.randrange(0, clientWidth - 12, 12)
        fruitY = random.randrange(0, clientHeight - 12, 12)
        snakeLength += 1
        score += 10

    mySnake = [lead_x, lead_y]
    mySnakeBody.append(mySnake)

    # First game mode
    # if lead_x == clientWidth or lead_y == clientHeight or lead_x == -snakeSize or lead_y == -snakeSize:
    #     done = gameOver()

    # Second game mode
    if lead_x == clientWidth:
        lead_x = -snakeSize
    elif lead_x == -snakeSize:
        lead_x = clientWidth
    if lead_y == clientHeight:
        lead_y = -snakeSize
    elif lead_y == -snakeSize:
        lead_y = clientHeight

    if len(mySnakeBody) > snakeLength:
        del mySnakeBody[0]

    for eachSegment in mySnakeBody[:-1]:
        if eachSegment == mySnake:
            done = gameOver()

    Snake(10, mySnakeBody)
    pygame.display.update()

pygame.quit()

# @Created by NotTorulia
