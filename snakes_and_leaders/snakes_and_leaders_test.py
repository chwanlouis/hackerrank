class SnakesAndLadders(object):

	def __init__(self, ladders, snakes):
		self.ladders = ladders
		self.snakes = snakes
		self.nodes = 15
		self.pathway_matrix = self.build_pathway_matrix(self.ladders, self.snakes)
		# print self.pathway_matrix
		self.pathway_matrix = self.floyd_warshall_algorithm(self.pathway_matrix)
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
		print 'chess_board_pathway_init'
		self.print_matrix(pathway_matrix)
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
			for k in range(1,7):
				if i + k < self.nodes:
					pathway_matrix[i][i+k] = 1
		print 'dice_move_import'
		self.print_matrix(pathway_matrix)
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
			pathway_matrix[start-1][end-1] = 0
		for snake in snakes:
			start, end = snake
			pathway_matrix[start-1][end-1] = 0
		print 'ladders_and_snakes_import'
		self.print_matrix(pathway_matrix)
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
		print 'resolve_connectivity'
		self.print_matrix(pathway_matrix)
		return pathway_matrix

	def build_pathway_matrix(self, ladders, snakes):
		pathway_matrix = self.chess_board_pathway_init()
		pathway_matrix = self.dice_move_import(pathway_matrix)
		pathway_matrix = self.ladders_and_snakes_import(pathway_matrix, ladders, snakes)
		pathway_matrix = self.resolve_connectivity(pathway_matrix)
		return pathway_matrix

	def floyd_warshall_algorithm(self, pathway_matrix):
		for i in range(self.nodes):
			for j in range(self.nodes):
				for k in range(self.nodes):
					if i != j and j != k:
						if pathway_matrix[i][j] > pathway_matrix[i][k] + pathway_matrix[k][j]:
							pathway_matrix[i][j] = pathway_matrix[i][k] + pathway_matrix[k][j]
							# if i == 0 and j == self.nodes-1:
							# 	# print pathway_matrix[i][j]
		print 'floyd_warshall_algorithm'
		self.print_matrix(pathway_matrix)
		return pathway_matrix

	def print_matrix(self, matrix):
		for row in matrix:
			print row

	def get_iterations(self):
		return self.pathway_matrix[0][self.nodes-1]


if __name__ == '__main__':
	ladders = [[3,14]]
	snakes = [[13,4], [12,2]]
	chess_board = SnakesAndLadders(ladders, snakes)
	print chess_board.get_iterations()