import parser_util

lines = parser_util.readList(
    "inputs/1.txt", "string", False, False)

numDic = {"one" : "1",
          "two" : "2",
          "three" : "3",
          "four" : "4",
          "five" : "5",
          "six" : "6",
          "seven" : "7",
          "eight" : "8",
          "nine" : "9"}

numbers = []
sum = 0

for l in lines:
    strNum = ""
    numBuf = ""

    # PARSE
    for c in l:

        if c.isnumeric():
            if len(strNum) > 1:
                strNum = strNum[0] # Overwrite last no
            strNum += c
            numBuf = "" # Reset buf
        else:
            numBuf += c

            for numWord in numDic.keys():
                if numWord in numBuf: # Check if buf contains a number word

                    if len(strNum) > 1:
                        strNum = strNum[0] # Overwrite last no
                    strNum += numDic[numWord] # Add the number to string if so

                    numBuf =  numBuf[-1] # Reset buf and keep last symbol in case of combined LMAO
                    break

    # CONVERT
    if len(strNum) < 2:
        strNum += strNum[0]
    numbers += [int(strNum)]
    sum += int(strNum)

print(numbers)
print(sum)