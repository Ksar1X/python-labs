from stars import *

N = 4
actions = {
    "L": lambda: [vertical(N), horizontal(N)],
    "E": lambda: [horizontal(N), vertical(1), horizontal(N), vertical(1), horizontal(N)]
}

user_answer = str(input("What do you want to draw? E or l?"))
if user_answer.upper() == "L":
    print(actions["L"]())
elif user_answer.upper() == "E":
    print(actions["E"]())
else:
    print("I can't draw it :(")

