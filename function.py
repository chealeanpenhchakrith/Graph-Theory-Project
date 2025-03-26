#Define a function to read and store the constraint table in memory
def storeDataInMemory(constraintTableFile):
    data = constraintTableFile.readlines()
    return data

#Define a function that computes the number of vertices
def verticeCounter(dataStored):
    line_count = 0
    for line in dataStored:
        line_count += 1
    verticeCounter = line_count
    return verticeCounter

#Define a function that fills with 0 rows that doesn't contain predecessor
def fillsPredecessor(dataStored):
    rowList = []
    for line in dataStored:
        column = line.split()
        if (len(column) == 2):
            column.append('0')
            rowList.append(column)
        else:
            rowList.append(column)
    return rowList

#Define a function that displays the updated data file
def displayUpdatedDataFile(updatedList):
    listLength = len(updatedList)
    for i in range (listLength):
        print(updatedList[i])

#Define a function that computes the number of edges
def edgeCounter(dataStored):
    dataStoredLength = len(dataStored)
    edgeCounter = 0
    for i in range (dataStoredLength):
        column = len(dataStored[i])
        j = 2
        while (j != column):
            edgeCounter += 1
            j += 1
    return edgeCounter

#Define a function that displays the graph as a form of triplets
def graphInFormOfTriplets(updatedList):
    iteration1 = len(updatedList)
    for i in range (iteration1):
        iteration2 = len(updatedList[i])
        for j in range (iteration2):
            if (j == 2 and j < iteration2 and updatedList[i][j] == '0'):
                print(f"{updatedList[i][j]} -> {updatedList[i][0]} = 0")
            else:
                if (j >= 2 and j < iteration2 and updatedList[i][j] != '0'):
                    print(f"{updatedList[i][j]} -> {updatedList[i][0]} = {updatedList[i][1]}")

#Define a function that represents the graph in a value matrix form
def createEmptyAdjacencyMatrix(updatedList):
    emptyAdjacencyMatrix = []
    temporaryRow = []
    verticeCounter = len(updatedList) + 1
    for row in range (verticeCounter):
        for column in range (verticeCounter):
            temporaryRow.append(0)
        emptyAdjacencyMatrix.append(temporaryRow)
        temporaryRow = []
    return emptyAdjacencyMatrix

#Define a function that displays the adjacency matrix in a value form 
def displayAdjacencyMatrix(matrix):
    matrixLength = len(matrix)
    for i in range (matrixLength):
        print(matrix[i])

def verticeIndex(updatedList):
    verticeCounter = len(updatedList)
    verticeList = []
    for i in range (verticeCounter + 1):
        verticeList.append(i)
    return verticeList