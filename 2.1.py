with open("input.txt", "r") as file:
    line_count = 0
    game_sets = []
    game_power = 1
    game_powers = []

    for line in file:

        minCubes = {
            "r":0,
            "g":0,
            "b":0,
        }

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
                    if minCubes[game_sets[i][j+1]] < int(cube_amount):
                        minCubes[game_sets[i][j+1]] = int(cube_amount)
                    break;
        for i in minCubes.values():
            game_power *= i

        game_powers.append(game_power)
        game_power = 1

    print(game_powers)
    print(sum(game_powers))
