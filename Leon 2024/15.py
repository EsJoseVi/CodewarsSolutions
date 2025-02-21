# Calleja

n = float(input())

capacity = (13000000 * 50) - 201

n = n / 60

time = capacity / (n*200)

seconds = time % 60

time -= seconds

time = time / 60

minutes = time % 60

time -= minutes

time = time / 60

hours = time % 60

time -= hours

days = time / 24

print(f"{round(days)} days, {round(hours)} hours, {round(minutes)} minutes and {round(seconds)} seconds")

