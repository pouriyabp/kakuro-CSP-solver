class Kakuro:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = []

    def add_nodes_to_board(self, array_of_nodes):
        self.board.append(array_of_nodes)
