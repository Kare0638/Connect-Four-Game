class Board:
    # Constructor, default 7 * 7 board
    def __init__(self, rows: int = 7, cols: int = 7):
        # define rows and cols
        self.rows = rows
        self.cols = cols

        # chess counter for two players P1 and P2
        self.chessCounterForP1 = 0
        self.chessCounterForP2 = 0

        # build a board, "+" means empty space
        # use a 2D str list to build a board
        self.boardMatrix = []
        for i in range(0, rows):
            row = []
            for j in range(0, cols):
                row.append(" + ")
            self.boardMatrix.append(row)

    # the method returns board.
    def getBoard(self) -> list[list[str]]:
        return self.boardMatrix

    # the method prints board.
    def printBoard(self):
        for i in range(0, self.rows):
            row = self.boardMatrix[i]
            for j in range(0, self.cols):
                if j == self.cols - 1:
                    print(row[j])
                else:
                    print(row[j], end="")

    # validate the move of chess
    def validateTheMoveOfChess(self, x: int, y: int) -> bool:
        # validate if x and y are out of the board boundary
        if (x < 0 or x >= self.cols):
            return False
        if (y < 0 or y >= self.rows):
            return False

        # check the space if empty or not
        if self.boardMatrix[y][x] == " + ":
            return True
        else:
            return False

    # drop one chess on the board. Success of move returns True.
    def dropOneChess(self, x: int, y: int, chess: str, playerName: str) -> bool:
        # y is row index, x is the column index
        if self.validateTheMoveOfChess(x, y) == False:
            return False

        # count chesses dropped from two players
        self.boardMatrix[y][x] = chess
        if playerName == "P1":
            self.chessCounterForP1 += 1
        if playerName == "P2":
            self.chessCounterForP2 += 1
        return True

    # check if the board game has a winner
    # return the player name and whether the player is a winner
    def checkTheWinner(self, x: int, y: int, chess: str, playerName: str) -> list[str, bool]:
        # give the pointer x and y value
        pointerX = x
        pointerY = y
        # a container for playerName and True or False
        statusInfo = []
        statusInfo.append(playerName)
        # if the number of chesses is less than 4, there is no need to check
        if playerName == "P1" and self.chessCounterForP1 < 4:
            # False means there is no winner
            statusInfo.append(False)
            return statusInfo

        if playerName == "P2" and self.chessCounterForP2 < 4:
            # False means there is no winner
            statusInfo.append(False)
            return statusInfo

        '''decides what kinds of directions of this chess can have a Four Connect
         There are 4 directions to find a Four Connect.
         define a map for directions and increments

         For instances: 
         Assume that there are 4 start pointer(colIndex, rowIndex) for board
         to find a Connect Four line.

         1. vertical direction: Its start pointer is (x, 0).
            colIndex is always x and rowIndex will be incremented by 1 from 0

         2. horizonal direction: Its start pointer is (0, y).
            colIndex will be incremented by 1 from 0 and rowIndex is always y

         3. first diagonal direction: 
            (1) If x >= y, its start pointer is (x-y, 0).
            colIndex and rowIndex will be incremented by 1 from (x-y,0)
            (2) If x < y, its start pointer is (0, y-x).
            colIndex and rowIndex will be incremented by 1 from (0,y-x)

         4. second diagonal direction: 
         (1) If x + y <= 6, its start pointer is (0,x+y).
         colIndex will be incremented by 1 from 0 to (x+y), rowIndex will be incremented by -1 from (x+y) to 0
         (2) If x + y > 6, its start pointer is (x+y-rowLength+1, rowLength-1).
         colIndex will be incremented by 1 from (x+y-rowLength+1) to (rowLength-1) 
         and rowIndex will be incremented by -1 from (rowLength-1) to (x+y-rowLength+1)'''

        directions = ["vertical", "horizonal", "firstDiagonal", "secondDiagonal"]

        # put two different start pointers for the vertical and horizonal direction
        directionsStartPointerMap = {
            "vertical": [pointerX, 0],
            "horizonal": [0, pointerY]
        }

        # based on conditions, put a start pointer for the first diagonal direction
        if x >= y:
            directionsStartPointerMap["firstDiagonal"] = [x - y, 0]
        else:
            directionsStartPointerMap["firstDiagonal"] = [0, y - x]

        # based on conditions, put a start pointer for the second diagonal direction
        if x + y <= 6:
            directionsStartPointerMap["secondDiagonal"] = [0, x + y]
        else:
            directionsStartPointerMap["secondDiagonal"] = [x + y - self.rows + 1, self.rows - 1]

        '''
        Assume that there is four star pointer(colIndex, rowIndex)
        set a map for directions and increment lists
         1. vertical direction: .
            colIndex is always x and rowIndex will be incremented by 1 from 0

         2. horizonal direction:
            colIndex will be incremented by 1 from 0 and rowIndex is always y

         3. first diagonal direction: 
            colIndex and rowIndex will be incremented by 1

         4. second diagonal direction: 
            colIndex will be incremented by 1 and rowIndex will be incremented by -1   
        '''

        directionsIncrementsMap = {
            "vertical": [0, 1],
            "horizonal": [1, 0],
            "firstDiagonal": [1, 1],
            "secondDiagonal": [1, -1]
        }

        # find a Four Connect in 4 directions
        for direction in directions:
            # get start pointer
            startPointer = directionsStartPointerMap[direction]
            # get increments
            increments = directionsIncrementsMap[direction]
            # call findFourConnect function to get True or False
            resultFound = self.findFourConnect(chess, startPointer[0], startPointer[1], increments[0], increments[1])
            # this line is for testing : print(resultFound)

            # if there is Four Connect in a direction, return list [playerName, True]
            if resultFound == True:
                statusInfo.append(True)
                return statusInfo

        # if there is no Four Connect in 4 directions, return list [playerName, False]
        statusInfo.append(False)
        return statusInfo

    # this function checks the direction of the chess about if there is a Four Connect
    def findFourConnect(self, chess: str, pointerX: int, pointerY: int, incrementX: int, incrementY: int) -> bool:
        # get pointerX data
        i = pointerX
        # get pointerY data
        j = pointerY
        # create a list to contain the string values of points
        pointsList = []
        while (i >= 0 and i < self.rows and j >= 0 and j < self.rows):
            pointsList.append(self.boardMatrix[j][i])

            # make sure the length of list always is not more than 4
            if len(pointsList) > 4:
                # if the length is more than 4, pop the first point in the list
                pointsList.pop(0)

            # this line is for testing :
            # print("i:"+str(i)+" j:"+str(j)+" list:")
            # this line is for testing :
            # print(pointsList)


            # call a function to check the list is a FourConnect line or not
            if self.checkListFourConnect(chess, pointsList) == True:
                # If there is a FourConnect line in this direction, return True
                return True

            # i and j is incremented by incrementX and incrementY
            i += incrementX
            j += incrementY

        # If there is no FourConnect line in this direction, return False
        return False

    # check
    def checkListFourConnect(self, chess: str, pointsList: list) -> bool:
        # if the length of list is not 4, just return False
        if len(pointsList) != 4:
            return False

        # check if every element in the list is the same with the string value of chess
        for i in range(0, 4):
            # if not, return False
            if pointsList[i] != chess:
                return False

        # if every element is the same with the string value of chess, return True
        return True


# code for testing
if __name__ == "__main__":
    # two kinds of chesses : " @ " and " O "

    # create an instance of Board class
    board = Board()
    # code for testing
    '''
    board.dropOneChess(0, 0, " @ ", "P1")
    board.dropOneChess(1, 0, " @ ", "P1")
    board.dropOneChess(2, 0, " @ ", "P1")
    board.dropOneChess(3, 0, " @ ", "P1")
    print(board.checkTheWinner(3, 0, " @ ", "P1"))
    board.printBoard()
    '''

    '''
    board.dropOneChess(1, 1, " O ", "P2")
    board.dropOneChess(2, 2, " O ", "P2")
    board.dropOneChess(3, 3, " O ", "P2")
    board.dropOneChess(4, 4, " O ", "P2")
    print(board.checkTheWinner(4, 4, " O ", "P2"))
    board.printBoard()
    '''

    '''
    board.dropOneChess(6, 1, " O ", "P1")
    board.dropOneChess(6, 2, " O ", "P1")
    board.dropOneChess(6, 3, " O ", "P1")
    board.dropOneChess(6, 4, " O ", "P1")
    print(board.checkTheWinner(6, 4, " O ", "P1"))
    board.printBoard()
    '''

    # code for testing
    '''board.dropOneChess(0, 6, " @ ", "P2")
    board.dropOneChess(1, 5, " @ ", "P2")
    board.dropOneChess(2, 4, " @ ", "P2")
    print(board.checkTheWinner(2, 4, " @ ", "P2"))
    board.dropOneChess(3, 3, " @ ", "P2")
    print(board.checkTheWinner(3, 3, " @ ", "P2"))
    board.printBoard()'''

    # code for testing
    board.dropOneChess(0, 6, " @ ", "P2")
    print(board.checkTheWinner(0, 6, " @ ", "P2"))
    board.printBoard()

    board.dropOneChess(1, 5, " @ ", "P2")
    print(board.checkTheWinner(1, 5, " @ ", "P2"))
    board.printBoard()

    board.dropOneChess(4, 6, " @ ", "P2")
    print(board.checkTheWinner(4, 6, " @ ", "P2"))
    board.printBoard()

    board.dropOneChess(3, 5, " @ ", "P2")
    print(board.checkTheWinner(3, 5, " @ ", "P2"))
    board.printBoard()

    board.dropOneChess(2, 4, " @ ", "P2")
    print(board.checkTheWinner(2, 4, " @ ", "P2"))
    board.printBoard()

    board.dropOneChess(3, 3, " @ ", "P2")
    print(board.checkTheWinner(3, 3, " @ ", "P2"))
    board.printBoard()
