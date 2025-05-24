# please run this file to launch the game

import sys
from BoardModule import Board

print("Welcome to Connect Four game!")
while (True):
    # Main Menu
    print("Here are three options:")
    print("1. Start")
    print("2. How to play the game")
    print("3. Exit")

    # receive a input from user
    mainMenuInput = input("Please enter a number to choose your option:")

    # Judge the input
    if (mainMenuInput == "1"):
        # 1. Start

        # The board has 7 rows and 7 columns 
        board = Board();
        # In classic mode, there is a gravity on board
        # So each player can only choose which column the chess will be dropped.

        # use columnsList to store how many chesses are in every column
        columnsList = []

        # if game has a winner, this variable will be true
        hasWinner = False

        # chess symbol settings:
        p1ChessSymbol = " O "
        p2ChessSymbol = " X "

        # seven columns, all zero chess in each column
        for i in range(0, 7):
            columnsList.append(0)

        print("Player 1 first")
        print("Player 1 second")
        print("Game Start !")
        print()
        # a loop for the board game
        while (True):
            while(True):
                print("Now it is Player 1 turn.")
                # receive a input from user

                print("Your chess symbol is: " + p1ChessSymbol)

                inputP1 = input("Choose a column(1-7) to drop a chess:")
                columnInput = 0;
                try:
                    columnInput = int(inputP1) - 1
                    if not(columnInput >= 0 and columnInput <= 6):
                        print("You have inputed an invalid value, please try it again.")
                        print()
                        continue

                except Exception as e:
                    print("Error:")
                    print(e)
                    print("You have inputed an invalid value, please try it again.")
                    print()
                    continue

                # chess position of x.
                x = columnInput

                # chess position of y.
                y = 6 - columnsList[x]
                if not(y>=0 and y<= 6):
                    print("You cannot drop a chess in this column")
                    print("Please try it again.")
                    print()
                    continue

                # record the chess in the column
                columnsList[x] += 1

                # drop a chess
                board.dropOneChess(x, y, p1ChessSymbol, "P1")

                # get the list[str, bool]: the player name and whether the player is a winner
                playerNameAndIsWinner = board.checkTheWinner(x, y, p1ChessSymbol, "P1")

                # this line for testing
                # print(playerNameAndIsWinner)

                # print the board
                board.printBoard()

                # hasWinner variable receives a true or false
                hasWinner = playerNameAndIsWinner[1]

                # if true, show prints
                if hasWinner:
                    print("Congratulations!")
                    print("The winner is: " + playerNameAndIsWinner[0]);

                # Turn of player 1 ends.
                print()
                break

            # # if there is a winner, the program will end the game, and go back to main menu.
            #  so user can restart the game
            if hasWinner:
                print()
                print("Back to main menu. If you want to restart the game, please chooes option 1.")
                break


            while(True):
                print("Now it is Player 2 turn.")
                # receive a input from user

                print("Your chess symbol is: " + p2ChessSymbol)

                inputP2 = input("Choose a column(1-7) to drop a chess:")
                columnInput = 0;
                try:
                    columnInput = int(inputP2) - 1
                    if not(columnInput >= 0 and columnInput <= 6):
                        print("You have inputed an invalid value, please try it again.")
                        print()
                        continue

                except Exception as e:
                    print("Error:")
                    print(e)
                    print("You have inputed an invalid value, please try it again.")
                    print()
                    continue

                # chess position of x.
                x = columnInput

                # chess position of y.
                y = 6 - columnsList[x]
                if not (y >= 0 and y <= 6):
                    print("You cannot drop a chess in this column")
                    print("Please try it again.")
                    print()
                    continue

                # record the chess in the column
                columnsList[x] += 1

                # drop a chess
                board.dropOneChess(x, y, p2ChessSymbol, "P2")

                # get the list[str, bool]: the player name and whether the player is a winner
                playerNameAndIsWinner = board.checkTheWinner(x, y, p2ChessSymbol, "P2")

                # this line for testing
                # print(playerNameAndIsWinner)

                # print the board
                board.printBoard()

                # hasWinner variable receives a true or false
                hasWinner = playerNameAndIsWinner[1]

                # if true, show information
                if hasWinner:
                    print("Congratulations!")
                    print("The winner is:"+playerNameAndIsWinner[0]);

                # Turn of player 2 ends.
                print()
                break

            # if there is a winner, the program will end the game, and go back to main menu.
            # so user can restart the game
            if hasWinner:
                print()
                print("Back to main menu. If you want to restart the game, please chooes option 1.")
                break

    elif (mainMenuInput == "2"):
        # 2. How to play the game
        # print some rules about the game
        print('''
Rules about the game:
    1. There is a 7x7 empty board and two players drop one chess turn by turn. 
    2. The player who firstly connects the four chesses 
        horizontally, vertically, or diagonally will win the game. 
    3. The rule about setting a chess is that a chess will 
        land on the lowest empty spot in a column because of the gravity. 
        ''')
        print()

    elif (mainMenuInput == "3"):
        # 3. Exit
        print("Exiting the game...")
        print("Thank you!")
        print("See you next time!")
        sys.exit("User chooses to exit the game.")
    else:
        # input is unvalid
        print("Sorry. Your input is unvalid.")
        print("Going back to main menu...")
        print()
        continue
