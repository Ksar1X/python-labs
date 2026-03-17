from lab3_task5 import stars

N = 4
actions = {
    "L": lambda: [stars.vertical(N), stars.horizontal(N)],
    "E": lambda: [stars.horizontal(N), stars.vertical(1), stars.horizontal(N), stars.vertical(1), stars.horizontal(N)]
}

user_answer = str(input("What do you want to draw? E or l?")).upper()
if user_answer in actions:
    actions[user_answer]()
else:
    print("I can't draw it :(")

