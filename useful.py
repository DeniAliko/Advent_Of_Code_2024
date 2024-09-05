# Useful helper functions for AOC 2024

def openFile(dayNumber):
    '''Returns a list of the lines of a saved text input for a given day'''
    file = open(dayNumber + ".txt")
    inputFile = []
    linesInFile = file.readlines()
    for i in linesInFile:
        inputFile.append(format(i.strip()))
    return inputFile

def createGrid(listOfStrings):
    '''Given a list of strings, turns that into a grid dictionary.
    \n    [0, 0] [1, 0] [2, 0]
    \n    [0, 1] [1, 1] [2, 1]
    \n    [0, 2] [1, 2] [2, 2]
    '''
    grid = {}
    for i in range(0, len(listOfStrings)):
        for j in range(0, len(listOfStrings[i])):
            grid[listOfStrings[i][j]] = [j, i]
    return grid

def printList(listToPrint):
    '''Prints a list, item by item'''
    for item in listToPrint:
        print(item)

