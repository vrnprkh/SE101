bishop = 8
empty = 0
enemy = 1

# old format: origin, destination, substate that move leads to
# new format: [(move 1), (move 2)]
#             [substate from 1, substate from 2]


# For substate 0
state0 = [[empty, enemy],
          [bishop, empty]]
moves0 = [
    [[(1,0),(0,1)]],  
    [3]
]

# For substate 1
state1 = [[bishop, enemy],
          [empty, empty]]
moves1 = [ 
    [[(0,0),(1,1)]],
    [2]
]

# For substate 2
state2 = [[empty, enemy],
           [empty, bishop]]
moves2 = [ 
    [[(0,0)]],
    [1]
]

# For substate 3, the winning state
state3 = [[empty, bishop],
          [empty, empty]]
moves3 = [[]]
           

# SUBSTATES
substate0 = [state0, moves0]
substate1 = [state1, moves1]
substate2 = [state2, moves2]
substate3 = [state3, moves3]

allStates = [substate0, substate1, substate2, substate3]