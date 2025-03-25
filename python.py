import function as fct
condition = True
while (condition):
    userInput = input("Do you want to test a constraint table ? Answer by y or n : ")
    if (userInput == 'y'):
        try:
            tableInput = input("Which table do you want to work with ? Please enter a number between 1 and 14 :")
            with open(f"./Test Constraint Tables Mar 22 2025/table {tableInput}.txt") as f:
                data = fct.storeDataInMemory(f)
                print(fct.verticeCounter(data))
                #print(fct.fillsPredecessor(data))
        except NameError:
            print("There was an error")
            
    elif (userInput == 'n'):
        condition = False
    else:
        print("The value entered is incorrect")

#Open and close the constraint table file at the end of the block
#with open('./Test Constraint Tables Mar 22 2025/table 1.txt', 'r') as f : 

    
    # #Store data content within the file in memory
    # data = f.readlines()

    

    # # Calculate the number of lines within the file
    # line_count = 0

    # for line in data:
    #     line_count += 1
    # print("Total lines :", line_count)

    # #Deduce the number of vertices
    # verticeCounter = line_count
    # print("The number of vertices is :", verticeCounter)

    # #Create a list of vertices
    # verticeList = []
    # verticeIndex = 0
    # for i in range (verticeCounter):
    #     verticeIndex += 1
    #     verticeList.append(verticeIndex)
    # print("The list of vertices are :", verticeList)

    # #Create a list of task duration
    # taskDurationList = []
    # for line in data:
    #     column = line.split()
    #     if len(column) >= 2:
    #         taskDurationList.append(int(column[1]))
    #     else:
    #         taskDurationList.append(0)

    # #Map vertices to their respective task duration
    # verticeTaskDuration = []
    # for j in range (line_count):
    #     verticeTaskDuration.append((verticeList[j],taskDurationList[j]))
    # print("The list of vertices duration tasks is :", verticeTaskDuration)

    
    # #Map edges
    # edgesList = []
    # temporaryEdgeList = []
    # for line in data:
    #     column = line.split()
    #     columnNumber = len(column)
    #     if len(column) > 2:
    #         i = 2
    #         while (i < columnNumber):
    #             temporaryEdgeList.append(int(column[i]))
    #             edgesList.append((temporaryEdgeList[0]))
    #             temporaryEdgeList.clear()
    #             i += 1
    #     else:
    #         if (len(column) == 2):
    #             temporaryEdgeList.append(0)
    #             edgesList.append((temporaryEdgeList[0]))
    #             temporaryEdgeList.clear()
    # print("\n\nThe list of all the edges are :", edgesList)
    

    
    # #Define a function to read and store the constraint table in memory
    # def storeDataInMemory(constraintTableFile):
    #     data = constraintTableFile.readlines()
    #     return data

    # #Define a function to display the content of the constraint table file
    # def displayFile(file):
    #     print("The data content within the file is :", storeDataInMemory(file))
    
    # storeDataInMemory(table)

    # def verticeCounter():
    #     lineCounter = 0
    #     for line in data:
    #         lineCounter += 1
    #     verticeCounter = lineCounter
    #     print("Total lines :", verticeCounter)

    # def schedulingGraph()