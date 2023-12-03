def readList(fileName, type, removeBlanks, keepNewLine):
    file = open(fileName, "r")
    out = file.readlines()
    if not keepNewLine:
        out = [s.replace('\n', '') for s in out]
    if removeBlanks:
        out = [s for s in out if len(s) != 0]

    if (type == "string"):
        return out
    elif (type == "int"):
        return [int(s) for s in out]


def readAsMatrix(fileName, type, sep):
    input = readList(fileName, type, True, False)

    matrix = list()
    for i in input:
        if sep != "":
            matrix.append(i.split(sep))
        else:
            matrix.append(i)
    return matrix
