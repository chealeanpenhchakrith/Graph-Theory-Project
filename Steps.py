from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes
from collections import deque

# ------------------------------
# STEP 1: Basic Functions
# ------------------------------

def storeDataInMemory(constraintTableFile):
    data = constraintTableFile.readlines()
    return data

def verticeCounter(dataStored):
    line_count = 0
    for line in dataStored:
        line_count += 1
    return line_count

def fillsPredecessor(dataStored):
    rowList = []
    for line in dataStored:
        column = line.split()
        if len(column) == 2:
            column.append('0')
            rowList.append(column)
        else:
            rowList.append(column)
    return rowList

def displayUpdatedDataFile(updatedList):
    for row in updatedList:
        print(row)

def edgeCounter(dataStored):
    edgeCounter = 0
    for i in range(len(dataStored)):
        column = len(dataStored[i])
        j = 2
        while j != column:
            edgeCounter += 1
            j += 1
    return edgeCounter

def graphInFormOfTriplets(updatedList):
    for i in range(len(updatedList)):
        for j in range(len(updatedList[i])):
            if j == 2 and updatedList[i][j] == '0':
                print(f"{updatedList[i][j]} -> {updatedList[i][0]} = 0")
            elif j >= 2 and updatedList[i][j] != '0':
                print(f"{updatedList[i][j]} -> {updatedList[i][0]} = {detectVerticeEdge(updatedList, int(updatedList[i][j]))}")

def graphInFormOfTripletsV2(edgeList):
    for edge in edgeList:
        print(f"{edge[0]} -> {edge[1]} = {edge[2]}")

def createEmptyAdjacencyMatrix(updatedList):
    emptyAdjacencyMatrix = []
    num = len(updatedList) + 2  # Add two fictional tasks: start (0) and finish (n-1)
    for _ in range(num):
        emptyAdjacencyMatrix.append(["."] * num)
    return emptyAdjacencyMatrix

def displayEmptyAdjacencyMatrix(matrix):
    for row in matrix:
        print(row)

def displayAdjacencyMatrix(matrix, updatedList):
    verticeTop = verticeIndex(updatedList)
    print('    ', end='')
    for j in verticeTop:
        print(f"{j:>3}", end=' ')
    print()
    for i in range(len(matrix)):
        print(f"{i:<3}", end=' ')
        for val in matrix[i]:
            display_val = "0" if val == 0 else str(val)
            print(f"{display_val:>3}", end=' ')
        print()

def verticeIndex(updatedList):
    num = len(updatedList) + 1
    verticeList = list(range(num))
    verticeList.append(num)  # add the finish vertex
    return verticeList

def edgeList(updatedList, verticeList):
    edgeList = []
    for i in range(len(updatedList)):
        for j in range(len(updatedList[i])):
            if j == 2 and updatedList[i][j] == '0':
                temp = [updatedList[i][j], updatedList[i][0], 0]
                edgeList.append(temp)
            elif j == 2 and updatedList[i][j] != '0':
                temp = [updatedList[i][j], updatedList[i][0], detectVerticeEdge(updatedList, int(updatedList[i][j]))]
                edgeList.append(temp)
            elif j > 2 and updatedList[i][j] != '0':
                temp = [updatedList[i][j], updatedList[i][0], detectVerticeEdge(updatedList, int(updatedList[i][j]))]
                edgeList.append(temp)
    sourceVertices = {int(edge[0]) for edge in edgeList}
    sinkVertices = [str(v) for v in verticeList if v not in sourceVertices]
    print("Here is the sink vertice list", sinkVertices)
    fictionalEndVertice = sinkVertices[-1]
    sinkVertices.pop()
    for s in sinkVertices:
        temp = [s, fictionalEndVertice, str(updatedList[int(s)-1][1])]
        edgeList.append(temp)
    print("The last part of the edge list is :", temp)
    print("The new edge list is this :", edgeList)
    return edgeList

def displayEdgeList(edgeList):
    for edge in edgeList:
        print(edge)

def detectVerticeEdge(updatedList, lookingVertice):
    return updatedList[lookingVertice-1][1]

def updatedEmptyAdjacencyMatrix(edgeList, matrix):
    for edge in edgeList:
        initialVertex = int(edge[0])
        targetVertex = int(edge[1])
        duration = int(edge[2])
        matrix[initialVertex][targetVertex] = duration
    return matrix

def displayWithPrettyTable(updatedMatrix, updatedData):
    from prettytable import PrettyTable
    from prettytable.colortable import ColorTable, Themes
    table = ColorTable(theme=Themes.LAVENDER)
    verticeList = verticeIndex(updatedData)
    verticeList.insert(0, ".")
    table.field_names = verticeList
    for i in range(len(updatedMatrix)):
        row = [str(i)]
        for val in updatedMatrix[i]:
            row.append("0" if val == 0 else str(val))
        table.add_row(row)
    print(table)

# ------------------------------
# STEP 3: Cycle & Negative Edge Check
# ------------------------------

def has_cycle(adj_matrix):
    n = len(adj_matrix)
    in_degree = [0] * n
    for i in range(n):
        for j in range(n):
            if isinstance(adj_matrix[i][j], int) and adj_matrix[i][j] != 0:
                in_degree[j] += 1
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
    return visited_count != n

def has_negative_edges(adj_matrix):
    for row in adj_matrix:
        for val in row:
            if val == ".":
                continue
            if val < 0:
                return True
    return False

# ------------------------------
# STEP 4: Compute Ranks (Longest Path in DAG)
# ------------------------------

def computeRanks(adj_matrix):
    n = len(adj_matrix)
    in_degree = [0] * n
    for u in range(n):
        for v in range(n):
            if isinstance(adj_matrix[u][v], int):
                in_degree[v] += 1
    queue = deque([node for node in range(n) if in_degree[node] == 0])
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in range(n):
            if isinstance(adj_matrix[u][v], int):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
    ranks = [0] * n
    for u in topo_order:
        for v in range(n):
            if isinstance(adj_matrix[u][v], int):
                if ranks[u] + 1 > ranks[v]:
                    ranks[v] = ranks[u] + 1
    return ranks

# ------------------------------
# Additional Functions for Scheduling
# ------------------------------

def compute_sorted_order(adj_matrix):
    n = len(adj_matrix)
    in_degree = [0] * n
    for u in range(n):
        for v in range(n):
            if isinstance(adj_matrix[u][v], int) and adj_matrix[u][v] != 0:
                in_degree[v] += 1
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    sorted_order = []
    while queue:
        u = queue.popleft()
        sorted_order.append(u)
        for v in range(n):
            if isinstance(adj_matrix[u][v], int) and adj_matrix[u][v] != 0:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
    return sorted_order

def compute_schedules(adj_matrix, sorted_order):
    """
    Computes scheduling data based on the weighted graph.
    
    Forward pass (for earliest start times):
      For each vertex u in sorted order,
      earliest_start[v] = max(earliest_start[v], earliest_start[u] + duration(u,v))
    
    Backward pass (for latest start times):
      Set latest_start[finish] = earliest_start[finish] where finish = n-1.
      Then for each vertex u in reverse topological order,
      latest_start[u] = min(latest_start[u], latest_start[v] - duration(u,v)) for all edges u->v.
    
    Floats are computed as: float = latest_start - earliest_start.
    
    The function returns a dictionary with keys:
      - "earliest_start"
      - "latest_start"
      - "floats"
      - "critical_path" (nodes with zero float, in topological order)
    """
    n = len(adj_matrix)
    # Forward pass: compute earliest start times
    earliest_start = [0] * n
    for u in sorted_order:
        for v in range(n):
            if isinstance(adj_matrix[u][v], int):
                candidate = earliest_start[u] + adj_matrix[u][v]
                if candidate > earliest_start[v]:
                    earliest_start[v] = candidate

    # Backward pass: compute latest start times
    latest_start = [float('inf')] * n
    finish = n - 1  # assume finish node is the last vertex
    latest_start[finish] = earliest_start[finish]
    for u in reversed(sorted_order):
        for v in range(n):
            if isinstance(adj_matrix[u][v], int):
                candidate = latest_start[v] - adj_matrix[u][v]
                if candidate < latest_start[u]:
                    latest_start[u] = candidate
    # For any node not updated, set LS = ES
    for i in range(n):
        if latest_start[i] == float('inf'):
            latest_start[i] = earliest_start[i]
    floats = [latest_start[i] - earliest_start[i] for i in range(n)]
    # Determine critical path: nodes with zero float in topological order
    critical_path = [i for i in sorted_order if floats[i] == 0]
    
    return {
        "earliest_start": {i: earliest_start[i] for i in range(n)},
        "latest_start": {i: latest_start[i] for i in range(n)},
        "floats": {i: floats[i] for i in range(n)},
        "critical_path": critical_path
    }

def display_critical_path(critical_path):
    print("Critical Path: " + " -> ".join(map(str, critical_path)))
