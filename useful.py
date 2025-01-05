# Useful helper functions for AOC 2024

def openFile(dayNumber):
    '''Returns a list of the lines of a saved text input for a given day'''
    file = open(str(dayNumber) + ".txt")
    inputFile = []
    linesInFile = file.readlines()
    for i in linesInFile:
        inputFile.append(format(i.strip()))
    return inputFile

def createGrid(listOfStrings):
    '''Given a list of strings, turns that into a grid dictionary.
        \n first coordinate is position in list, second coordinate is position in sublist
    '''
    grid = {}
    for i in range(0, len(listOfStrings)):
        for j in range(0, len(listOfStrings[i])):
            grid[(i, j)] = listOfStrings[i][j]
    return grid

def printList(listToPrint):
    '''Prints a list, item by item'''
    for item in listToPrint:
        print(item)

def bronKerbosch(R, P, X, connections, max = []):
    '''Finding the maximal subcliques of a graph, connections is a dictionary of neighbors'''
    if len(P) == 0 and len(X) == 0:
        max.append(R)

    else:
        for x in P:
            pIntN = []
            xIntN = []
            for i in connections[x]:
                if i in P:
                    pIntN.append(i)
                if i in X:
                    xIntN.append(i)
            bronKerbosch(R + [x], pIntN, xIntN, connections, max)
            P.remove(x)
            X.append(x)

    return max