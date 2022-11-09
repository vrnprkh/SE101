import globals
from chess import *

#this file will be the file that updates the gameState and calls the gui function
def change():
    globals.gameState = [[1, 2, 3, 4], [5, 6, 0, 0], [0, 0, 7, 8], [9, 10, 11, 12]]

def main():
    displayGame()


if __name__=="__main__":
    main()
