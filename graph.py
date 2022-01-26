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

    def dfs_recursion(self, source):
        print(source)
        if source not in self.dict_graph:
            return
        for neighbour in self.dict_graph[source]:
            self.dfs_recursion(neighbour)

    def dfs_iteration(self, source):
        stack = [source]
        while stack:
            current = stack.pop()
            print(current)
            if current in self.dict_graph:
                for neighbor in self.dict_graph[current]:
                    stack.append(neighbor)


if __name__ == "__main__":

    # routes = [
    #     ("Toronto", "Montreal"),
    #     ("Montreal", "Dubai"),
    #     ("Dubai", "Istanbul"),
    #     ("Toronto", "Dubai"),
    #     ("Toronto", "Istanbul"),
    #     ("Istanbul", "Tehran")
    # ]
    routes = [
        ("a", "b"),
        ("a", "c"),
        ("b", "d"),
        ("d", "f"),
        ("c", "e")
    ]
    routeGraph = DirectionalGraph(routes)
    # print(routeGraph.dfs("Toronto"))
    routeGraph.dfs_iteration("a")
