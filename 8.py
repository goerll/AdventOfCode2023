with open("input.txt", "r") as file:
    directions = file.readline()
    file.readline()
    nodes = file.readlines()

steps = 0
nodeDict = {}

arrived = False
nodes = [node.strip() for node in nodes if node != "\n"]
for line in nodes:
    line = line.strip()
    nodeDict[line[:3]] = (line[7:10], line[12:15])

next_node = nodes[0][:3]

while arrived == False:
    for direction in directions:
        #print(direction)
        steps += 1
        if direction == "L":
            next_node = nodeDict[next_node][0]
        if direction == "R":
            next_node = nodeDict[next_node][1]
        #print(next_node)
        if next_node == "ZZZ":
            arrived = True
            break
    if next_node == "ZZZ":
        arrived = True
        break

print(steps)
