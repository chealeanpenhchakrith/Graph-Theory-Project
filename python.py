# import the Steps (Steps.py) file
import Steps as fct

condition = True
while condition:
    userInput = input("Do you want to test a constraint table? Answer by y or n : ")
    print("\n")
    if userInput == 'y':
        try:
            tableInput = input("Which table do you want to work with? Please enter a number between 1 and 14 : ")
            print("\n")
            try:
                with open(f"./Test constraint tables/table {tableInput}.txt") as f:
                    data = fct.storeDataInMemory(f)
                    print("The data have been successfully stored in memory!\n")
                    print(f"#############################  Table : {tableInput}  ################################")
                    
                    updatedData = fct.fillsPredecessor(data)
                    print("\nThe chosen table looks like this:")
                    fct.displayUpdatedDataFile(updatedData)
                    print("\nThe number of vertices is : ", fct.verticeCounter(data) + 2, "(after adding 2 fictional tasks 0 and", fct.verticeCounter(data) + 1,")")
                    print("\nThe number of edges is : ", fct.edgeCounter(updatedData))
                    print("\nThe graph in form of triplets looks like this:")
                    fct.graphInFormOfTriplets(updatedData)
                    
                    verticeList = fct.verticeIndex(updatedData)
                    print("\nThe list of vertices is : ", verticeList)
                    
                    edgeList = fct.edgeList(updatedData, verticeList)
                    print("\nHere's the target output (edge list): ", edgeList)
                    print("\nThe edge list looks like this (vertex -> vertex = duration):")
                    fct.displayEdgeList(edgeList)
                    
                    print("\nNew display in form of triplets:")
                    fct.graphInFormOfTripletsV2(edgeList)
                    
                    print("\nHere is the value matrix, before pretty table:")
                    emptyMatrix = fct.createEmptyAdjacencyMatrix(updatedData)
                    updatedMatrix = fct.updatedEmptyAdjacencyMatrix(edgeList, emptyMatrix)
                    fct.displayAdjacencyMatrix(updatedMatrix, updatedData)
                    
                    print("\nWith pretty table magic:")
                    fct.displayWithPrettyTable(updatedMatrix, updatedData)
                    
                    if fct.has_cycle(updatedMatrix):
                        print("\n❌ The graph contains a cycle. It is not a valid scheduling graph.\n")
                    else:
                        print("\n✅ No cycles detected. Proceeding...\n")
                        if fct.has_negative_edges(updatedMatrix):
                            print("❌ The graph contains negative edge(s). This is not allowed in scheduling.\n")
                        else:
                            print("✅ No negative edge weights found.\n")
                            ranks = fct.computeRanks(updatedMatrix)
                            print("\n📊 Ranks of the vertices:")
                            for i, rank in enumerate(ranks):
                                print(f"Task {i}: Rank {rank}")
                            
                            ####### STEP 5: Compute Schedules #######
                            sorted_order = fct.compute_sorted_order(updatedMatrix)
                            schedule_data = fct.compute_schedules(updatedMatrix, sorted_order)
                            
                            print("\n📅 Earliest Start Dates:")
                            for node, es in schedule_data["earliest_start"].items():
                                print(f"Task {node}: {es}")
                            
                            print("\n📅 Latest Start Dates:")
                            for node, ls in schedule_data["latest_start"].items():
                                print(f"Task {node}: {ls}")
                            
                            print("\n📅 Floats:")
                            for node, fl in schedule_data["floats"].items():
                                print(f"Task {node}: {fl}")
                            
                            ####### STEP 6: Display Critical Path #######
                            fct.display_critical_path(schedule_data["critical_path"])
                print("\n###################################################################################")
            except NameError:
                print("The input must be between 1 and 14. Please enter again!")
        except NameError:
            print("An error occurred")
    elif userInput == 'n':
        condition = False
    else:
        print("The value entered is incorrect\n")
