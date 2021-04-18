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
                temp_arr = []
                temp_node = self.board[i][j]
                if temp_node.name[0] == 'X':
                    # from where temp_node is to right.
                    for k in range(j + 1, self.col):
                        temp_node2 = self.board[i][k]
                        if temp_node2.name[0] == 'X':
                            if temp_node2.name != temp_node.name:
                                temp_arr.append(temp_node2.name)
                        else:
                            break
                    # from where temp_node is to left.
                    for k in range(j, -1, -1):
                        temp_node2 = self.board[i][k]
                        if temp_node2.name[0] == 'X':
                            if temp_node2.name != temp_node.name:
                                temp_arr.append(temp_node2.name)
                        else:
                            if temp_node2.name[0] == 'C':
                                temp_node.set_row_constraint(temp_node2.rowC)
                                break
                    temp_node.add_vertical_neighbors(temp_arr)
                    temp_arr = []
                    # from where temp_node is to down.
                    for k in range(i + 1, self.row):
                        temp_node2 = self.board[k][j]
                        if temp_node2.name[0] == 'X':
                            if temp_node2.name != temp_node.name:
                                temp_arr.append(temp_node2.name)
                        else:
                            break
                        # from where temp_node is to down.
                    for k in range(i - 1, -1, -1):
                        temp_node2 = self.board[k][j]
                        if temp_node2.name[0] == 'X':
                            if temp_node2.name != temp_node.name:
                                temp_arr.append(temp_node2.name)
                        else:
                            if temp_node2.name[0] == 'C':
                                temp_node.set_col_constraint(temp_node2.colC)
                            break
                    temp_node.add_horizontal_neighbors(temp_arr)

    # set domain to each node that are have consistency less than 9
    def set_domain_to_each_node(
            self):  # TODO check the neighbors and then set domain depend on the count of neighbors.
        for i in range(0, self.row):
            for j in range(0, self.col):
                temp_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                temp_node = self.board[i][j]
                if temp_node.name[0] == 'X':
                    if temp_node.rowC > 9 and temp_node.colC > 9:
                        temp_node.set_domain(temp_arr)

                    elif temp_node.rowC < 9:
                        temp_arr = [x for x in temp_arr if x <= temp_node.rowC - 1]  # TODO check the neighbors>=1.
                        temp_node.set_domain(temp_arr)

                    elif temp_node.colC < 9:
                        temp_arr = [x for x in temp_arr if x <= temp_node.colC - 1]  # TODO check the neighbors>=1.
                        temp_node.set_domain(temp_arr)

                    # print(temp_node.domain)
