#import the function.py file
import function as fct

#Set a boolean which is True
condition = True
while (condition):

    #Ask for user input
    userInput = input("Do you want to test a constraint table ? Answer by y or n : ")
    print("\n")

    #User answer yes
    if (userInput == 'y'):

        #Try-catch clause to intercept any errors
        try:
                
            #Storing user input
            tableInput = input("Which table do you want to work with ? Please enter a number between 1 and 14 : ")

            print("\n")

            try:
                
                #Open and close the file after the block is executed
                with open(f"./Test Constraint Tables Mar 22 2025/table {tableInput}.txt") as f:
                    
                    #Reading the file and store it in memory
                    data = fct.storeDataInMemory(f)
                    print("The data have been succesfully stored in memory !\n")
                    print(f"#############################  Table : {tableInput}  ################################")


                    #Updating the data file by filling rows without predecessor
                    updatedData = fct.fillsPredecessor(data)
                    print("\n")

                    #Displaying the updated data file
                    print("The updated file looks like this \n")
                    fct.displayUpdatedDataFile(updatedData)
                    print("\n")

                    #Computing the number of vertices
                    print("The number of vertices is : ", fct.verticeCounter(data)+2)
                    print("\n")

                    #Computing the number of edges
                    print("The number of edges is : ", fct.edgeCounter(updatedData))
                    print("\n")

                    #Displaying the graph in form of a triplets
                    print("The graph in form of triplets looks like this :\n")
                    fct.graphInFormOfTriplets(updatedData)
                    print("\n")

                    #Creating the empty adjacency matrix
                    emptyMatrix = fct.createEmptyAdjacencyMatrix(updatedData)
                    print("The empty adjacency matrix without label looks like this :  \n")
                    fct.displayEmptyAdjacencyMatrix(emptyMatrix)
                    print("\n")

                    #Displaying the adjacency matrix
                    print("The adjacency with labels looks like this :  \n")
                    fct.displayAdjacencyMatrix(fct.createEmptyAdjacencyMatrix(updatedData), updatedData)
                    print("\n")

                    #Displaying the list of vertices
                    print("The list of vertices is : ", fct.verticeIndex(updatedData), "\n")

                    #Displaying the list of initialVertex,destinationVertex,edge
                    print("The list of vertex, destination (vertex, edge, duration) is : \n", fct.edgeList(updatedData))
                    edgeList = fct.edgeList(updatedData)
                    print("\nThe edge list looks like this : (vertex -> vertex = duration)\n")
                    fct.displayEdgeList(fct.edgeList(updatedData))

                    #Updating the empty matrix with correct edges
                    print("\nChecking that the value matrix is well updated\n")
                    emptyMatrix = fct.createEmptyAdjacencyMatrix(updatedData)
                    updatedMatrix = fct.updatedEmptyAdjacencyMatrix(edgeList, emptyMatrix)
                    fct.displayEdgeList(updatedMatrix)

                    #Displaying the adjacency matrix in value matrix
                    print("\nValue matrix display : \n")
                    fct.displayAdjacencyMatrix(updatedMatrix, updatedData)

                    #Before pretty table
                    print("\nBefore pretty table :\n")
                    fct.displayEdgeList(updatedMatrix)

                    #After pretty table
                    print("\nAfter pretty table magic :\n")
                    fct.displayWithPrettyTable(updatedMatrix, updatedData)

                    print("\n###################################################################################")
                   
            except NameError:
                print("The input must be between 1 and 14. Please enter again !")

        #Catch the error
        except NameError:
            print("An error occured")
    
    #Set the boolean to false if the user don't want to continue
    elif (userInput == 'n'):
        condition = False

    #Ask the user to enter again if incorrect input
    else:
        print("The value entered is incorrect\n")