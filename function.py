from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes
from collections import deque

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

    # Print header
    print('    ', end='')
    for j in verticeTop:
        print(f"{j:>3}", end=' ')
    print()

    # Print each row
    for i in range(matrixLength):
        print(f"{i:<3}", end=' ')
        for j in range(len(matrix[i])):
            value = matrix[i][j]
            display_val = "-" if value == 0 else str(value)
            print(f"{display_val:>3}", end=' ')
        print()

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
    from prettytable import PrettyTable
    from prettytable.colortable import ColorTable, Themes

    matrixLength = len(updatedMatrix)
    table = ColorTable(theme=Themes.LAVENDER)

    verticeList = verticeIndex(updatedData)
    verticeList.insert(0, ".")  # Header for row labels
    table.field_names = verticeList

    for i in range(matrixLength):
        # Replace 0s with "-" for display purposes
        row = [str(i)]  # First column: row label
        for val in updatedMatrix[i]:
            row.append("-" if val == 0 else str(val))
        table.add_row(row)

    print(table)

################# STEP3 ##################

# Check if the graph contains a cycle using Kahn's Algorithm
def has_cycle(adj_matrix):
    n = len(adj_matrix)
    in_degree = [0] * n

    # Calculate in-degrees
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] != 0:
                in_degree[j] += 1

    # Collect all nodes with in-degree 0
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    visited_count = 0

    while queue:
        node = queue.popleft()
        visited_count += 1
        for neighbor in range(n):
            if adj_matrix[node][neighbor] != 0:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    # If not all nodes were visited, there is a cycle
    return visited_count != n


# Check if the graph contains any negative edge weights
def has_negative_edges(adj_matrix):
    for row in adj_matrix:
        for val in row:
            if val < 0:
                return True
    return False



################# STEP4 ##################

# Compute ranks for all vertices (topological sort based)
def computeRanks(adj_matrix):
    n = len(adj_matrix)
    in_degree = [0] * n
    ranks = [0] * n

    # 1: Count incoming edges (in-degree)
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] != 0:
                in_degree[j] += 1

    # 2: Initialize queue with nodes having in-degree 0
    queue = deque([i for i in range(n) if in_degree[i] == 0])

    # 3: Process the graph in topological order
    while queue:
        current = queue.popleft()
        for neighbor in range(n):
            if adj_matrix[current][neighbor] != 0:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                # Update the rank
                ranks[neighbor] = max(ranks[neighbor], ranks[current] + 1)
    return ranks
