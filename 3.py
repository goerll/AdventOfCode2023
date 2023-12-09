with open("inputtest.txt", "r") as file:
    #Storing the file's vertical and horizontal length
    
    #Possible symbols
    symbols = ["&", "*", "#", "@", "%", "/", "$", "=", "-", ")", "(", "!", "+"]
    parts_numbers = []
    matrix = {
    }

    symbol_positions = {
    }

    for line_number, line in enumerate(file):
        for char_index, char in enumerate(line):
            matrix[f'[{line_number}][{char_index}]'] = char
            if char in symbols:
                symbol_positions[f'[{line_number}][{char_index}]'] = char
    num_found = ""
    
    for x in range(len(line)):
        num_found = ""
        for y in range(len(file.readlines())):
            if matrix[f'[{x}][{y}]'].isdigit():
                if num_found == "":
                    index_start = [x, y]
                num_found += matrix[f'[{x}][{y}]']
            else:
                if num_found != "":
                    index_end = [x-1, y-1]

                    for index in [index_start, index_end]:
                        adjascent_indexes = [
                            f'[{index[0]-1}][{index[1]-1}]',
                            f'[{index[0]-1}][{index[1]}]',
                            f'[{index[0]-1}][{index[1]+1}]',
                            f'[{index[0]}][{index[1]-1}]',
                            f'[{index[0]}][{index[1]+1}]',
                            f'[{index[0]+1}][{index[1]-1}]',
                            f'[{index[0]+1}][{index[1]}]',
                            f'[{index[0]+1}][{index[1]+1}]'
                        ]

                    for index in adjascent_indexes:
                        if index in symbol_positions.keys():
                            parts_numbers.append(num_found)
                            break

                    num_found = ""
    
    print(symbol_positions)
    print(matrix)
    #print(matrix.values())
    print(parts_numbers)
 
