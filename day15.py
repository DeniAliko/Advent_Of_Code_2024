import useful
data = useful.openFile(15)[0:50]
instructionList = useful.openFile(15)[51:]

# data = useful.openFile(15)[0:10]
# instructionList = useful.openFile(15)[11:]

# data = useful.openFile(15)[0:7]
# instructionList = useful.openFile(15)[8]

instructions = ""
for line in instructionList:
    instructions += line

walls = []
boxes1 = []

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "#":
            walls.append([i, j])
        elif data[i][j] == "O":
            boxes1.append([i, j])
        elif data[i][j] == "@":
            robot1 = [i, j]

class Movable:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def checkMovePx(self):
        trySpot = [self.x+1, self.y] 
        for object in walls:
            if trySpot == object:
                return False
        for object in boxes:
            if trySpot == [object.x, object.y]:
                return object.checkMovePx()
        return True
    def checkMoveNx(self):
        trySpot = [self.x-1, self.y] 
        for object in walls:
            if trySpot == object:
                return False
        for object in boxes:
            if trySpot == [object.x, object.y]:
                return object.checkMoveNx()
        return True
    def checkMovePy(self):
        trySpot = [self.x, self.y+1] 
        for object in walls:
            if trySpot == object:
                return False
        for object in boxes:
            if trySpot == [object.x, object.y]:
                return object.checkMovePy()
        return True
    def checkMoveNy(self):
        trySpot = [self.x, self.y-1] 
        for object in walls:
            if trySpot == object:
                return False
        for object in boxes:
            if trySpot == [object.x, object.y]:
                return object.checkMoveNy()
        return True
    
    def movePx(self):
        if self.checkMovePx():
            trySpot = [self.x+1, self.y] 
            for object in boxes:
                if trySpot == [object.x, object.y]:
                    object.movePx()
            
            self.x += 1
    def moveNx(self):
        if self.checkMoveNx():
            trySpot = [self.x-1, self.y] 
            for object in boxes:
                if trySpot == [object.x, object.y]:
                    object.moveNx()
            
            self.x -= 1
    def movePy(self):
        if self.checkMovePy():
            trySpot = [self.x, self.y+1] 
            for object in boxes:
                if trySpot == [object.x, object.y]:
                    object.movePy()
            
            self.y += 1
    def moveNy(self):
        if self.checkMoveNy():
            trySpot = [self.x, self.y-1] 
            for object in boxes:
                if trySpot == [object.x, object.y]:
                    object.moveNy()
            
            self.y -= 1

boxes = []
for box in boxes1:
    sdf = Movable(box[0], box[1])
    boxes.append(sdf)

robot = Movable(robot1[0], robot1[1])

for dir in instructions:
    if dir == "^":
        robot.moveNx()
    elif dir == ">":
        robot.movePy()
    elif dir == "<":
        robot.moveNy()
    elif dir == "v":
        robot.movePx()

final = 0
for box in boxes:
    final += box.x * 100 + box.y

print(final)
# part 2

gridNew = []
for line in data:
    cacheLine = ""
    for char in line:
        if char == "#":
            cacheLine += "##"
        elif char == "O":
            cacheLine += "O."
        elif char == "@":
            cacheLine += "@."
        elif char == ".":
            cacheLine += ".."
    gridNew.append(cacheLine)

walls = []
boxes1 = []

for i in range(len(gridNew)):
    for j in range(len(gridNew[0])):
        if gridNew[i][j] == "#":
            walls.append([i, j])
        elif gridNew[i][j] == "O":
            boxes1.append([i, j])
        elif gridNew[i][j] == "@":
            robot1 = [i, j]

class Box:
    def __init__(self, x, y1, y2):
        self.x = x
        self.y1 = y1
        self.y2 = y2

    def checkMovePx(self):
        try1 = [self.x+1, self.y1]
        try2 = [self.x+1, self.y2]

        for wall in walls:
            if try1 == wall or try2 == wall:
                return False
            
        gate = True
        for box in boxes:
            if box != self:
                left = [box.x, box.y1]
                right = [box.x, box.y2]
                if try1 == left or try2 == left or try1 == right or try2 == right:
                    if not box.checkMovePx():
                        gate = False

        return gate

    def checkMoveNx(self):
        try1 = [self.x-1, self.y1]
        try2 = [self.x-1, self.y2]

        for wall in walls:
            if try1 == wall or try2 == wall:
                return False
            
        gate = True
        for box in boxes:
            if box != self:
                left = [box.x, box.y1]
                right = [box.x, box.y2]
                if try1 == left or try2 == left or try1 == right or try2 == right:
                    if not box.checkMoveNx():
                        gate = False

        return gate

    def checkMovePy(self):
        try1 = [self.x, self.y1+1]
        try2 = [self.x, self.y2+1]

        for wall in walls:
            if try1 == wall or try2 == wall:
                return False
            
        gate = True
        for box in boxes:
            if box != self:
                left = [box.x, box.y1]
                right = [box.x, box.y2]
                if try1 == left or try2 == left or try1 == right or try2 == right:
                    if not box.checkMovePy():
                        gate = False

        return gate

    def checkMoveNy(self):
        try1 = [self.x, self.y1-1]
        try2 = [self.x, self.y2-1]

        for wall in walls:
            if try1 == wall or try2 == wall:
                return False
            
        gate = True
        for box in boxes:
            if box != self:
                left = [box.x, box.y1]
                right = [box.x, box.y2]
                if try1 == left or try2 == left or try1 == right or try2 == right:
                    if not box.checkMoveNy():
                        gate = False

        return gate

    def movePx(self):
        if self.checkMovePx():
            try1 = [self.x+1, self.y1]
            try2 = [self.x+1, self.y2]

            for box in boxes:
                if box != self:
                    left = [box.x, box.y1]
                    right = [box.x, box.y2]
                    if try1 == left or try1 == right or try2 == left or try2 == right:
                        box.movePx()
            
            self.x += 1

    def moveNx(self):
        if self.checkMoveNx():
            try1 = [self.x-1, self.y1]
            try2 = [self.x-1, self.y2]

            for box in boxes:
                if box != self:
                    left = [box.x, box.y1]
                    right = [box.x, box.y2]
                    if try1 == left or try1 == right or try2 == left or try2 == right:
                        box.moveNx()
            
            self.x -= 1

    def movePy(self):
        if self.checkMovePy():
            try1 = [self.x, self.y1+1]
            try2 = [self.x, self.y2+1]

            for box in boxes:
                if box != self:
                    left = [box.x, box.y1]
                    right = [box.x, box.y2]
                    if try1 == left or try1 == right or try2 == left or try2 == right:
                        box.movePy()
            
            self.y1 += 1
            self.y2 += 1

    def moveNy(self):
        if self.checkMoveNy():
            try1 = [self.x, self.y1-1]
            try2 = [self.x, self.y2-1]

            for box in boxes:
                if box != self:
                    left = [box.x, box.y1]
                    right = [box.x, box.y2]
                    if try1 == left or try1 == right or try2 == left or try2 == right:
                        box.moveNy()
            
            self.y1 -= 1
            self.y2 -= 1

class Movable:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def checkMovePx(self):
        trySpot = [self.x+1, self.y] 
        for object in walls:
            if trySpot == object:
                return False
        for object in boxes:
            if trySpot == [object.x, object.y1] or trySpot == [object.x, object.y2]:
                return object.checkMovePx()
        return True
    def checkMoveNx(self):
        trySpot = [self.x-1, self.y] 
        for object in walls:
            if trySpot == object:
                return False
        for object in boxes:
            if trySpot == [object.x, object.y1] or trySpot == [object.x, object.y2]:
                return object.checkMoveNx()
        return True
    def checkMovePy(self):
        trySpot = [self.x, self.y+1] 
        for object in walls:
            if trySpot == object:
                return False
        for object in boxes:
            if trySpot == [object.x, object.y1] or trySpot == [object.x, object.y2]:
                return object.checkMovePy()
        return True
    def checkMoveNy(self):
        trySpot = [self.x, self.y-1] 
        for object in walls:
            if trySpot == object:
                return False
        for object in boxes:
            if trySpot == [object.x, object.y1] or trySpot == [object.x, object.y2]:
                return object.checkMoveNy()
        return True
    
    def movePx(self):
        if self.checkMovePx():
            trySpot = [self.x+1, self.y] 
            for object in boxes:
                if trySpot == [object.x, object.y1] or trySpot == [object.x, object.y2]:
                    object.movePx()
            
            self.x += 1
    def moveNx(self):
        if self.checkMoveNx():
            trySpot = [self.x-1, self.y] 
            for object in boxes:
                if trySpot == [object.x, object.y1] or trySpot == [object.x, object.y2]:
                    object.moveNx()
            
            self.x -= 1
    def movePy(self):
        if self.checkMovePy():
            trySpot = [self.x, self.y+1] 
            for object in boxes:
                if trySpot == [object.x, object.y1] or trySpot == [object.x, object.y2]:
                    object.movePy()
            
            self.y += 1
    def moveNy(self):
        if self.checkMoveNy():
            trySpot = [self.x, self.y-1] 
            for object in boxes:
                if trySpot == [object.x, object.y1] or trySpot == [object.x, object.y2]:
                    object.moveNy()
            
            self.y -= 1

boxes = []
for box in boxes1:
    sdf = Box(box[0], box[1], box[1]+1)
    boxes.append(sdf)

robot = Movable(robot1[0], robot1[1])

for dir in instructions:
    if dir == "^":
        robot.moveNx()
    elif dir == ">":
        robot.movePy()
    elif dir == "<":
        robot.moveNy()
    elif dir == "v":
        robot.movePx()

final = 0
for box in boxes:
    # print(box.x1, box.y)
    final += box.x * 100 + box.y1

print(final)