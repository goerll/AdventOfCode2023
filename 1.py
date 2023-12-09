with open("input.txt", "r") as file:
    numbers = []
    line_numbers = []
    current_number = ""

    for line in file:
        for i in line:
            if i.isdigit():
                line_numbers.append(i)
        
        current_number += line_numbers[0]
        current_number += line_numbers[-1]
        numbers.append(int(current_number))

        current_number = ""
        line_numbers = []

print(sum(numbers))

