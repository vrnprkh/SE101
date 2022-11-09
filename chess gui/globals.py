#this file is used to share the gameState variable between the gui file and the file that updates the gameState
def init(): 
    global gameState
    gameState = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


if __name__=="__init__":
    init()