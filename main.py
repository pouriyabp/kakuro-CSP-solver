import Kakuro
import Node

if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        cols = int(f.readline()[0])
        rows = int(f.readline()[0])
        game = Kakuro.Kakuro(rows, cols)
        print(f"rows is {rows} cols is {cols}")
        i = 0
        j = 0
        while i < rows:
            listOfcells = []
            data = f.readline()
            data = data.replace('\n', ' ')
            data = list(data)
            for x in range(0, data.count(' ')):
                temp = data[:data.index(' ')]
                text = ''
                for n in temp:
                    text = text + n
                    data.remove(n)
                data.remove(' ')
                listOfcells.append(int(text))  # TODO: solve the problem if i have both row and col consistency.
            # print(listOfcells)
            while j < cols:
                if listOfcells[j] == 0:
                    tempNode = Node.Node('value', i, j)
                    tempNode.set_name()
                    # tempNode.set_domain([1, 2, 3, 4, 5, 6, 7, 8, 9])
                    listOfcells[j] = tempNode
                elif listOfcells[j] == -1:
                    tempNode = Node.Node('blank', i, j)
                    tempNode.set_name()
                    listOfcells[j] = tempNode
                else:
                    tempNode = Node.Node('constraint', i, j)
                    tempNode.set_name()
                    if i == 0:
                        tempNode.set_col_constraint(listOfcells[j])
                    elif i != 0 and j == 0:
                        tempNode.set_row_constraint(listOfcells[j])
                    elif i != 0 and j == cols - 1:
                        tempNode.set_col_constraint(listOfcells[j])
                    elif i == rows - 1 and j != 0:
                        tempNode.set_row_constraint(listOfcells[j])
                    listOfcells[j] = tempNode
                j += 1
            # print(listOfcells)
            game.add_nodes_to_board(listOfcells)
            i += 1
            j = 0

        print(game.print_board())
        game.find_neighbors()
        game.set_domain_to_each_node()
        game.solve()
