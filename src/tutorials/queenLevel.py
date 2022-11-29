queen = 11
empty = 0
enemy = 1

# old format: origin, destination, substate that move leads to
# new format: [(move 1), (move 2)]
#             [substate from 1, substate from 2]


# For substate 0
state0 = [[empty, enemy],
          [queen, empty]]
moves0 = [
    [[(1,0),(0,0)], [(1,0),(1,1)]], [(1,0), (0,1)],
    [1, 2, 3]
]

# For substate 1
state1 = [[queen, enemy],
          [empty, empty]]
moves1 = [ 
    [[(0,0),(0,1)], [(0,0), (1,0)]], [(0,0), (1,1)],
    [3, 0, 2]
]

# For substate 2
state2 = [[empty, enemy],
           [empty, queen]]
moves2 = [ 
    [[(1,1),(0,1)], [(1,1), (1,0)]], [(1,1), (0,0)],
    [3, 0, 1]
]

# For substate 3, the winning state
state3 = [[empty, queen],
          [empty, empty]]
moves3 = [[]]
           

# SUBSTATES
substate0 = [state0, moves0]
substate1 = [state1, moves1]
substate2 = [state2, moves2]
substate3 = [state3, moves3]


allStates = [substate0, substate1, substate2, substate3]