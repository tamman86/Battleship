import shipClass
import random

"""
Making ships. 0 is Horizontal, 1 is Vertical
"""
carrier = shipClass.Ship("Carrier", 5, random.choice([0, 1]))
battleship = shipClass.Ship("Battleship", 4, random.choice([0, 1]))
cruiser = shipClass.Ship("Cruiser", 3, random.choice([0, 1]))
submarine = shipClass.Ship("Submarine", 3, random.choice([0, 1]))
patrol = shipClass.Ship("Patrol Boat", 2, random.choice([0, 1]))

boats = [carrier, battleship, cruiser, submarine, patrol]

def horizPlacement(ship, board):
    placing = True                          #True means we are looking for a spot to place the ship
    print("Horizontal")
    while placing:                          #"placing" means trying to install the ship
        row = random.randint(0, 9)         #pick a row
        col = random.randint(0, 9)         #pick a col
        print(str(row) + ", " + str(col))
        occupied = False                    #space of current length of ship is not taken
        for i in range(0, ship.size):           #iterate through size of ship
            print(col + i)
            if col + i > 9:             #if ship spot exceeds 10x10 board
                occupied = True
                break
            elif board[row][col + i] == False:        #ship spot is not taken
                continue
            else:
                occupied = True                         #everything else will mean taken
                break
        if not occupied:                                    #space of current length turned out not taken
            for i in range(0, ship.size):
                board[row][col + i] = True                  #update the board to place ship here
                ship.place.append([row, col + i])
            placing = False                                 #ship is in place, close the loop

    return board


def vertPlacement(ship, board):
    placing = True                          # True means we are looking for a spot to place the ship
    print("Vertical")
    while placing:                          # "placing" means trying to install the ship
        row = random.randint(0, 9)         # pick a row
        col = random.randint(0, 9)         # pick a col
        print(str(row) + ", " + str(col))
        occupied = False                    # space of current length of ship is not taken
        for i in range(0, ship.size):           # iterate through size of ship
            print(row + i)
            if row + i > 9:             # if ship spot exceeds 10x10 board
                occupied = True
                break
            elif board[row + i][col] == False:        # ship spot is not taken
                continue
            else:
                occupied = True                         # everything else will mean taken
                break
        if not occupied:                                    # space of current length turned out not taken
            for i in range(0, ship.size):
                board[row + i][col] = True                  # update the board to place ship here
                ship.place.append([row + i, col])
            placing = False                                 # ship is in place, close the loop

    return board


def initialize():
    boardStart = [[False] * 10] * 10
    return boardStart


def generateDisplay():
    display = [["~"] * 10] * 10
    return display



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    again = "Y"

    while again == "Y":
        board = initialize()
        display = generateDisplay()

        count = 0
        for boat in boats:
            if boat.orientation == 0:
                board = horizPlacement(boat, board)
            else:
                board = vertPlacement(boat, board)
            print("Placed " + str(boat.name))

        difficulty = True
        while difficulty:
            print("How many tries? (1 - 25): ")
            tries = int(input())
            if 0 < int(tries) < 26:
                difficulty = False

        print("Ships have been placed! Good luck!")

        gameActive = True

        guesses = []
        liveShips = 5
        victory = False

        while gameActive:
            for row in display:
                print(*row)

            print("Enter a row: ")
            row = int(input())
            print("Enter a column: ")
            col = int(input())

            if [row, col] in guesses:
                print("This has already been guessed! Try again!")
            else:
                hit = False
                for boat in boats:
                    if [row, col] in boat.place:
                        print("You have hit the " + str(boat.name) + "!")
                        boat.health -= 1
                        hit = True
                        display[row][col] = "X"
                        if boat.health == 0:
                            boat.sunk = True
                            liveShips -= 1
                            print("You have sunk the " + str(boat.name) + "!")
                        break
                if not hit:
                    print("Thats a miss!")
                    display[row][col] = "O"
                    tries -= 1

            print("You have " + str(tries) + " guesses remaining!")

            if liveShips == 0:
                gameActive = False
                victory = True

            if tries == 0:
                gameActive = False

        if victory:
            print("You win! All ships are sunk!")
        else:
            print("You have run out of tries! Better luck next time!")

        print("Play again? (Y/N): ")
        again = input()
        again.upper()
