class Node:
    def __init__(self, type_of_node, row_index, col_index):
        self.type = type_of_node
        self.rowIndex = row_index
        self.colIndex = col_index
        self.value = None
        self.domain = []
        self.copyOfDomain = []
        self.rowC = None
        self.colC = None
        self.name = None
        self.horizontalNeighbors = []
        self.verticalNeighbors = []

    def set_name(self):
        if self.type == "value":
            self.name = 'X' + str(self.rowIndex) + str(self.colIndex)
        elif self.type == "constraint":
            self.name = 'C' + str(self.rowIndex) + str(self.colIndex)
        else:
            self.name = "B"

    def set_value(self, value):
        if self.type == "value":
            self.value = value
        else:
            return

    def set_row_constraint(self, row_constraint):
        # if self.type == "constraint":
        self.rowC = row_constraint

    def set_col_constraint(self, col_constraint):
        # if self.type == "constraint":
        self.colC = col_constraint

    def set_domain(self, array_of_domain):
        if self.type == "value":
            self.domain = array_of_domain
        else:
            return

    def __repr__(self):
        # return f'({self.type}-{self.value}-{self.rowC}-{self.colC})'
        return f"{self.name}"

    def add_vertical_neighbors(self, arr):
        self.verticalNeighbors = arr

    def add_horizontal_neighbors(self, arr):
        self.horizontalNeighbors = arr

    def set_copy_of_domain(self):
        self.copyOfDomain = self.domain.copy()

    def __gt__(self, other):
        # degree heuristic
        if len(self.domain) == len(other.domain):
            return (len(self.horizontalNeighbors) + len(self.verticalNeighbors)) > (
                    len(other.horizontalNeighbors) + len(other.verticalNeighbors))
        # MRV heuristic
        return len(self.domain) > len(other.domain)
