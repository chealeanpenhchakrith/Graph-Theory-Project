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

                    # Display the number of vertices (including fictional start and finish)
                    print("\nThe number of vertices is : ", fct.verticeCounter(data) + 2, 
                          "(after adding 2 fictional tasks 0 and", fct.verticeCounter(data) + 1,")")
                    
                    # Generate and display the list of vertices.
                    verticeList = fct.verticeIndex(updatedData)
                    
                    # Generate and display the edge list
                    edgeList = fct.edgeList(updatedData, verticeList)

                    # Display the number of edges
                    print("\nThe number of edges is : ", len(edgeList))
                    
                    # Display the triplets again using an alternative view.
                    print("\nThe graph in form of triplets is :\n")
                    fct.graphInFormOfTripletsV2(edgeList)
                    
                    # Create and display the value matrix before formatting.
                    emptyMatrix = fct.createEmptyAdjacencyMatrix(updatedData)
                    updatedMatrix = fct.updatedEmptyAdjacencyMatrix(edgeList, emptyMatrix)
                    
                    # Display the value matrix using PrettyTable.
                    print("\nThe adjacency matrix is :\n")
                    fct.displayWithPrettyTable(updatedMatrix, updatedData)
                    
                    # Check whether the graph contains a cycle or not
                    if fct.has_cycle(updatedMatrix, updatedData):
                        print("\n❌ The graph contains a cycle. It is not a valid scheduling graph.\n")

                        # Check whether the graph contains negeative edges or not
                    elif fct.has_negative_edges(updatedMatrix):
                        print("\n❌ The graph contains negative edge weights. It is not a valid scheduling graph.\n")

                    else:
                        # If both condition are met compute the next steps (rank, earliest dates, latest dates, floats, critical path)
                        print("\nThere is no cycle and no negative edges thus : ✅ The graph is a valid scheduling graph.  Proceeding with scheduling calculation...\n")
                        # Compute ranks only if both conditions are met
                        ranks = fct.computeRanks(updatedMatrix)
                        print("\n📊 Ranks of the vertices:\n")
                        for i, rank in enumerate(ranks):
                            print(f"Task {i}: Rank {rank}")
                        print("\n")

                        # Compute and display the earliest dates, latest dates, floats, critical path
                        print("Computing : earliest date, latest date, floats, critical path\n")
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