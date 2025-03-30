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

# Define a function v2 of graphInFormOfTriplets
def graphInFormOfTripletsV2(edgeList):
    for i in range (len(edgeList)):
        for k in range (len(edgeList[i])):
            print(f"{edgeList[i][k]} -> {edgeList[i][k+1]} = {edgeList[i][k+2]}")
            break

#Define a function that represents the graph in a value matrix form
def createEmptyAdjacencyMatrix(updatedList):
    emptyAdjacencyMatrix = []
    temporaryRow = []
    verticeCounter = len(updatedList) + 2
    for row in range (verticeCounter):
        for column in range (verticeCounter):
            temporaryRow.append(".")
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
            display_val = "0" if value == 0 else str(value)
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
def edgeList(updatedList, verticeList):
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

    sourceVertices = {int(edge[0]) for edge in edgeList}
    sinkVertices = [str(vertice) for vertice in verticeList if vertice not in sourceVertices]
    print("Here is the sink vertice list", sinkVertices)
    fictionalEndVertice = sinkVertices[-1]
    sinkVertices.pop()

    for p in range (len(sinkVertices)):
        edgeListToFinalFictionalVertex = []
        edgeListToFinalFictionalVertex.append(sinkVertices[p])
        edgeListToFinalFictionalVertex.append(fictionalEndVertice)
        edgeListToFinalFictionalVertex.append(str(updatedList[int(sinkVertices[p])-1][1]))
        edgeList.append(edgeListToFinalFictionalVertex)

        
    print("The last part of the edge list is : ", edgeListToFinalFictionalVertex)

    print("The new edge list is this :", edgeList)
    # edgeList.append(updatedList[sinkVertices[]])

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
            row.append("0" if val == 0 else str(val))
        table.add_row(row)

    print(table)

################# STEP3 ##################

# Check if the graph contains a cycle using Kahn's Algorithm
def has_cycle(adj_matrix):
    n = len(adj_matrix)
    in_degree = [0] * n

    # Calculate in-degrees: Only count valid edges (cells that are int and nonzero)
    for i in range(n):
        for j in range(n):
            if isinstance(adj_matrix[i][j], int) and adj_matrix[i][j] != 0:
                in_degree[j] += 1

    # Collect all nodes with in-degree 0
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    visited_count = 0

    while queue:
        node = queue.popleft()
        visited_count += 1
        for neighbor in range(n):
            if isinstance(adj_matrix[node][neighbor], int) and adj_matrix[node][neighbor] != 0:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    # If not all nodes were visited, there is a cycle
    return visited_count != n



# Check if the graph contains any negative edge weights
def has_negative_edges(adj_matrix):
    for row in adj_matrix:
        for val in row:
            if val == ".":
                continue
            if val < 0:
                return True
    return False



################# STEP4 ##################

# Compute ranks for all vertices (topological sort based)
from collections import deque

def computeRanks(adj_matrix):
    """
    Compute the rank of each vertex in a single-source DAG where:
      - The source is vertex 0 (rank(0) = 0).
      - rank(v) = the maximal number of edges in any path from 0 to v.

    We assume 'adj_matrix[u][v]' is:
      - '.' (string) if there is no edge u->v,
      - an integer (possibly 0) if there is an edge u->v.
    """

    n = len(adj_matrix)
    # 1) Compute in-degree for topological sort
    in_degree = [0] * n
    for u in range(n):
        for v in range(n):
            val = adj_matrix[u][v]
            # If it's an integer, treat it as an edge
            if isinstance(val, int):
                in_degree[v] += 1

    # 2) Perform topological sort (Kahn's Algorithm)
    queue = deque([node for node in range(n) if in_degree[node] == 0])
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in range(n):
            val = adj_matrix[u][v]
            if isinstance(val, int):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

    # 3) Longest-path relaxation in topological order
    ranks = [0] * n  # Start all ranks at 0; rank(0)=0 by definition
    for u in topo_order:
        for v in range(n):
            val = adj_matrix[u][v]
            if isinstance(val, int):
                # Edge u->v => update rank[v] = max(rank[v], rank[u]+1)
                if ranks[u] + 1 > ranks[v]:
                    ranks[v] = ranks[u] + 1

    return ranks





# vertices = [0,1,2,3,4,5]
# edges = [
#     ['0', '1', 0],
#     ['0', '2', 0],
#     ['1', '3', '3'],
#     ['2', '3', '2'],
#     ['4', '3', '1'],
#     ['2', '4', '2']
#     ]

# source_vertices = {int(edge[0]) for edge in edges}

# non_source_vertices = [v for v in vertices if v not in source_vertices]

# print("Vertices that never appear as a source in the edge list are : ", non_source_vertices)