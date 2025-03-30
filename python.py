# import the function.py file
import function as fct

# Set a boolean which is True
condition = True
while (condition):

    # Ask for user input
    userInput = input("Do you want to test a constraint table ? Answer by y or n : ")
    print("\n")

    # User answer yes
    if (userInput == 'y'):

        # Try-catch clause to intercept any errors
        try:

            # Storing user input
            tableInput = input("Which table do you want to work with ? Please enter a number between 1 and 14 : ")

            print("\n")

            try:

                # Open and close the file after the block is executed
                with open(f"./Test constraint tables/table {tableInput}.txt") as f:

                    # Reading the file and store it in memory
                    data = fct.storeDataInMemory(f)
                    print("The data have been succesfully stored in memory !\n")
                    print(f"#############################  Table : {tableInput}  ################################")

                    # Updating the data file by filling rows without predecessor
                    updatedData = fct.fillsPredecessor(data)
                    print("\n")

                    # Displaying the updated data file
                    print("The chosen table looks like this \n")
                    fct.displayUpdatedDataFile(updatedData)
                    print("\n")

                    # Computing the number of vertices
                    print("The number of vertices is : ", fct.verticeCounter(data) + 2, "(after adding 2 fictional tasks 0 and", fct.verticeCounter(data) + 1,")")
                    print("\n")

                    # Computing the number of edges
                    print("The number of edges is : ", fct.edgeCounter(updatedData))
                    print("\n")

                    # Displaying the graph in form of a triplets
                    print("The graph in form of triplets looks like this :\n")
                    fct.graphInFormOfTriplets(updatedData)
                    print("\n")

                    # Displaying the list of vertices
                    verticeList = fct.verticeIndex(updatedData)
                    print("The list of vertices is : ", verticeList)

                    # Displaying the list of initialVertex,destinationVertex,edge
                    edgeList = fct.edgeList(updatedData, verticeList)
                    print("Here's the target output : ", edgeList)
                    print("\nThe edge list looks like this : (vertex -> vertex = duration)\n")
                    fct.displayEdgeList(edgeList)

                    # New display in form of triplets
                    print("New display in form of triplets :\n")
                    fct.graphInFormOfTripletsV2(edgeList)

                    # # Displaying the adjacency matrix in value matrix
                    print("\nHere is the value matrix, before pretty table : \n")
                    emptyMatrix = fct.createEmptyAdjacencyMatrix(updatedData)
                    updatedMatrix = fct.updatedEmptyAdjacencyMatrix(edgeList, emptyMatrix)
                    fct.displayAdjacencyMatrix(updatedMatrix, updatedData)

                    # # After pretty table
                    print("\nWith pretty table magic :\n")
                    fct.displayWithPrettyTable(updatedMatrix, updatedData)

                    # Check for cycle
                    if fct.has_cycle(updatedMatrix):
                        print("\n❌ The graph contains a cycle. It is not a valid scheduling graph.\n")
                    else:
                        print("\n✅ No cycles detected. Proceeding...\n")

                    #Check for negative edges
                    if fct.has_negative_edges(updatedMatrix):
                        print("❌ The graph contains negative edge(s). This is not allowed in scheduling.\n")
                    else:
                        print("✅ No negative edge weights found.\n")

                        # Compute ranks only if both conditions are met
                        ranks = fct.computeRanks(updatedMatrix)
                        print("\n📊 Ranks of the vertices:")
                        for i, rank in enumerate(ranks):
                            print(f"Task {i}: Rank {rank}")
                print("\n###################################################################################")
            except NameError:
                print("The input must be between 1 and 14. Please enter again !")

        # Catch the error
        except NameError:
            print("An error occured")

    # Set the boolean to false if the user don't want to continue
    elif (userInput == 'n'):
        condition = False

    # Ask the user to enter again if incorrect input
    else:
        print("The value entered is incorrect\n")
