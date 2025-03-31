# import the Steps (Steps.py) file
import Steps as fct

condition = True
while condition:
    # Ask the user if they want to test a constraint table
    userInput = input("Do you want to test a constraint table? Answer by y or n : ")
    print("\n")
    if userInput == 'y':
        try:
            # Prompt the user for the table number
            tableInput = input("Which table do you want to work with? Please enter a number between 1 and 14 : ")
            print("\n")
            try:
                # Open the specified table file
                with open(f"./Test constraint tables/table {tableInput}.txt") as f:
                    data = fct.storeDataInMemory(f)
                    print("The data have been successfully stored in memory!\n")
                    print(f"#############################  Table : {tableInput}  ################################")
                    
                    # Process the data to fill in missing predecessor values
                    updatedData = fct.fillsPredecessor(data)
                    #print("\nThe chosen table looks like this:")
                    #fct.displayUpdatedDataFile(updatedData)

                    # Display the number of vertices (including fictional start and finish)
                    print("\nThe number of vertices is : ", fct.verticeCounter(data) + 2, 
                          "(after adding 2 fictional tasks 0 and", fct.verticeCounter(data) + 1,")")
                    
                    

                    # Display the graph in triplet format.
                    #print("\nThe graph in form of triplets looks like this:")
                    #fct.graphInFormOfTriplets(updatedData)
                    
                    # Generate and display the list of vertices.
                    verticeList = fct.verticeIndex(updatedData)
                    #print("\nThe list of vertices is : ", verticeList)
                    
                     # Generate and display the edge list
                    edgeList = fct.edgeList(updatedData, verticeList)
                    #print("\nHere's the target output (edge list): ", edgeList)
                    #print("\nThe edge list looks like this (vertex -> vertex = duration):")
                    #fct.displayEdgeList(edgeList)

                    # Display the number of edges
                    print("\nThe number of edges is : ", len(edgeList))
                    
                     # Display the triplets again using an alternative view.
                    print("\nNew display in form of triplets:\n")
                    fct.graphInFormOfTripletsV2(edgeList)
                    
                    # Create and display the value matrix before formatting.
                    #print("\nHere is the value matrix, before pretty table:")
                    emptyMatrix = fct.createEmptyAdjacencyMatrix(updatedData)
                    updatedMatrix = fct.updatedEmptyAdjacencyMatrix(edgeList, emptyMatrix)
                    #fct.displayAdjacencyMatrix(updatedMatrix, updatedData)
                    
                     # Display the value matrix using PrettyTable.
                    print("\nWith pretty table magic:")
                    fct.displayWithPrettyTable(updatedMatrix, updatedData)
                    
                    # Check for cycles
                    if fct.has_cycle(updatedMatrix):
                        print("\n❌ The graph contains a cycle. It is not a valid scheduling graph.\n")
                    else:
                        print("\n✅ No cycles detected. Proceeding...\n")

                        # Check for negative edge weights
                        if fct.has_negative_edges(updatedMatrix):
                            print("❌ The graph contains negative edge(s). This is not allowed in scheduling.\n")
                        else:
                            print("✅ No negative edge weights found.\n")


                            # Compute ranks only if both conditions are met
                            ranks = fct.computeRanks(updatedMatrix)
                            print("\n📊 Ranks of the vertices:\n")
                            for i, rank in enumerate(ranks):
                                print(f"Task {i}: Rank {rank}")
                           
                    if fct.has_cycle(updatedMatrix):
                        print("\n❌ The graph contains a cycle. Unable to calculate scheduling information.\n")
                    elif fct.has_negative_edges(updatedMatrix):
                        print("\n❌ The graph contains negative edge weights. Unable to calculate scheduling information.\n")
                    else:
                        print("\n✅ The graph is a valid scheduling graph. Proceeding with scheduling calculation...\n")
                        updatedMatrix = fct.convert_adj_matrix(updatedMatrix)
                        earliest_dates, latest_dates, floats, critical_path = fct.scheduling_analysis(
                            updatedMatrix, ranks, updatedData)
                        print("\nScheduling analysis completed!")

                print("\n###################################################################################")
            except NameError:
                print("The input must be between 1 and 14. Please enter again!")
        except NameError:
            print("An error occurred")
    elif userInput == 'n':
        condition = False
    else:
        print("The value entered is incorrect\n")