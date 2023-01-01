import shipClass
import random

"""
Making ships. 0 is Horizontal, 1 is Vertical
"""
carrier = shipClass.Ship(5, random.choice([0, 1]))
battleship = shipClass.Ship(4, random.choice([0, 1]))
cruiser = shipClass.Ship(3, random.choice([0, 1]))
submarine = shipClass.Ship(3, random.choice([0, 1]))
patrol = shipClass.Ship(2, random.choice([0, 1]))

def horizPlacement(ship, board):
    placing = True
    while placing:
        row = random.choice([0,9])
        if ship.orientation == 0:
            


def vertPlacement(ship, board):





def placement():
    ships = [[False]*10]*10
    return ships

def generateBoard():
    board = [["~"]*10]*10
    for row in board:
        print(*row)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generateBoard()
    placement()