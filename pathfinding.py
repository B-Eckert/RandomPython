arr=[[0,0,0,1,0,3], # 2 is where the 'mover' is, 3 is where the 'target' is
     [0,2,1,1,0,1],
     [0,0,0,1,1,1],
     [0,0,0,1,1,1],
     [0,1,1,1,0,0]]

def matrixCopy(mat):
    copy = []
    for x in range(mat.__len__()):
        copy.append([])
        for y in range(mat[x].__len__()):
            copy[x].append(mat[x][y])
    return copy

def matrixPrint(mat):
    for x in range(mat.__len__()):
        for y in range(mat[x].__len__()):
            print(mat[x][y], end=" ")
        print(" ")


# Steps to Pathfind
# 1) Assign the distances and return the distance matrix
def distMatrix(mat):
    # Step a) Find 2
    startCoords = None
    targCoords = None
    for x in range(mat.__len__()):
        for y in range(mat[x].__len__()):
            if(mat[x][y] == 2):
                startCoords = (x, y)
            if(mat[x][y] == 3):
                targCoords = (x, y)
    if startCoords == None or targCoords == None:
        return None
    # Step b) Make the distance matrix
    distMatrix = matrixCopy(mat)
    # Count the distance from 2 to 1. 2 becomes the first 1
    distMatrix[startCoords[0], startCoords[1]] = 1
    cursor = startCoords
    # maybe recursively?
    # Spread out from the
    path = [targCoords] # Array of coordinates on the path


