directions = {"Left":1,"Right":3}
n = input()
direction = 0
path = []
while n != "End":
    n = n[5:]
    n = n[:-1]
    if n.isdigit():
        path.append((direction,int(n)))
    else:
        direction += directions[n]
        direction = direction % 4
    n = input()

currentx = 0
currenty = 0
bestx = [0,0]
besty = [0,0]

for i in path:
    if i[0] == 0:
        currenty -= i[1]
    if i[0] == 1:
        currentx += i[1]
    if i[0] == 2:
        currenty += i[1]
    if i[0] == 3:
        currentx -= i[1]
    if currentx < 0:
        if bestx[0] > currentx:
            bestx[0] = currentx
    if currentx > 0:
        if bestx[1] < currentx:
            bestx[1] = currentx
    if currenty < 0:
        if besty[0] > currenty:
            besty[0] = currenty
    if currenty > 0:
        if besty[1] < currenty:
            besty[1] = currenty
            
size = (abs(bestx[0]) + bestx[1], abs(besty[0])  + besty[1])
start = (abs(bestx[0]),abs(besty[1]))

drawing = []
for y in range(size[1]+1):
    if y == start[1]:
        drawing.append(" "*abs(bestx[0])+"S"+" "*bestx[1])
    else:
        drawing.append(" "*(size[0]+1))

##Drawing
def drawHorizontal(canvas,start,length):
    line = list(canvas[start[1]])
    for i in range(abs(length)):
        if length > 0:
            line[start[0]+i] = "X"
        else:
            line[start[0]-i] = "X"
    canvas[start[1]] = "".join(line)

def drawVertical(canvas,start,length):
    n = 1
    for i in range(abs(length)):
        if length < 0:
            n = -1
        line = canvas[start[1]+(i*n)]
        line = list(line)
        line[start[0]] = "X"
        canvas[start[1]+(i*n)] = "".join(line)

n = 1
for i in path:
    if i[0] % 2 == 0:
        if i[0] == 2:
            n = -1
        else:
            n = 1
        start = (start[0],start[1]+n)
        drawVertical(drawing,start,n*i[1])
        start = (start[0],start[1]+n*i[1]-n)
    else:
        if i[0] == 3:
            n = -1
        else:
            n = 1
        start = (start[0]+n,start[1])
        drawHorizontal(drawing,start,n*i[1])
        start = (start[0]+n*i[1]-n,start[1])

line = list(drawing[start[1]])
line[start[0]] = "F"
drawing[start[1]] = "".join(line)

for i in drawing:
    print(i)
