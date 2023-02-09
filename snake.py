import pygame
import sys
import random
from json import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BUTTON_FONT = pygame.font.Font(None, 36) 
TITLE_FONT = pygame.font.Font(None, 50)
SCORE_FONT = pygame.font.SysFont("comicsans", 30)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_GREEN = (40, 210, 180)
LIGH_BLUE = (0, 255, 255)


config = {
    "blockSize": 20,
    "FPS": 10
}

snake = {
    "x": SCREEN_WIDTH / 2,
    "y": SCREEN_HEIGHT / 2,
    "direction": "none",
    "length": 0,
    "tail": []
}

food = {
    "x": 0,
    "y": 0,
}

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def randomFood():
    food["x"] = round(random.randrange(0, SCREEN_WIDTH - config["blockSize"]) / config["blockSize"]) * config["blockSize"]
    food["y"] = round(random.randrange(0, SCREEN_HEIGHT - config["blockSize"]) / config["blockSize"]) * config["blockSize"]

def registerScore():
    global username
    with open("scores.json", "r") as file:
        data = load(file)
        
        data["scores"].append({
            "name": username,
            "score": snake["length"]
        })
    with open("scores.json", "w") as file:
        dump(data, file, indent=4)

def menu():
    run = True
    username = ""

    while run:
        screen.fill(BLACK)

        MENU_TEXT = TITLE_FONT.render("SNAKE GAME", True, (WHITE))
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 80))
        screen.blit(MENU_TEXT, MENU_RECT)

        LABEL_TEXT = BUTTON_FONT.render("Enter your name:", 1, WHITE)
        LABEL_RECT = LABEL_TEXT.get_rect(center=(400, 150))
        screen.blit(LABEL_TEXT, LABEL_RECT)
        
        INPUT_TEXT = BUTTON_FONT.render(username, True, WHITE)
        INPUT_RECT = INPUT_TEXT.get_rect(center=(400, 200))
        screen.blit(INPUT_TEXT, INPUT_RECT)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.unicode.isalpha():
                    username += event.unicode

                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]

                elif event.key == pygame.K_RETURN:
                    LABEL_NAME = SCORE_FONT.render("Name Added!", 1, WHITE)
                    LABEL_NAME_RECT = LABEL_NAME.get_rect(center=(400, 250))
                    screen.blit(LABEL_NAME, LABEL_NAME_RECT)
                    
                    pygame.display.update()
                    pygame.time.wait(2000)
                    
                    main()

        pygame.display.update()
    
def drawGame(screen):
    screen.fill(LIGHT_GREEN)
    score = snake["length"]
    
    # Score #
    SCORE_TEXT = SCORE_FONT.render("Score: " + str(score), 1, WHITE)
    SCORE_TEXT_RECT = SCORE_TEXT.get_rect(center=(400, 20))
    screen.blit(SCORE_TEXT, SCORE_TEXT_RECT)
    
    # Snake #
    pygame.draw.rect(screen, RED, (snake["x"], snake["y"], config["blockSize"], config["blockSize"]))
    for tail in snake["tail"]:
        pygame.draw.rect(screen, RED, (tail[0], tail[1], config["blockSize"], config["blockSize"]))
    
    # Food #
    pygame.draw.rect(screen, LIGH_BLUE, (food["x"], food["y"], config["blockSize"], config["blockSize"]))
    pygame.display.update()

def main():
    randomFood()
    while True:
        clock.tick(config["FPS"])
        drawGame(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if snake["direction"] != "down":
                        snake["direction"] = "up"
                elif event.key == pygame.K_DOWN:
                    if snake["direction"] != "up":
                        snake["direction"] = "down"
                elif event.key == pygame.K_LEFT:
                    if snake["direction"] != "right":
                        snake["direction"] = "left"
                elif event.key == pygame.K_RIGHT:
                    if snake["direction"] != "left":
                        snake["direction"] = "right"


        # Snake movement #   
        if snake["direction"] == "up":
            snake["y"] -= config["blockSize"]
        elif snake["direction"] == "down":
            snake["y"] += config["blockSize"]
        elif snake["direction"] == "left":
            snake["x"] -= config["blockSize"]
        elif snake["direction"] == "right":
            snake["x"] += config["blockSize"]

        
        # Snake wrap around #
        if snake["x"] < 0 or snake["x"] >= SCREEN_WIDTH or snake["y"] < 0 or snake["y"] >= SCREEN_HEIGHT:
            registerScore()
            menu()
        
        # TO CHECK IF SNAKE IS EATING FOOD #
        if snake["x"] == food["x"] and snake["y"] == food["y"]:
            snake["length"] += 1
            randomFood()
            if snake["length"] > 0:
                snake["tail"].append((snake["x"], snake["y"]))
                

        # ADDING TAIL TO SNAKE #
        if snake["length"] > 0:
            snake["tail"].append((snake["x"], snake["y"]))

        # TO CHECK IF SNAKE IS EATING ITSELF #
        if [snake["x"], snake["y"]] in snake["tail"]:
            menu()

        # TO START ADDING TAIL TO SNAKE #
        if len(snake["tail"]) > snake["length"]:
            del snake["tail"][0]
            
if __name__ == "__main__":
    menu()