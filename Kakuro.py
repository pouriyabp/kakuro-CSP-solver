import heapq


class Kakuro:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = []
        self.arrOfValueNodes = []
        self.copyOfArrOfValueNodes = []

    # full the arr of nodes to have all value nodes in one arr.
    def set_arr_of_value_nodes(self):
        for i in range(0, self.row):
            for j in range(0, self.col):

                temp_node = self.board[i][j]
                if temp_node.name[0] == 'X':
                    self.arrOfValueNodes.append(temp_node)

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
                                temp_arr.append(temp_node2)
                        else:
                            break
                    # from where temp_node is to left.
                    for k in range(j, -1, -1):
                        temp_node2 = self.board[i][k]
                        if temp_node2.name[0] == 'X':
                            if temp_node2.name != temp_node.name:
                                temp_arr.append(temp_node2)
                        else:
                            if temp_node2.name[0] == 'C':
                                temp_node.set_row_constraint(temp_node2.rowC)
                                break
                    temp_node.add_horizontal_neighbors(temp_arr)
                    temp_arr = []
                    # from where temp_node is to down.
                    for k in range(i + 1, self.row):
                        temp_node2 = self.board[k][j]
                        if temp_node2.name[0] == 'X':
                            if temp_node2.name != temp_node.name:
                                temp_arr.append(temp_node2)
                        else:
                            break
                        # from where temp_node is to up.
                    for k in range(i - 1, -1, -1):
                        temp_node2 = self.board[k][j]
                        if temp_node2.name[0] == 'X':
                            if temp_node2.name != temp_node.name:
                                temp_arr.append(temp_node2)
                        else:
                            if temp_node2.name[0] == 'C':
                                temp_node.set_col_constraint(temp_node2.colC)
                            break
                    temp_node.add_vertical_neighbors(temp_arr)

    # # set domain to each node that are have consistency less than 9
    # def set_domain_to_each_node(
    #         self):  # TODO check the neighbors and then set domain depend on the count of neighbors.
    #     for i in range(0, self.row):
    #         for j in range(0, self.col):
    #             temp_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #             temp_node = self.board[i][j]
    #             if temp_node.name[0] == 'X':
    #                 if temp_node.rowC > 9 and temp_node.colC > 9:
    #                     temp_node.set_domain(temp_arr)
    #
    #                 elif temp_node.rowC < 9:
    #                     temp_arr = [x for x in temp_arr if x <= temp_node.rowC - 1]  # TODO check the neighbors>=1.
    #                     temp_node.set_domain(temp_arr)
    #
    #                 elif temp_node.colC < 9:
    #                     temp_arr = [x for x in temp_arr if x <= temp_node.colC - 1]  # TODO check the neighbors>=1.
    #                     temp_node.set_domain(temp_arr)
    #
    #                 # print(temp_node.domain)

    # calculate the domain of nodes that has no value depend on their neighbors
    def calculate_domain(self):
        for i in range(0, self.row):
            for j in range(0, self.col):
                temp_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                temp_node = self.board[i][j]
                if temp_node.name[0] == 'X' and temp_node.value is None:
                    number_of_neighbors = 1
                    # print(temp_node.horizontalNeighbors)
                    for k in range(0, len(temp_node.horizontalNeighbors)):
                        if temp_node.horizontalNeighbors[k].value is None:
                            number_of_neighbors += 1
                    # print(temp_node.rowC)
                    max_value = int(temp_node.rowC - ((number_of_neighbors * (number_of_neighbors - 1)) / 2))
                    min_value = int(temp_node.rowC - ((20 - number_of_neighbors) * (number_of_neighbors - 1)) / 2)
                    # print(f"{temp_node} max Value {max_value} min Value {min_value}")
                    # print(number_of_neighbors)
                    temp_arr = [x for x in temp_arr if x >= min_value]
                    temp_arr = [x for x in temp_arr if x <= max_value]
                    # print(temp_arr)
                    temp_node.set_domain(temp_arr)

                    number_of_neighbors = 1
                    # print(temp_node.verticalNeighbors)
                    for k in range(0, len(temp_node.verticalNeighbors)):
                        if temp_node.verticalNeighbors[k].value is None:
                            number_of_neighbors += 1
                    max_value = int(temp_node.colC - ((number_of_neighbors * (number_of_neighbors - 1)) / 2))
                    min_value = int(temp_node.colC - ((20 - number_of_neighbors) * (number_of_neighbors - 1)) / 2)
                    temp_arr = [x for x in temp_arr if x >= min_value]
                    temp_arr = [x for x in temp_arr if x <= max_value]
                    # print(temp_arr)
                    # print(f"{temp_node} max Value {max_value} min Value {min_value}")
                    if temp_node.domain != temp_arr:
                        if len(temp_arr) < len(temp_node.domain):
                            temp_node.set_domain(temp_arr)
                    # print(temp_node.domain)

    @staticmethod
    # function that check goal: if all variables have value.
    def check_goal(row, col, board):
        i = 0
        check_node = False
        while i < row:
            j = 0
            while j < col:
                temp_node = board[i][j]
                if temp_node.name[0] == 'X' and temp_node.value is None:
                    check_node = True
                    break
                else:
                    j += 1
            if check_node:
                break
            else:
                i += 1

        if check_node:
            return False
        else:
            return True

    def set_copy_of_domain_each_node(self):
        for node in self.arrOfValueNodes:
            node.set_copy_of_domain()

    def set_copy_of_value_nodes(self):
        self.copyOfArrOfValueNodes = self.arrOfValueNodes.copy()

    @staticmethod
    def add_none_value_nodes(first_arr, second_arr):
        for x in first_arr:
            if x.value is None:
                if x not in second_arr:
                    second_arr.append(x)
            elif x.value is not None:
                if x in second_arr:
                    second_arr.remove(x)

    # use queue in this search that act like MRV and degree heuristic
    def backtrack_search_use_queue(self):
        Kakuro.add_none_value_nodes(self.arrOfValueNodes, self.copyOfArrOfValueNodes)
        heapq.heapify(self.copyOfArrOfValueNodes)
        if len(self.copyOfArrOfValueNodes) > 0 and not Kakuro.check_goal(self.row, self.col, self.board):
            node = heapq.heappop(self.copyOfArrOfValueNodes)
            Kakuro.least_constraining_value(node)
            if node.value is None:
                i = 0
                # chang it to while loop because for is not work good
                while i < len(node.copyOfDomain):
                    node.value = node.copyOfDomain[i]
                    node.copyOfDomain.remove(node.value)
                    # print(Kakuro.print_board_value(self.row, self.col, self.board))
                    print(f"{node}: {node.value}-----> {node.copyOfDomain}")
                    if Kakuro.valid_value(node):
                        if Kakuro.forward_checking(node):
                            Kakuro.add_none_value_nodes(self.arrOfValueNodes, self.copyOfArrOfValueNodes)
                            heapq.heapify(self.copyOfArrOfValueNodes)
                            if self.backtrack_search_use_queue():
                                return True

                    Kakuro.rec_forward_checking(node)
                    node.copyOfDomain.append(node.value)
                    node.copyOfDomain.sort()
                    node.copyOfDomain = list(dict.fromkeys(node.copyOfDomain))
                    # print (f"{node}----------->copy of domain before lcv{node.copyOfDomain}")
                    Kakuro.least_constraining_value(node)
                    node.value = None
                    # print(Kakuro.print_board_value(self.row, self.col, self.board))
                    i += 1
                # ------------------------------------------------------------------------------------------------------
                # change this code to while loop
                # for domain in node.copyOfDomain:
                #     node.value = domain
                #     node.copyOfDomain.remove(node.value)
                #     print(Kakuro.print_board_value(self.row, self.col, self.board))
                #     print(f"{node}: {node.value}-----> {node.copyOfDomain}")
                #     if Kakuro.valid_value(node):
                #         if Kakuro.forward_checking(node):
                #             Kakuro.add_none_value_nodes(self.arrOfValueNodes, self.copyOfArrOfValueNodes)
                #             heapq.heapify(self.copyOfArrOfValueNodes)
                #             if self.backtrack_search_use_queue():
                #                 return True
                #
                #     Kakuro.rec_forward_checking(node)
                #     node.copyOfDomain.append(node.value)
                #     node.copyOfDomain.sort()
                #     node.copyOfDomain = list(dict.fromkeys(node.copyOfDomain))
                #     # print (f"{node}----------->copy of domain before lcv{node.copyOfDomain}")
                #     Kakuro.least_constraining_value(node)
                #     node.value = None
                #     print(Kakuro.print_board_value(self.row, self.col, self.board))
                # ------------------------------------------------------------------------------------------------------

        else:
            print("*" * 64 + '\n')
            print(Kakuro.print_board_value(self.row, self.col, self.board))
            print("*" * 64)
            exit()

    def backtrack_search(self, number_in_arr_of_value):
        # we use not check_goal because we need it to be true when it is false.
        if number_in_arr_of_value < len(self.arrOfValueNodes) and not Kakuro.check_goal(self.row, self.col, self.board):
            node = self.arrOfValueNodes[number_in_arr_of_value]
            if node.value is None:
                for domain in node.copyOfDomain:
                    node.value = domain
                    # node.copyOfDomain.remove(node.value)
                    print(f"{node}: {node.value}-----> {node.copyOfDomain}")
                    # print(Kakuro.print_board_value(self.row, self.col, self.board))
                    if Kakuro.valid_value(node):
                        # if Kakuro.forward_checking(node):
                        if self.backtrack_search(number_in_arr_of_value + 1):
                            return True

                    # Kakuro.rec_forward_checking(node)
                    # node.copyOfDomain.append(node.value)
                    # node.copyOfDomain = list(dict.fromkeys(node.copyOfDomain))
                    # node.copyOfDomain.sort()
                    node.value = None
        else:
            print("*" * 64 + '\n')
            print(Kakuro.print_board_value(self.row, self.col, self.board))
            print("*" * 64)
            exit()

    @staticmethod
    def forward_checking(node):
        for x in node.verticalNeighbors:
            if node.value in x.copyOfDomain:
                x.copyOfDomain.remove(node.value)
            if len(x.copyOfDomain) <= 0 and x.value is None:
                return False
        for x in node.horizontalNeighbors:
            if node.value in x.copyOfDomain:
                x.copyOfDomain.remove(node.value)
            if len(x.copyOfDomain) <= 0 and x.value is None:
                return False
        return True

    @staticmethod
    def rec_forward_checking(node):
        for x in node.verticalNeighbors:
            if node.value in x.domain:
                x.copyOfDomain.append(node.value)
                x.copyOfDomain = list(dict.fromkeys(x.copyOfDomain))
                x.copyOfDomain.sort()
        for x in node.horizontalNeighbors:
            if node.value in x.domain:
                x.copyOfDomain.append(node.value)
                x.copyOfDomain = list(dict.fromkeys(x.copyOfDomain))
                x.copyOfDomain.sort()

    @staticmethod
    def valid_value(node):
        sum_vertical = node.value
        sum_horizontal = node.value
        count_h = 0
        count_v = 0
        for x in node.verticalNeighbors:
            if x.value is not None:
                if x.value == node.value:
                    return False
                count_v += 1
                sum_vertical += x.value
        for x in node.horizontalNeighbors:
            if x.value is not None:
                if x.value == node.value:
                    return False
                count_h += 1
                sum_horizontal += x.value

        if sum_horizontal > node.rowC:
            return False
        elif sum_vertical > node.colC:
            return False
        elif count_v == len(node.verticalNeighbors) and sum_vertical != node.colC:
            return False
        elif count_h == len(node.horizontalNeighbors) and sum_horizontal != node.rowC:
            return False
        else:
            return True

    @staticmethod
    def print_board_value(row, col, board):
        text = ""
        for i in range(0, row):
            for j in range(0, col):
                # because B nodes has no number in their name
                if board[i][j].value is None and board[i][j].type == 'value':
                    text += '0 '
                elif board[i][j].type == 'constraint':
                    if board[i][j].rowC is not None:
                        text += str(board[i][j].rowC) + " "
                    elif board[i][j].colC is not None:
                        text += str(board[i][j].colC) + " "
                elif board[i][j].type == 'blank':
                    text += '-1 '

                else:
                    text += str(board[i][j].value) + " "
            text += '\n'
        return text

    @staticmethod
    # LCV heuristic
    def least_constraining_value(node):
        arr = node.copyOfDomain
        neighbors = node.verticalNeighbors.copy()
        neighbors += node.horizontalNeighbors.copy()
        new_arr = []
        count_of_each_domain = {}

        for n in arr:
            counter = 0
            for neighbor in neighbors:
                if n in neighbor.domain:
                    counter += 1
            count_of_each_domain[n] = counter
        # print(f'{node}--------------------------------------------->new arr{count_of_each_domain}')
        result = sorted(count_of_each_domain, key=count_of_each_domain.get)
        if len(result) != len(arr):  # TODO check and put the domain that doesn't in neighbours
            print('---------------------------=========error=======================-----------------------------------')

        # for n in arr:
        #     for neighbor in neighbors:
        #         if n not in neighbor.domain and n not in new_arr:
        #             new_arr.append(n)
        # for n in arr:
        #     if n not in new_arr:
        #         new_arr.append(n)
        #

        # print(f'{node}--------------------------------------------->new arr{result}')
        node.copyOfDomain = result

    @staticmethod
    # MRV heuristic (NOT USE)
    def minimum_remaining_values(arr_of_nodes):
        heapq.heapify(arr_of_nodes)
        # arr_of_nodes.sort(key=lambda x: len(x.domain))
        # print(arr_of_nodes)
