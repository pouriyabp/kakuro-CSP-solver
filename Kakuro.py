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
