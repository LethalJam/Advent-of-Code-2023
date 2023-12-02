import parser_util

games = parser_util.readList(
    "inputs/2.txt", "string", False, False)

colorMaxDic = {"red" : 12, "green" : 13, "blue" : 14}
IdSum = 0
PowerSum = 0

for g in games:

    gamePossible = True
    [gameTag, data] = g.split(": ")
    Id = int(gameTag.split(" ")[-1])
    sets = data.split("; ")

    # Part 2 variable
    colorMinDic = {"red" : 0, "green" : 0, "blue" : 0}

    for set in sets:
        cCubes = set.split(", ") # Example: 3 blue
        for c in cCubes:
            [num, color] = c.split(" ")

            # Part 1
            if int(num) > colorMaxDic[color]:
                gamePossible = False

            # Part 2
            if int(num) > colorMinDic[color]:
                colorMinDic[color] = int(num)

    # Part 1 solution
    if gamePossible:
        IdSum += Id
    
    # Part 2 solution
    power = 1
    for p in colorMinDic.values():
        power *= p
    PowerSum += power
    print(Id, ", ", power)


print("Sum of valid Ids is: ", IdSum)
print("Sum of powers of min cubes is: ", PowerSum)