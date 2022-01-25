class DirectionalGraph:

    def __init__(self, edges):
        self.edges = edges
        self.dict_graph = {}
        for start, end in self.edges:
            if start in self.dict_graph:
                self.dict_graph[start].append(end)
            else:
                self.dict_graph[start] = [end]

    def get_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.dict_graph:
            return []
        paths = []
        for node in self.dict_graph[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths


if __name__ == "__main__":

    routes = [
        ("Toronto", "Montreal"),
        ("Montreal", "Dubai"),
        ("Dubai", "Tehran"),
        ("Toronto", "Dubai"),
        ("Toronto", "Istanbul"),
        ("Istanbul", "Tehran"),
        ("Tehran", "Istanbul")
    ]
    routeGraph = DirectionalGraph(routes)
    routeGraph.get_path("Toronto", "Tehran")
