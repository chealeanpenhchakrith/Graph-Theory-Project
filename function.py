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

def displayUpdatedDataFile(updatedList):
    listLength = len(updatedList)
    for i in range (listLength):
        print(updatedList[i])

#Define a functin that computes the number of edges