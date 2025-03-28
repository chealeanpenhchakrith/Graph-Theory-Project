from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

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
                    print(f"{updatedList[i][j]} -> {updatedList[i][0]} = {detectVerticeEdge(updatedList, int(updatedList[i][j]))}")

#Define a function that represents the graph in a value matrix form
def createEmptyAdjacencyMatrix(updatedList):
    emptyAdjacencyMatrix = []
    temporaryRow = []
    verticeCounter = len(updatedList) + 2
    for row in range (verticeCounter):
        for column in range (verticeCounter):
            temporaryRow.append(0)
        emptyAdjacencyMatrix.append(temporaryRow)
        temporaryRow = []
    return emptyAdjacencyMatrix

def displayEmptyAdjacencyMatrix(matrix):
    matrixLength = len(matrix)
    for i in range (matrixLength):
        print(matrix[i])

#Define a function that displays the adjacency matrix in a value form 
def displayAdjacencyMatrix(matrix, updatedList):
    matrixLength = len(matrix)
    verticeTop = verticeIndex(updatedList)
    print('    ', end = '')
    for j in range (len(verticeTop)):
        if (j >= 9 and j <= len(verticeTop)):
            print(verticeTop[j], '', end='')
        else:
            print(verticeTop[j], '', end=' ')
    print("")
    for i in range (matrixLength):
        if (i >= 0 and i <= 9):
            print(i, "", matrix[i])
        else:
            print(i, matrix[i])

#Define a function that return the list of vertex
def verticeIndex(updatedList):
    verticeCounter = len(updatedList) + 1
    verticeList = []
    for i in range (verticeCounter):
        verticeList.append(i)
        if (i == verticeCounter-1):
            verticeList.append(i+1)
    return verticeList

#Define a function that return a list of vertices, edges, duration
def edgeList(updatedList):
    edgeList = []
    iteration1 = len(updatedList)
    for i in range (iteration1):
        iteration2 = len(updatedList[i])
        for j in range (iteration2):
            if (j == 2 and j < iteration2 and updatedList[i][j] == '0'):
                tempEdgeList = []
                tempEdgeList.append(updatedList[i][j])
                tempEdgeList.append(updatedList[i][0])
                tempEdgeList.append(0)
                edgeList.append(tempEdgeList)
            else:
                if (j == 2 and j < iteration2 and updatedList[i][j] != '0'):
                    tempEdgeList = []
                    tempEdgeList.append(updatedList[i][j])
                    tempEdgeList.append(updatedList[i][0])
                    tempEdgeList.append(detectVerticeEdge(updatedList, int(updatedList[i][j])))
                    edgeList.append(tempEdgeList)

                else:
                    if ( j > 2 and j < iteration2 and updatedList[i][j] != '0'):
                        tempEdgeList = []
                        tempEdgeList.append(updatedList[i][j])
                        tempEdgeList.append(updatedList[i][0])
                        tempEdgeList.append(detectVerticeEdge(updatedList, int(updatedList[i][j])))
                        edgeList.append(tempEdgeList)
    return edgeList

#Define a function that display the edge list
def displayEdgeList(edgeList):
    edgeListLength = len(edgeList)
    for i in range (edgeListLength):
        print(edgeList[i])

#Define a function that finds the respective duration according to the vertex
def detectVerticeEdge(updatedList, lookingVertice):
    verticeEdge = updatedList[lookingVertice-1][1]
    return verticeEdge

#Define a function that displays the adjacency matrix with correct edges
def updatedEmptyAdjacencyMatrix(edgeList, matrix):
    for i in range (len(edgeList)):
        for j in range (len(edgeList[i])):
            initialVertex = int(edgeList[i][j])
            targetVertex = int(edgeList[i][1])
            duration = int(edgeList[i][2])
            matrix[initialVertex][targetVertex] = duration
            break
    return matrix

#Define a function that displays the adjacency matrix with a beautiful display
def displayWithPrettyTable(updatedMatrix, updatedData):
    matrixLength = len(updatedMatrix)
    table = PrettyTable()
    table = ColorTable(theme=Themes.LAVENDER)
    verticeList = verticeIndex(updatedData)
    verticeList.insert(0, ".")
    table.field_names = verticeList
    for i in range (matrixLength):
        updatedMatrix[i].insert(0, i)
    for j in range (matrixLength):
        table.add_row(updatedMatrix[j])
    print(table)