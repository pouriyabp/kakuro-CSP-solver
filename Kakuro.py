import Node


class Kakuro:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = []

    def add_nodes_to_board(self, array_of_nodes):
        self.board.append(array_of_nodes)

    def print_board(self):
        text = ""
        for i in range(0, self.row):
            for j in range(0, self.col):
                # because B nodes has no number in their name
                if str(self.board[i][j]) == 'B':
                    text += str(self.board[i][j]) + " " * 3
                else:
                    text += str(self.board[i][j]) + " "
            text += '\n'
        return text

    def solve(self):
        pass

    def find_neighbors(self):
        for i in range(0, self.row):
            for j in range(0, self.col):
                tempArr = []
                tempNode = self.board[i][j]
                if tempNode.name[0] == 'X':
                    # from where tempNode is to right.
                    for k in range(j + 1, self.col):
                        tempNode2 = self.board[i][k]
                        if tempNode2.name[0] == 'X':
                            if tempNode2.name != tempNode.name:
                                tempArr.append(tempNode2.name)
                        else:
                            break
                    # from where tempNode is to left.
                    for k in range(j, -1, -1):
                        tempNode2 = self.board[i][k]
                        if tempNode2.name[0] == 'X':
                            if tempNode2.name != tempNode.name:
                                tempArr.append(tempNode2.name)
                        else:
                            if tempNode2.name[0] == 'C':
                                tempNode.set_row_constraint(tempNode2.rowC)
                                break
                    tempNode.add_vertical_neighbors(tempArr)
                    tempArr = []
                    # from where tempNode is to down.
                    for k in range(i + 1, self.row):
                        tempNode2 = self.board[k][j]
                        if tempNode2.name[0] == 'X':
                            if tempNode2.name != tempNode.name:
                                tempArr.append(tempNode2.name)
                        else:
                            break
                        # from where tempNode is to down.
                    for k in range(i - 1, -1, -1):
                        tempNode2 = self.board[k][j]
                        if tempNode2.name[0] == 'X':
                            if tempNode2.name != tempNode.name:
                                tempArr.append(tempNode2.name)
                        else:
                            if tempNode2.name[0] == 'C':
                                tempNode.set_col_constraint(tempNode2.colC)
                            break
                    tempNode.add_horizontal_neighbors(tempArr)