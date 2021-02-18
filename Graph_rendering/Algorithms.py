from Graph_rendering import Graph
import collections
import time

NODE_COLOR = "red"
NODE_COLORS = ["red", "blue", "green", "orange", "grey", "pink"]  # enough?


def DFS(graph: Graph, visited, node, counter=0):  # done i guess
    if node not in visited:
        counter += 1
        file_name = 'DFS_result\DFS_step_' + str(counter) + '.gv'
        graph.graphviz_graph.node(str(node), fillcolor=NODE_COLOR, style="filled")
        graph.graphviz_graph.render(filename=file_name, view=False)
        visited.add(node)
        for neighbour in graph.adjacency_list[node]:
            counter = DFS(graph, visited, neighbour, counter)
    return counter


def BFS(graph: Graph, visited, node):
    queue = collections.deque([node])
    visited.add(node)
    counter = 1
    color_count = 0
    file_name = 'BFS_result\BFS_step_' + str(counter) + '.gv'
    graph.graphviz_graph.node(str(node), fillcolor=NODE_COLOR, style="filled")
    graph.graphviz_graph.render(filename=file_name, view=False)

    # graph.()
    while queue:
        vertex = queue.popleft()
        print(vertex)
        color_count += 1
        for neighbour in graph.adjacency_list[vertex]:

            if neighbour not in visited:
                counter += 1
                file_name = 'BFS_result\BFS_step_' + str(counter) + '.gv'
                visited.add(neighbour)
                graph.graphviz_graph.node(str(neighbour), fillcolor=NODE_COLORS[color_count], style="filled")
                # graph.draw_graph()
                graph.graphviz_graph.render(filename=file_name, view=False)
                queue.append(neighbour)
    return