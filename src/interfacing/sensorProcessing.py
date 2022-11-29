UPPER_LIM = 0.7
LOWER_LIM = 0.4

def getSensorMap(i1, i2, i3, i4):
    boardState = [
        [i1, i2, 0, 0],
        [i3, i4, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
        #hardcoded for now, fix later
    ]

    '''

    boardState = [
        [processInput(i1), processInput(i2), 0, 0],
        [processInput(i3), processInput(i4), 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    '''
    for i in range(2):
        for j in range(2):
            boardState[i][j] = processInput(boardState[i][j])
    
    return boardState


def processInput(input):
    if (input == 0):
        return 0 #temporary, get rid of me later
    if abs(input - 0.5) > 0.1:
        return 1
    return 0

# test1 = getBoardState(0.3, 0.8, 0.5, 0.5)
# print(test1[0])
# print(test1[1])

# print()

# test2 = getBoardState(0.3, 0.5, 0.5, 0.8)
# print(test2[0])
# print(test2[1])

'''
1 | 2
-----
3 | 4
'''