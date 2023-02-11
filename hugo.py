from json import *

def check_user(username,difficulty,data_score):
    if username not in data_score[difficulty]:
        return True
    return False
    

def registerScore(username,snake_len,difficulty):
    with open("gameScores.json", "r") as file:
        data_score = load(file)

    if check_user(username,difficulty,data_score):
        print("user not found")
        data_score[difficulty][username]=[]
        print(data_score[difficulty])


    data_score[difficulty][username].append(snake_len)

    with open("gameScores.json", "w") as file:
        dump(data_score, file, indent=4)


registerScore("Hugo",99,"easy")