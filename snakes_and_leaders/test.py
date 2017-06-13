def floyd_warshall_algorithm(pathway_matrix):
    nodes = len(pathway_matrix)
    shortest_distance_matrix = [row for row in pathway_matrix]
    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):
                if pathway_matrix[i][j] > pathway_matrix[i][k] + pathway_matrix[k][j]:
                    pathway_matrix[i][j] = pathway_matrix[i][k] + pathway_matrix[k][j]
    return shortest_distance_matrix


if __name__ == '__main__':
    p = 100000
    pathway_matrix = [[0, 5, p, 10],
                      [p, 0, 3, p],
                      [p, p, 0, 1],
                      [p, p, p, 0]]
    shortest_distance_matrix = floyd_warshall_algorithm(pathway_matrix)
    for row in shortest_distance_matrix:
        print row
