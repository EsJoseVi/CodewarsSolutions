
unlocked = ["Fire", "Earth", "Air", "Water"]

recepies = {"Earth + Fire":"Lava",
            "Air + Earth":"Dust",
            "Fire + Air":"Smoke",
            "Fire + Water":"Steam",
            "Water + Water":"Puddle",
            "Earth + Water":"Mud",
            "Water + Air":"Mist",
            "Fire + Fire":"Energy",
            "Air + Air":"Pressure",
            "Earth + Earth":"Land",
            "Lava + Earth":"Volcano",
            "Lava+ Air":"Stone",
            "Lava + Pressure":"Granite",
            "Lava + Water":"Obsidian",
            "Dust + Fire":"GunPowder",
            "Steam + Earth":"Geyser",
            "Puddle + Puddle":"Pond",
            "Mud + Fire":"Brick",
            "Energy + Air":"Heat",
            "Energy + Earth":"Earthquake",
            "Pressure + Air":"Wind",
            "Land + Land":"Continent"}


data = input()
while data != "0":
    datal = data.split()
    if datal[0] not in unlocked or datal[2] not in unlocked:
        print(f"{data} --> Nothing happens")
    else:
        unlock = recepies[data]
        if unlock not in unlocked:
            print(f"{data} --> {unlock} unlocked")
            unlocked.append(unlock)
        else:
            print(f"{data} --> {unlock} created")
    data = input()
