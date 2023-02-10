from json import *

with open("snake.json", "r") as file:
    contents = file.read().strip()
    gameConfig = loads(contents)

print(gameConfig["snake"]["easy"]["size"])