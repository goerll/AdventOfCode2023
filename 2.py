with open("input.txt", "r") as file:
    line_count = 0
    game_sets = []
    cube_amount = ""
    possible_game = True
    possible_games = []

    cubeDict = {
        "r":12,
        "g":13,
        "b":14,
    }
    
    for line in file:
        line_count += 1

        if line_count < 10:
            line = line[7:].strip()
        elif line_count < 100:
            line = line[8:].strip()
        else:
            line = line[9:].strip()
        
        line = line.replace(";", ",")
        game_sets = line.split(", ")

        for i in range(len(game_sets)):
            cube_amount = ""
            for j in range(len(game_sets[i])-1):
                char = game_sets[i][j]
                if char.isdigit():
                    cube_amount += char
                else:
                    if cubeDict[game_sets[i][j+1]] < int(cube_amount):
                        possible_game = False
                    break;
        if possible_game:
            possible_games.append(line_count)

        #Resetting var for next iteration
        possible_game = True

    print(sum(possible_games))
