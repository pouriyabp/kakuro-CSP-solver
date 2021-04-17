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

    # find neighbors of each nodes and set row and col consistency to each value node.
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

    # set domain to each node that are have consistency less than 9
    def set_domain_to_each_node(self):
        for i in range(0, self.row):
            for j in range(0, self.col):
                tempArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                tempNode = self.board[i][j]
                if tempNode.name[0] == 'X':
                    if tempNode.rowC > 9 and tempNode.colC > 9:
                        tempNode.set_domain(tempArr)

                    elif tempNode.rowC < 9:
                        tempArr = [x for x in tempArr if x <= tempNode.rowC - 1]  # TODO chek the neighbors>=1
                        tempNode.set_domain(tempArr)

                    elif tempNode.colC < 9:
                        tempArr = [x for x in tempArr if x <= tempNode.colC - 1]  # TODO chek the neighbors>=1
                        tempNode.set_domain(tempArr)

                    # print(tempNode.domain)
