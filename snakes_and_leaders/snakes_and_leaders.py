class SnakesAndLadders(object):
    def __init__(self, ladders, snakes):
        self.ladders = ladders
        self.snakes = snakes
        self.nodes = 100
        self.pathway_matrix = self.build_pathway_matrix(self.ladders, self.snakes)
        # print self.pathway_matrix
        self.shortest_distance_matrix = self.floyd_warshall_algorithm(self.pathway_matrix)

    # print self.pathway_matrix

    def chess_board_pathway_init(self):
        """
        Return the pathway matrix represented by a 2d array
        define zero iterations passing the original node to itself
        node 1 => node 1 : iterations = 0

        @rtype:   list of list
        @return:  2d list with length 100
        """
        pathway_matrix = list()
        for i in range(self.nodes):
            row = list()
            for j in range(self.nodes):
                if i != j:
                    row.append(None)
                else:
                    row.append(0)
            pathway_matrix.append(row)
        return pathway_matrix

    def dice_move_import(self, pathway_matrix):
        """
        Return the pathway matrix represented by a 2d array
        with dice move of 1 iteration
        dice number = 1, 2, 3, 4, 5, 6
        node 2 => node 3 : iterations = 1
        node 2 => node 4 : iterations = 1
        node 2 => node 5 : iterations = 1
        node 2 => node 6 : iterations = 1
        node 2 => node 7 : iterations = 1
        node 2 => node 8 : iterations = 1

        @rtype:   list of list
        @return:  2d list with length 100
        """
        for i in range(self.nodes):
            for k in range(1, 7):
                if i + k < self.nodes:
                    pathway_matrix[i][i + k] = 1
        return pathway_matrix

    def ladders_and_snakes_import(self, pathway_matrix, ladders, snakes):
        """
        Return the pathway matrix represented by a 2d array
        with ladder move of 0 iteration
        give ladder is 21 to 65
        node 21 => node 65 : iterations = 0

        @rtype:   list of list
        @return:  2d list with length 100
        """
        for ladder in ladders:
            start, end = ladder
            pathway_matrix[start - 1][end - 1] = 0
        for snake in snakes:
            start, end = snake
            pathway_matrix[start - 1][end - 1] = 0
        return pathway_matrix

    def resolve_connectivity(self, pathway_matrix):
        """
        Return the pathway matrix represented by a 2d array
        filling unavailable path with sufficient large number as penalty
        give node 2 to 1 is unavailable
        node 2 => node 1 : iterations = 10000

        @rtype:   list of list
        @return:  2d list with length 100
        """
        penalty = 10000
        for i in range(self.nodes):
            for j in range(self.nodes):
                if pathway_matrix[i][j] is None:
                    pathway_matrix[i][j] = penalty
        return pathway_matrix

    def build_pathway_matrix(self, ladders, snakes):
        pathway_matrix = self.chess_board_pathway_init()
        pathway_matrix = self.dice_move_import(pathway_matrix)
        pathway_matrix = self.ladders_and_snakes_import(pathway_matrix, ladders, snakes)
        pathway_matrix = self.resolve_connectivity(pathway_matrix)
        return pathway_matrix

    def floyd_warshall_algorithm(self, pathway_matrix):
        shortest_distance_matrix = [row for row in pathway_matrix]
        for i in range(self.nodes):
            for j in range(self.nodes):
                for k in range(self.nodes):
                    if pathway_matrix[i][j] > pathway_matrix[i][k] + pathway_matrix[k][j]:
                        pathway_matrix[i][j] = pathway_matrix[i][k] + pathway_matrix[k][j]
        return shortest_distance_matrix

    def get_iterations(self):
        return self.shortest_distance_matrix[0][-1]


class InputAdapter(object):
    def __init__(self):
        self.number_of_test = int(raw_input())
        self.ladders = list()
        self.snakes = list()
        for i in range(self.number_of_test):
            number_of_leaders = int(raw_input())
            all_leaders = list()
            for _ in range(number_of_leaders):
                head, tail = str(raw_input()).split(' ')
                leader = [int(head), int(tail)]
                all_leaders.append(leader)
            self.ladders.append(all_leaders)
            number_of_snakes = int(raw_input())
            all_snakes = list()
            for _ in range(number_of_snakes):
                head, tail = str(raw_input()).split(' ')
                snake = [int(head), int(tail)]
                all_snakes.append(snake)
            self.snakes.append(all_snakes)

    def solve(self):
        """
        By Using the class SnakesAndLadders to solve the input source
        """
        for ladders, snakes in zip(self.ladders, self.snakes):
            chess_board = SnakesAndLadders(ladders, snakes)
            iterations = chess_board.get_iterations()
            print iterations


if __name__ == '__main__':
    program = InputAdapter()
    program.solve()
