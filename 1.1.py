with open("input.txt", "r") as file:
    current_number = ""
    line_content = []
    line_numbers = []
    numbers = []

    numDict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for line in file:
        print(line, end="")

        firstNumFound = False
        for i in range(len(line)):
            if firstNumFound == False:
                searching = line[0:i+1]
                if line[i].isdigit():
                    line_numbers.append(line[i])
                    firstNumFound = True
                else:
                    for key in numDict.keys():
                        if key in searching:
                            line_numbers.append(numDict[key])
                            firstNumFound = True
    

        secondNumFound = False
        for i in range(len(line)):
            if secondNumFound == False:
                searching = line[-i-1:]
                if line[-i-1].isdigit():
                    line_numbers.append(line[-i-1])
                    secondNumFound = True
                else:
                    for key in numDict.keys():
                        if key in searching:
                            line_numbers.append(numDict[key])
                            secondNumFound = True
        print(line_numbers)
        numbers.append(int(str(line_numbers[0]) + str(line_numbers[-1])))
        line_numbers = []
print(sum(numbers))

