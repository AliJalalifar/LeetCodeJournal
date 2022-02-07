class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.undir_graph_dict = self.undir_graph()
        self.dir_graph_dict = self.dir_graph()

    def undir_graph(self):
        neighbour_dict = {}
        for start, end in self.edges:
            if start == end:
                neighbour_dict[start] = []
                continue
            if start in neighbour_dict:
                neighbour_dict[start].append(end)
            else:
                neighbour_dict[start] = [end]
            if end in neighbour_dict:
                neighbour_dict[end].append(start)
            else:
                neighbour_dict[end] = [start]
        return neighbour_dict

    def dir_graph(self):
        neighbour_dict = {}
        for start, end in self.edges:
            if start == end:
                neighbour_dict[start] = []
                continue
            if start in neighbour_dict:
                neighbour_dict[start].append(end)
            else:
                neighbour_dict[start] = [end]
            if end not in neighbour_dict:
                neighbour_dict[end] = []

        return neighbour_dict

    def bfs(self, start, graph):
        queue = [start]
        while queue:
            start = queue.pop()
            visited.append(start)
            print(start)

            for neighbor in graph[start]:
                queue.insert(0, neighbor)



if __name__ == "__main__":
    routes = [
        ("1", "2"),
        ("4", "6"),
        ("5", "6"),
        ("6", "8"),
        ("7", "6"),
        ["3", "3"]
    ]
    routeGraph = Graph(routes)
    routeGraph.bfs('1', routeGraph.dir_graph_dict)