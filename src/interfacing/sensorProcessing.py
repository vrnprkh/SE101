UPPER_LIM = 0.55
LOWER_LIM = 0.48

def getSensorMap(i0, i1):
    # boardState = [
    #     [i0[0], i0[1], i0[2], i0[3]],
    #     [i0[4], i0[5], i0[6], i0[7]],
    #     [i1[0], i1[1], i1[2], i1[3]],
    #     [i1[4], i1[5], i1[6], i1[7]]
    #     #hardcoded for now, fix later
    # ]
    boardState = [
        [i0[3], i0[0], i1[4], i1[3]],
        [i0[2], i0[1], i1[5], i1[2]],
        [i0[4], i0[5], i1[6], i1[1]],
        [i0[7], i0[6], i1[7], i1[0]]
    #     #hardcoded for now, fix later
    ]

    '''

    boardState = [
        [processInput(i1), processInput(i2), 0, 0],
        [processInput(i3), processInput(i4), 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    '''
    for i in range(4):
        for j in range(4):
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