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