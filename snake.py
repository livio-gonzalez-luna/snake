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
RED = (255, 0, 0)
LIGHT_GREEN = (40, 210, 180)
LIGH_BLUE = (0, 255, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

snake = {
    "easy": {
        "x": SCREEN_WIDTH / 2,
        "y": SCREEN_HEIGHT / 2,
        "direction": "none",
        "length": 2,
        "tail": [],
        "speed": 5,
        "size": 20
        
    },
    "medium": {
        "x": SCREEN_WIDTH / 2,
        "y": SCREEN_HEIGHT / 2,
        "direction": "none",
        "length": 2,
        "tail": [],
        "speed": 10,
        "size": 30
    },
    "hard": {
        "x": SCREEN_WIDTH / 2,
        "y": SCREEN_HEIGHT / 2,
        "direction": "none",
        "length": 2,
        "tail": [],
        "speed": 15,
        "size": 40
    }
}


food = {
    "x": 0,
    "y": 0,
}

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def randomFood(snake, difficulty, size):

    with open("snake.json", "r") as file:
        snake = load(file)
        
        if difficulty == "easy":
            food["x"] = round(random.randrange(0, SCREEN_WIDTH - snake["easy"][size]) / snake["easy"][size]) * snake["easy"][size]
            food["y"] = round(random.randrange(0, SCREEN_HEIGHT - snake["easy"][size]) / snake["easy"][size]) * snake["easy"][size]
        elif difficulty == "medium":
            food["x"] = round(random.randrange(0, SCREEN_WIDTH - snake["medium"][size]) / snake["medium"][size]) * snake["medium"][size]
            food["y"] = round(random.randrange(0, SCREEN_HEIGHT - snake["medium"][size]) / snake["medium"][size]) * snake["medium"][size]
        elif difficulty == "hard":
            food["x"] = round(random.randrange(0, SCREEN_WIDTH - snake["hard"][size]) / snake["hard"][size]) * snake["hard"][size]
            food["y"] = round(random.randrange(0, SCREEN_HEIGHT - snake["hard"][size]) / snake["hard"][size]) * snake["hard"][size]
    
    # food["x"] = round(random.randrange(0, SCREEN_WIDTH - snake["difficulty"][size]) / snake["difficulty"][size]) * snake["difficulty"][size]
    # food["y"] = round(random.randrange(0, SCREEN_HEIGHT - snake["difficulty"][size]) / snake["size"]) * snake["size"]

# def check_user(username, difficulty, data_score):
#     if username not in data_score[difficulty]:
#         return True
#     return False

# def registerScore(username, snake["length"], difficulty):
#     with open("scores.json", "r") as file:
#         data_score = load(file)

#     if check_user(username,difficulty,data_score):
#         data_score[difficulty][username]=[]
#         print(data_score[difficulty])

#     data_score[difficulty][username].append(snake_len)

#     with open("scores.json", "w") as file:
#         dump(data_score, file, indent=4)


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
                    
                    diffChoice()

        pygame.display.update()

def diffChoice():
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_e:
                    main()
                elif event.key == pygame.K_m:
                    main()
                elif event.key == pygame.K_h:
                    main()

        pygame.display.update()

def drawGame(snake):
    # difficulty = snake["difficulty"]
    screen.fill(LIGHT_GREEN)
    score = snake["length"]
    
    # Score #
    SCORE_TEXT = SCORE_FONT.render("Score: " + str(score), 1, WHITE)
    SCORE_TEXT_RECT = SCORE_TEXT.get_rect(center=(400, 20))
    screen.blit(SCORE_TEXT, SCORE_TEXT_RECT)
    
    # Snake #
    pygame.draw.rect(screen, RED, (snake["x"], snake["y"], snake["size"], snake["size"]))
    for tail in snake["tail"]:
        pygame.draw.rect(screen, RED, (tail[0], tail[1], snake["size"], snake["size"]))
    
    # Food #
    pygame.draw.rect(screen, LIGH_BLUE, (food["x"], food["y"], snake["size"], snake["size"]))
    pygame.display.update()

def main():
    randomFood()
    while True:
        clock.tick(snake["speed"])
        drawGame()
        
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
            snake["y"] -= snake["size"]
        elif snake["direction"] == "down":
            snake["y"] += snake["size"]
        elif snake["direction"] == "left":
            snake["x"] -= snake["size"]
        elif snake["direction"] == "right":
            snake["x"] += snake["size"]

        
        # Snake wrap around #
        if snake["x"] < 0 or snake["x"] >= SCREEN_WIDTH or snake["y"] < 0 or snake["y"] >= SCREEN_HEIGHT:
            # registerScore(username, snake["length"], difficulty)
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