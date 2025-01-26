mx, my, okx, oky, sx, sy,sec = list(map(int,input().split(",")))

print(f"MouseMove{okx - mx, oky - my}")
print("While(True)")
print('    Click(1, "Left")')
print(f"    MouseMove{sx - okx, sy - oky}")
print('    Click(1, "Left")')
print(f"    Wait({sec*1000})")
print(f"    MouseMove{okx - sx, oky - sy}")