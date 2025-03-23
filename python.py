#Open and close the constraint table file at the end of the block
with open('./Test Constraint Tables Mar 22 2025/table 1.txt', 'r') as f : 

    #Store data content within the file in memory
    data = f.readlines()

    #Display content within the file in memory 
    print("The data content within the file is : ", data)

    # Calculate the number of lines within the file
    line_count = 0

    for line in data:
        line_count += 1
    print("Total lines :", line_count)

    #Deduce the number of vertices
    verticeCounter = line_count
    print("The number of vertices is :", verticeCounter)

    #Create a list of vertices
    verticeList = []
    verticeIndex = 0
    for i in range (verticeCounter):
        verticeIndex += 1
        verticeList.append(verticeIndex)
    print("The list of vertices are :", verticeList)

    #Create a list of task duration
    taskDurationList = []
    for line in data:
        column = line.split()
        if len(column) >= 2:
            taskDurationList.append(int(column[1]))
        else:
            taskDurationList.append(0)

    #Map vertices to their respective task duration
    verticeTaskDuration = []
    for j in range (line_count):
        verticeTaskDuration.append((verticeList[j],taskDurationList[j]))
    print("The list of vertices duration tasks is :", verticeTaskDuration)