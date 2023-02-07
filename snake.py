import pygame
import sys
import random

pygame.init()

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

def drawGame(screen):
    screen.fill(colors["MintyGreen"])
    pygame.draw.rect(screen, snake["color"], (snake["x"], snake["y"], config["blockSize"], config["blockSize"]))
    for tail in snake["tail"]:
        pygame.draw.rect(screen, snake["color"], (tail[0], tail[1], config["blockSize"], config["blockSize"]))
    pygame.draw.rect(screen, food["color"], (food["x"], food["y"], config["blockSize"], config["blockSize"]))
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
        if snake["x"] < 0 or snake["x"] >= config["screen_X"] or snake["y"] < 0 or snake["y"] >= config["screen_Y"]:
            # snake["x"] = config["screen_X"] / 2
            # snake["y"] = config["screen_Y"] / 2
            # snake["direction"] = "none"
            break
        
        # TO CHECK IF SNAKE IS EATING ITSELF #
        if [snake["x"], snake["y"]] in snake["tail"]:
            print("Game Over")
            break

        if snake["x"] == food["x"] and snake["y"] == food["y"]:
            snake["length"] += 1
            snake["tail"].append((snake["x"], snake["y"]))
            randomFood()

        snake["tail"].append((snake["x"], snake["y"]))
        if len(snake["tail"]) > snake["length"]:
            del snake["tail"][0]
            
        
            
        # if len(snake["tail"]) > snake["length"]:
        #         del snake["tail"][0]   
            
            # if snake["length"] % 5 == 0:
            #     config["FPS"] += 5
            

if __name__ == "__main__":
    main()