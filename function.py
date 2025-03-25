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
# def fillsPredecessor(dataStored):
#     for line in dataStored:
#         column = line.split()
#         if (len(column) == 2):
#             column.append(0)
#     return column

#Define a functin that computes the number of edges