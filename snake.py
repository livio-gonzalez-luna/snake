import pygame
import sys
import random
from json import *


pygame.init()

BUTTON_FONT = pygame.font.Font(None, 36) 
TITLE_FONT = pygame.font.Font(None, 50)
SCORE_FONT = pygame.font.SysFont("comicsans", 30)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


config = {
    "screen_X": 800,
    "screen_Y": 600,
    "screenTitle": "Snake Game",
    "blockSize": 20,
    "FPS": 10
}

colors = {
    "MintyGreen": (40, 210, 180),
    "Red": (255, 0, 0),
    "lightBlue": (0, 255, 255)
}

snake = {
    "x": config["screen_X"] / 2,
    "y": config["screen_Y"] / 2,
    "direction": "none",
    "color": colors["Red"],
    "length": 0,
    "tail": []
}

food = {
    "x": 0,
    "y": 0,
    "color": colors["lightBlue"]
}

screen = pygame.display.set_mode((config["screen_X"], config["screen_Y"]))
pygame.display.set_caption(config["screenTitle"])
clock = pygame.time.Clock()

def randomFood():
    food["x"] = round(random.randrange(0, config["screen_X"] - config["blockSize"]) / config["blockSize"]) * config["blockSize"]
    food["y"] = round(random.randrange(0, config["screen_Y"] - config["blockSize"]) / config["blockSize"]) * config["blockSize"]


def menu():
    run = True
    username = ""

    while run:
        screen.fill(BLACK)

        MENU_TEXT = TITLE_FONT.render("SNAKE GAME", True, (WHITE))
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 80))
        screen.blit(MENU_TEXT, MENU_RECT)

        LABEL_TEXT = BUTTON_FONT.render("Enter your name:", 1, (0, 255, 0))
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
                if event.unicode.isalpha():
                    username += event.unicode
                elif event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]

                elif event.key == pygame.K_RETURN:
                    LABEL_TEXT = SCORE_FONT.render("Name Added!", 1, WHITE)
                    screen.blit(LABEL_TEXT, (config["screen_X"] / 2 - LABEL_TEXT.get_width() / 2, 150))
                    main(username)
            
            

        pygame.display.update()
    




def drawGame(screen):
    screen.fill(colors["MintyGreen"])
    score = snake["length"]
    
    # draw score #
    score_text = SCORE_FONT.render("Score: " + str(score), 1, WHITE)
    screen.blit(score_text, (20, 20))
    
    # draw snake #
    pygame.draw.rect(screen, snake["color"], (snake["x"], snake["y"], config["blockSize"], config["blockSize"]))
    for tail in snake["tail"]:
        pygame.draw.rect(screen, snake["color"], (tail[0], tail[1], config["blockSize"], config["blockSize"]))
    
    # draw food #
    pygame.draw.rect(screen, food["color"], (food["x"], food["y"], config["blockSize"], config["blockSize"]))
    pygame.display.update()


def main(username):
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
        if snake["x"] < 0 or snake["x"] >= config["screen_X"] or snake["y"] < 0 or snake["y"] >= config["screen_Y"]:
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

        
        
        if len(snake["tail"]) > snake["length"]:
            del snake["tail"][0]
            # if snake["length"] % 5 == 0:
            #     config["FPS"] += 5
            
if __name__ == "__main__":
    menu()