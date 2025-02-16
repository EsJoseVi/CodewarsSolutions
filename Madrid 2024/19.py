goku, vegeta, piccolo = list(map(int,input().split(",")))
gokus, vegetas, piccolos = [0,0,0]
lobstacles = {".":1,"@":3,"_":5}

def character(name,persona,personas,obstacle):
    if obstacle == " ":
            personas += persona
            print(f"{name} advanced to {personas} Km")
    elif persona > 0:
        persona -= lobstacles[obstacle]
        if persona <= 0:
            print(f"{name} died in the Km {personas}")
        else:
            personas += persona
            print(f"{name} found a {-lobstacles[obstacle]} points obstacle then advanced to {personas} Km")
    return [persona,personas]

for i in range(5):
    print(f"Turn {i+1}:")
    obstacles = input().split("|")
    obstacles = obstacles[1:4]
    goku, gokus = character("Goku",goku,gokus,obstacles[0])
    vegeta, vegetas = character("Vegeta",vegeta,vegetas,obstacles[1])
    piccolo, piccolos = character("Piccolo",piccolo,piccolos,obstacles[2])
possible = {"Vegeta":vegetas,"Goku":gokus,"Piccolo":piccolos}
sorted(possible,key=lambda x:x[1], reverse=True)
keey = list(possible.keys())[0]
print(f"At the end of the 5 turns, the winner is {keey} with {possible[keey]} Km")