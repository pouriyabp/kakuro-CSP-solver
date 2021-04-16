class Node:
    def __init__(self, type_of_node, row_index, col_index):
        self.type = type_of_node
        self.rowIndex = row_index
        self.colIndex = col_index
        self.value = None
        self.domain = []
        self.rowC = None
        self.colC = None

    def set_value(self, value):
        if self.type == "value":
            self.value = value
        else:
            return

    def set_row_constraint(self, row_constraint):
        if self.type == "constraint":
            self.rowC = row_constraint
        else:
            return

    def set_col_constraint(self, col_constraint):
        if self.type == "constraint":
            self.colC = col_constraint
        else:
            return

    def set_domain(self, array_of_domain):
        if self.type == "value":
            self.domain = array_of_domain
        else:
            return
    def __repr__(self):
       return f'({self.type}-{self.value}-{self.rowC}-{self.colC})'
