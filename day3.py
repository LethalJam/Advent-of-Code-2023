import parser_util

matrix = parser_util.readAsMatrix( # [y][x]
    "inputs/3.txt", "string", "")
maxY = len(matrix)
maxX = len(matrix[0])
print(maxY)
print(maxX)

def check_pos(y,x):
    if y >= 0 and x >= 0 and y < maxY and x < maxX:
        return matrix[y][x] != "."
    else: # Out of Range
        return False

def adjacent_symbol_middle(pos):
    y = pos[0]
    x = pos[1]

    if check_pos(y-1,x): return True
    if check_pos(y+1,x): return True
    return False

def adjacent_symbol_edge(pos : tuple(), dir : int()):
    y = pos[0]
    x = pos[1]

    if check_pos(y-1,x): return True
    if check_pos(y+1,x): return True

    if check_pos(y-1,x+dir): return True
    if check_pos(y,x+dir): return True
    if check_pos(y+1,x+dir): return True
    return False

def adjacent_symbol_edges(left : tuple(), right : tuple()):
    adjL = adjacent_symbol_edge(left, -1)
    adjR = adjacent_symbol_edge(right, 1)
    return adjL or adjR

def check_adjacencies(posNums : list()):
    edges = adjacent_symbol_edges(posNums[0], posNums[-1])
    rests = False
    if len(posNums) > 2:
        rest = posNums[1:-1]
        for r in rest:
            rests = adjacent_symbol_middle(r)
            if rests: break
    return edges or rests
    

def build_number(posNums : list()):
    numStr = ""
    for pos in posNums:
        numStr += matrix[pos[0]][pos[1]]
    return int(numStr)

yP = 0
xP = 0
partNumbers = []

for row in matrix:

    numBuf = []
    for x in row:
        if x.isnumeric():
            numBuf.append((yP,xP))
        else:
            if len(numBuf) > 0:
                if check_adjacencies(numBuf):
                    partNumbers += [build_number(numBuf)]

            numBuf = []

        xP += 1
    if len(numBuf) > 0:
        if check_adjacencies(numBuf):
            partNumbers += [build_number(numBuf)]

    xP = 0
    yP += 1

print(partNumbers)
print(sum(partNumbers))