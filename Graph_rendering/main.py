from Graph_rendering import Graph
from Graph_rendering import Algorithms

if __name__ == '__main__':
    graph = Graph.Graph()
    graph.draw_graph()
    visited = set()
    #Algorithms.DFS(graph, visited, 0)  # TODO need random node in input
    Algorithms.BFS(graph, visited, 0)
