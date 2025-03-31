from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes
from collections import deque
import copy
# ------------------------------
# STEP 1 AND STEP 2: Basic Functions
# ------------------------------

# Define a function that stores data in memory by reading all lines from the file
def storeDataInMemory(constraintTableFile):
    data = constraintTableFile.readlines()
    return data

# Define a function that counts the number of vertices (lines) in the data
def verticeCounter(dataStored):
    line_count = 0
    for line in dataStored:
        line_count += 1
    return line_count

# Define a function that fills in missing predecessor data
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

# Define a function that displays the updated data file by printing each row
def displayUpdatedDataFile(updatedList):
    for row in updatedList:
        print(row)

# Define a function that computes the number of edges from the data
def edgeCounter(dataStored):
    edgeCounter = 0
    for i in range(len(dataStored)):
        column = len(dataStored[i])
        j = 2
        while j != column:
            edgeCounter += 1
            j += 1
    return edgeCounter

# Define a function that displays the graph as triplets 
def graphInFormOfTriplets(updatedList):
    for i in range(len(updatedList)):
        for j in range(len(updatedList[i])):
            if j == 2 and updatedList[i][j] == '0':
                print(f"{updatedList[i][j]} -> {updatedList[i][0]} = 0")
            elif j >= 2 and updatedList[i][j] != '0':
                print(f"{updatedList[i][j]} -> {updatedList[i][0]} = {detectVerticeEdge(updatedList, int(updatedList[i][j]))}")

# Define a function that displays the graph as triplets 
def graphInFormOfTripletsV2(edgeList):
    for edge in edgeList:
        print(f"{edge[0]} -> {edge[1]} = {edge[2]}")

# Define a function that creates an empty adjacency matrix
def createEmptyAdjacencyMatrix(updatedList):
    emptyAdjacencyMatrix = []
    num = len(updatedList) + 2  # Add two fictional tasks: start (0) and finish (n-1)
    for _ in range(num):
        emptyAdjacencyMatrix.append(["."] * num)
    return emptyAdjacencyMatrix

# Define a function that displays an empty adjacency matrix row by row
def displayEmptyAdjacencyMatrix(matrix):
    for row in matrix:
        print(row)

# Define a function that displays the adjacency matrix with a header row
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

# Define a function that returns a list of vertex indices
def verticeIndex(updatedList):
    num = len(updatedList) + 1
    verticeList = list(range(num))
    verticeList.append(num)  # add the finish vertex
    return verticeList

# Define a function that builds and returns an edge list from the updated data
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
    #print("Here is the sink vertice list", sinkVertices)
    fictionalEndVertice = sinkVertices[-1]
    sinkVertices.pop()
    for s in sinkVertices:
        temp = [s, fictionalEndVertice, str(updatedList[int(s)-1][1])]
        edgeList.append(temp)
    #print("The last part of the edge list is :", temp)
    #print("The new edge list is this :", edgeList)
    return edgeList

# Define a function that displays the edge list by printing each edge
def displayEdgeList(edgeList):
    for edge in edgeList:
        print(edge)

# Define a function that returns the duration for a given vertex
def detectVerticeEdge(updatedList, lookingVertice):
    return updatedList[lookingVertice-1][1]

# Define a function that updates the empty adjacency matrix with edge durations
def updatedEmptyAdjacencyMatrix(edgeList, matrix):
    for edge in edgeList:
        initialVertex = int(edge[0])
        targetVertex = int(edge[1])
        duration = int(edge[2])
        matrix[initialVertex][targetVertex] = duration
    return matrix

#Define a function that displays the adjacency matrix using PrettyTable for a nicer format
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

# Define a function that checks for cycles in the graph using Kahn's Algorithm
def has_cycle(adj_matrix, updatedData):
    print("\n* Detecting a cycle \n")
    print("* Method of eliminating entry points : \n")
    n = len(adj_matrix)
    in_degree = [0] * n
    for i in range(n):
        for j in range(n):
            if isinstance(adj_matrix[i][j], int) and adj_matrix[i][j] != ".":
                in_degree[j] += 1
    sourceVerticesList = deque([i for i in range(n) if in_degree[i] == 0])
    print("The current source vertice is :", list(sourceVerticesList))
    visited_count = 0
    verticeList = list(deque(verticeIndex(updatedData)))
    print("The vertice list before elimination looks like :", verticeList)
    while sourceVerticesList:
        node = sourceVerticesList.popleft()
        print(f"\nSelected entry points = [{node}]")
        print(f"Eliminating entry points [{node}]...")
        verticeList.remove(node)
        if not (verticeList):
            print("Remaining vertices : None")
        else:
            print(f"The current list of remaining vertices is : {verticeList}.") 
        visited_count += 1
        for neighbor in range(n):
            if isinstance(adj_matrix[node][neighbor], int) and adj_matrix[node][neighbor] != ".":
                in_degree[neighbor] -= 1
                
                if in_degree[neighbor] == 0:
                    sourceVerticesList.append(neighbor)
                    
        if not list(sourceVerticesList):
            print("Method of eliminating vertices finished")
        else:
            print(f"Remaining sources vertices : {list(sourceVerticesList)}")
    return visited_count != n

# Define a function that checks if there are any negative edge weights in the graph
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

# Define a function that computes the rank of each vertex
def computeRanks(adj_matrix):
    n = len(adj_matrix)
    in_degree = [0] * n
    for u in range(n):
        for v in range(n):
            if isinstance(adj_matrix[u][v], int):
                in_degree[v] += 1
    sourceVerticesList = deque([node for node in range(n) if in_degree[node] == 0])
    topo_order = []
    while sourceVerticesList:
        u = sourceVerticesList.popleft()
        topo_order.append(u)
        for v in range(n):
            if isinstance(adj_matrix[u][v], int):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    sourceVerticesList.append(v)
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

################# STEP5/6 ##################

def calculate_earliest_dates(adj_matrix, ranks, num_vertices):

    earliest_dates = [[0, []] for _ in range(num_vertices)]
    
    valid_vertices = [(i, r) for i, r in enumerate(ranks) if i > 0 and i < num_vertices - 1]
    sorted_vertices = sorted(valid_vertices, key=lambda x: x[1])
    
    for vertex, _ in sorted_vertices:
        predecessors = []
        for pred in range(num_vertices):
            if adj_matrix[pred][vertex] not in (0, '.'):  
                try:
                    duration = int(adj_matrix[pred][vertex])
                except ValueError:
                    print(f"⚠️ Error: Unable to convert {adj_matrix[pred][vertex]} to int. Setting duration to 0.")
                    duration = 0
                
                pred_finish_time = earliest_dates[pred][0] + duration  
                predecessors.append((pred, pred_finish_time))
        
        if predecessors:
            max_time = max(predecessors, key=lambda x: x[1])[1]
            earliest_dates[vertex][0] = max_time
            earliest_dates[vertex][1] = [pred for pred, finish_time in predecessors if finish_time == max_time]
        else:
            earliest_dates[vertex][0] = 0
            earliest_dates[vertex][1] = []

    last_task = num_vertices - 1
    predecessors = []
    for pred in range(num_vertices - 1): 
        if adj_matrix[pred][last_task] not in (0, '.'): 
            try:
                duration = int(adj_matrix[pred][last_task])
            except ValueError:
                print(f"⚠️ Error: Unable to convert {adj_matrix[pred][last_task]} to int. Setting duration to 0.")
                duration = 0

            pred_finish_time = earliest_dates[pred][0] + duration
            predecessors.append((pred, pred_finish_time))

    if predecessors:
        max_time = max(predecessors, key=lambda x: x[1])[1]
        earliest_dates[last_task][0] = max_time
        earliest_dates[last_task][1] = [pred for pred, finish_time in predecessors if finish_time == max_time]
    else:
        earliest_dates[last_task][0] = 0
        earliest_dates[last_task][1] = []
    
    return earliest_dates


def convert_adj_matrix(adj_matrix):
    converted_matrix = []
    for row in adj_matrix:
        converted_row = []
        for value in row:
            if value == '.' or value == '0':
                converted_row.append(0)
            else:
                try:
                    converted_row.append(int(value))
                except ValueError:
                    try:
                        converted_row.append(float(value))
                    except ValueError:
                        converted_row.append(0)
        converted_matrix.append(converted_row)
    return converted_matrix


def calculate_latest_dates(adj_matrix, earliest_dates, ranks, num_vertices):

    try:
        ranks = [int(rank) for rank in ranks]
    except ValueError:
        print("⚠️ ranks 包含無法轉換為 int 的元素。")
    
    try:
        project_end_time = int(earliest_dates[num_vertices - 1][0])
    except ValueError:
        try:
            project_end_time = float(earliest_dates[num_vertices - 1][0])
        except ValueError:
            print(f"⚠️ Error: Unable to convert project_end_time to a valid number. Using 0 as fallback.")
            project_end_time = 0

    latest_dates = [0 if i == 0 else project_end_time for i in range(num_vertices)]
    last_task = num_vertices - 1  
    leaf_nodes = []
    
    for task in range(1, num_vertices - 1): 
        has_successor = False
        
        for succ in range(num_vertices):
            if adj_matrix[task][succ] not in (0, '.'):  
                has_successor = True
                break
        
        if not has_successor:  
            leaf_nodes.append(task)
    
    for leaf in leaf_nodes:
        latest_dates[leaf] = earliest_dates[leaf][0]

    valid_vertices = [(i, ranks[i]) for i in range(1, num_vertices - 1)]
    sorted_vertices = sorted(valid_vertices, key=lambda x: x[1], reverse=True)
    
    for vertex, _ in sorted_vertices:
        successors = []
        
        if ranks[vertex] == max(ranks): 
            latest_dates[vertex] = earliest_dates[vertex][0] 
            successors.append((num_vertices - 1, latest_dates[vertex])) 
        else:
            for succ in range(num_vertices):
                if adj_matrix[vertex][succ] != 0 and adj_matrix[vertex][succ] != '.':
                    try:
                        duration = int(adj_matrix[vertex][succ])
                        latest_start_constraint = latest_dates[succ] - duration
                        successors.append((succ, latest_start_constraint))
                    except ValueError:
                        print(f"Error converting {adj_matrix[vertex][succ]} to int.")
            
            if successors:
                min_succ, min_time = min(successors, key=lambda x: x[1])
                latest_dates[vertex] = min_time
            else:
                if latest_dates[vertex] == project_end_time:
                    latest_dates[vertex] = project_end_time

    return latest_dates

def calculate_floats(earliest_dates, latest_dates, num_vertices):
    floats = []
    for i in range(num_vertices):
        earliest = earliest_dates[i][0] if isinstance(earliest_dates[i], list) else earliest_dates[i]
        float_time = latest_dates[i] - earliest
        floats.append(float_time)
    return floats

def identify_critical_path(floats, num_vertices, earliest_dates, ranks, adj_matrix, updatedData):
    critical_tasks = [i for i in range(num_vertices) if floats[i] == 0]

    for row in adj_matrix:
        for index, value in enumerate(row):
            if isinstance(value, str):
                if value == '.':
                    row[index] = 0
                else:
                    try:
                        row[index] = int(value)
                    except ValueError:
                        row[index] = 0
    
    modified_earliest_dates = copy.deepcopy(earliest_dates)
    for i in range(1, num_vertices - 1):  
        if ranks[i] == 1 and not modified_earliest_dates[i][1]:
            modified_earliest_dates[i][1] = [0]  
    
    last_task = num_vertices - 1  
    max_rank = max(ranks[1:last_task])  
    max_rank_tasks = [i for i in range(1, last_task) if ranks[i] == max_rank]  

    for task in max_rank_tasks:
        if task not in modified_earliest_dates[last_task][1]:
            modified_earliest_dates[last_task][1].append(task)
    
    leaf_nodes = []
    for task in range(1, num_vertices - 1): 
        is_leaf = all(adj_matrix[task][j] in (0, '.') for j in range(num_vertices))
        if is_leaf:
            leaf_nodes.append(task)

    for leaf in leaf_nodes:
        if leaf not in modified_earliest_dates[last_task][1]:
            modified_earliest_dates[last_task][1].append(leaf)
    
    def calculate_path_sum(task):
        path_sum = 0
        current = task
        
        while current != 0:
            predecessors = modified_earliest_dates[current][1]
            if not predecessors:
                break  
            
            pred = predecessors[0]  
            duration = adj_matrix[pred][current] if adj_matrix[pred][current] != '.' else 0
            path_sum += duration
            current = pred

        return path_sum

    def get_task_duration(task_id):
        for data in updatedData:
            if int(data[0]) == task_id:
                return int(data[1])
        return 0  
    
    path_sums = {}
    for task in max_rank_tasks:
        task_path_sum = calculate_path_sum(task)
        task_duration = get_task_duration(task)  
        total_path_sum = task_path_sum + task_duration  
        path_sums[task] = total_path_sum
    
    max_path_sum = max(path_sums.values())
    valid_max_tasks = [task for task, sum_value in path_sums.items() if sum_value == max_path_sum]

    task_paths = {i: [] for i in range(num_vertices)}
    for task in critical_tasks:
        predecessors = modified_earliest_dates[task][1]
        task_paths[task] = predecessors

    all_critical_paths = []
    
    def backtrack(current_task, path):
        if current_task == 0: 
            complete_path = path[::-1] + [last_task]
            all_critical_paths.append(complete_path)
            return
        
        if current_task not in task_paths or not task_paths[current_task]:
            return
        
        for pred in task_paths[current_task]:  
            backtrack(pred, path + [pred])
    
    for task in valid_max_tasks:
        backtrack(task, [task])
    
    return all_critical_paths

def display_scheduling_results(earliest_dates, latest_dates, floats, critical_path, updatedData):
    from prettytable import PrettyTable
    
    table = PrettyTable()
    table.field_names = ["Task", "Duration", "Earliest Start", "Latest Start", "Float", "Critical Path"]
    
    num_vertices = len(floats)
    
    for i in range(num_vertices):
        duration = 0
        if i > 0 and i < len(updatedData) + 1:
            try:
                duration = int(updatedData[i-1][1])
            except:
                duration = 0
        earliest = earliest_dates[i][0] if isinstance(earliest_dates[i], list) else earliest_dates[i]
        
        is_critical = "Yes" if floats[i] == 0 else "No"
        
        table.add_row([i, duration, earliest, latest_dates[i], floats[i], is_critical])
    
    print(table)
    for path in critical_path:
        print(f"critical path(s): {' → '.join(map(str, path))}")

def scheduling_analysis(adj_matrix, ranks, updatedData):

    num_vertices = len(adj_matrix)

    earliest_dates = calculate_earliest_dates(adj_matrix, ranks, num_vertices)
    latest_dates = calculate_latest_dates(adj_matrix, earliest_dates, ranks, num_vertices)
    floats = calculate_floats(earliest_dates, latest_dates, num_vertices)
    critical_path= identify_critical_path(floats, num_vertices, earliest_dates, ranks, adj_matrix, updatedData)
    
    display_scheduling_results(earliest_dates, latest_dates, floats, critical_path, updatedData)
    
    return earliest_dates, latest_dates, floats, critical_path