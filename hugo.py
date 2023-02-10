from json import *

def check_user(username,difficulty,data_score):
    if username not in data_score[difficulty]:
        return True
    return False
    

def registerScore(username,snake_len,difficulty):
    with open("scores.json", "r") as file:
        data_score = load(file)

    if check_user(username,difficulty,data_score):
        data_score[difficulty][username]=[]
        print(data_score[difficulty])

    data_score[difficulty][username].append(snake_len)

    with open("scores.json", "w") as file:
        dump(data_score, file, indent=4)


registerScore("Hugo",99,"easy")