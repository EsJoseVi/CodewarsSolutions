## El de jesus calleja

import math
v = 60 / float(input())

space = 13000000 * 50 - 201

time = (space * v) / 200
seconds = round(time % 60)
minutes = round(((time - seconds) / 60) % 60)
hours = (time - seconds) / 60
hours = (hours - minutes) / 60
hours = hours % 24
hours = round(hours)
days = math.floor(time / (24 * 60**2))
print(f"{days} days, {hours} hours, {minutes} minutes and {seconds} seconds")