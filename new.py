from json import *
import pygame
import random


pygame.init()

# CONSTANTS #
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED = (255, 0, 0)
LIGHT_GREEN = (40, 210, 180)
DARK_GREEN = (0, 100, 0)
LIGHT_BLUE = (0, 255, 255)

BUTTON_FONT = pygame.font.Font(None, 36) 
TITLE_FONT = pygame.font.Font(None, 50)
SCORE_FONT = pygame.font.SysFont("comicsans", 30)

with open("gameConfig.json", "r") as file:
    contents = file.read().strip()
    gameConfig = loads(contents)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def random_food(difficulty):
    snakeSize = gameConfig["snake"][difficulty]["size"]
    x = round(random.randrange(0, SCREEN_WIDTH - snakeSize) / snakeSize) * snakeSize + snakeSize / 2
    y = round(random.randrange(0, SCREEN_HEIGHT - snakeSize) / snakeSize) * snakeSize + snakeSize / 2
    gameConfig["food"]["x"] = x 
    gameConfig["food"]["y"] = y
    
def menu():
    run = True
    while run:
        screen.fill(BLACK)

        MENU_TEXT = TITLE_FONT.render("SNAKE GAME", True, (WHITE))
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 80))
        screen.blit(MENU_TEXT, MENU_RECT)

        LABEL_TEXT = BUTTON_FONT.render("Choose difficulty:", 1, WHITE)
        LABEL_RECT = LABEL_TEXT.get_rect(center=(400, 150))
        screen.blit(LABEL_TEXT, LABEL_RECT)

        EASY_TEXT = BUTTON_FONT.render("Easy", 1, WHITE)
        EASY_RECT = EASY_TEXT.get_rect(center=(400, 200))
        screen.blit(EASY_TEXT, EASY_RECT)

        MEDIUM_TEXT = BUTTON_FONT.render("Medium", 1, WHITE)
        MEDIUM_RECT = MEDIUM_TEXT.get_rect(center=(400, 250))
        screen.blit(MEDIUM_TEXT, MEDIUM_RECT)

        HARD_TEXT = BUTTON_FONT.render("Hard", 1, WHITE)
        HARD_RECT = HARD_TEXT.get_rect(center=(400, 300))
        screen.blit(HARD_TEXT, HARD_RECT)

        pygame.display.update()
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_e:
                    game("easy")
                elif event.key == pygame.K_m:
                    game("medium")
                elif event.key == pygame.K_h:
                    game("hard")
         


def draw(difficulty):
    screen.fill(LIGHT_BLUE)
    score = gameConfig["snake"][difficulty]["length"] - 2
    snakeSize = gameConfig["snake"][difficulty]["size"]
    snakeTail = gameConfig["snake"][difficulty]["tail"] 
    snakeX = gameConfig["snake"][difficulty]["x"]
    snakeY = gameConfig["snake"][difficulty]["y"]
    
    # Score #
    score_text = SCORE_FONT.render("Score: " + str(score), 1, DARK_GREEN)
    score_text_rect = score_text.get_rect(center=(SCREEN_WIDTH - 100, 50))
    screen.blit(score_text, score_text_rect)

    ## SNAKE ##
    x = snakeX - snakeSize / 2
    y = snakeY - snakeSize / 2 
    pygame.draw.rect(screen, DARK_GREEN, (x, y, snakeSize, snakeSize))
    
    for tail in snakeTail:
        tailX = tail[0] - snakeSize / 2
        tailY = tail[1] - snakeSize / 2
        pygame.draw.rect(screen, DARK_GREEN, (tailX, tailY, snakeSize, snakeSize))
    
    # Food #
    foodX = gameConfig["food"]["x"] - snakeSize / 2 - 5
    foodY = gameConfig["food"]["y"] - snakeSize / 2 - 5
    pygame.draw.rect(screen, RED, (foodX, foodY, snakeSize, snakeSize))
    
    pygame.display.update()



def game(difficulty):
    random_food(difficulty)

    while True:
        clock.tick(gameConfig["snake"][difficulty]["speed"])
        draw(difficulty)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if gameConfig["snake"][difficulty]["direction"] != "down":
                        gameConfig["snake"][difficulty]["direction"] = "up"
                elif event.key == pygame.K_DOWN:
                    if gameConfig["snake"][difficulty]["direction"] != "up":
                        gameConfig["snake"][difficulty]["direction"] = "down"
                elif event.key == pygame.K_LEFT:
                    if gameConfig["snake"][difficulty]["direction"] != "right":
                        gameConfig["snake"][difficulty]["direction"] = "left"
                elif event.key == pygame.K_RIGHT:
                    if gameConfig["snake"][difficulty]["direction"] != "left":
                        gameConfig["snake"][difficulty]["direction"] = "right"

        if gameConfig["snake"][difficulty]["direction"] == "up":
            gameConfig["snake"][difficulty]["y"] -= gameConfig["snake"][difficulty]["size"]
        elif gameConfig["snake"][difficulty]["direction"] == "down":
            gameConfig["snake"][difficulty]["y"] += gameConfig["snake"][difficulty]["size"]
        elif gameConfig["snake"][difficulty]["direction"] == "left":
            gameConfig["snake"][difficulty]["x"] -= gameConfig["snake"][difficulty]["size"]
        elif gameConfig["snake"][difficulty]["direction"] == "right":
            gameConfig["snake"][difficulty]["x"] += gameConfig["snake"][difficulty]["size"]

        # BORDER COLLISION #
        if (gameConfig["snake"][difficulty]["x"] + 5) < 0 or (gameConfig["snake"][difficulty]["x"] + 5) > SCREEN_WIDTH or (gameConfig["snake"][difficulty]["y"] + 5) < 0 or (gameConfig["snake"][difficulty]["y"] + 5) > SCREEN_HEIGHT:
            menu()

        # FOOD COLLISION #
        if (gameConfig["snake"][difficulty]["x"] + 5) == gameConfig["food"]["x"] and (gameConfig["snake"][difficulty]["y"] + 5) == gameConfig["food"]["y"]:
            random_food(difficulty)
            gameConfig["snake"][difficulty]["length"] += 1

        # ADD TAIL #
        gameConfig["snake"][difficulty]["tail"].append((gameConfig["snake"][difficulty]["x"], gameConfig["snake"][difficulty]["y"]))
        if len(gameConfig["snake"][difficulty]["tail"]) > gameConfig["snake"][difficulty]["length"]:
            del gameConfig["snake"][difficulty]["tail"][0]
        
        # SNAKE COLLISION #
        for tail in gameConfig["snake"][difficulty]["tail"][:-1]:
            if tail == (gameConfig["snake"][difficulty]["x"], gameConfig["snake"][difficulty]["y"]):
                menu()


if __name__ == "__main__":
    menu()


