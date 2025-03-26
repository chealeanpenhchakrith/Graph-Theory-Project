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
            print("The value entered must be between 1 and 14. Please enter again !")

            print("\n")

            try:
                
                #Open and close the file after the block is executed
                with open(f"./Test Constraint Tables Mar 22 2025/table {tableInput}.txt") as f:
                    
                    #Reading the file and store it in memory
                    data = fct.storeDataInMemory(f)
                    print("The data have been succesfully stored in memory !\n")

                    #Updating the data file by filling rows without predecessor
                    updatedData = fct.fillsPredecessor(data)
                    print("\n")

                    #Displaying the updated data file
                    print("The updated file looks like this \n")
                    fct.displayUpdatedDataFile(updatedData)
                    print("\n")

                    #Computing the number of vertices
                    print("The number of vertices is : ", fct.verticeCounter(data))
                    print("\n")

                    #Computing the number of edges
                    print("The number of edges is : ", fct.edgeCounter(updatedData))
                    print("\n")

                    #Displaying the graph in form of a triplets
                    print("The graph in form of triplets looks like this :\n")
                    fct.graphInFormOfTriplets(updatedData)
                    print("\n")

                    #Creating the empty adjacency matrix
                    print("The empty adjacency matrix is ", fct.createEmptyAdjacencyMatrix(updatedData))

                    #Displaying the adjacency matrix
                    print("The adjacency matrix looks like : ")
                    fct.displayAdjacencyMatrix(fct.createEmptyAdjacencyMatrix(updatedData))

                    #Displaying the list of vertices
                    print("The list of vertices is : ", fct.verticeIndex(updatedData))
                
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