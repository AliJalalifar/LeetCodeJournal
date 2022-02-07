class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.dir_graph_dict = self.do_dir_graph_dict()
        self.undir_graph_dict = self.do_undir_graph_dict()

    def do_dir_graph_dict(self):
        dict_graph = {}
        for start, end in self.edges:
            if start in dict_graph:
                dict_graph[start].append(end)
            else:
                dict_graph[start] = [end]
        return dict_graph

    def do_undir_graph_dict(self):
        dict_graph = {}
        for start, end in self.edges:
            if start in dict_graph:
                dict_graph[start].append(end)
            else:
                dict_graph[start] = [end]
            if end in dict_graph:
                dict_graph[end].append(start)
            else:
                dict_graph[end] = [start]
        return dict_graph

    def get_path(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                new_paths = self.get_path(graph, node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def dfs_recur(self, graph, source):
        print(source)
        if source in graph:
            for neighbour in graph[source]:
                self.dfs_recur(graph, neighbour)

    def dfs_itr(self, graph, source):
        stack = [source]
        while stack:
            current = stack.pop()
            print(current)
            if current in graph:
                for neighbor in graph[current]:
                    stack.append(neighbor)

    def bfs_itr(self, graph, source):
        queue = [source]
        while queue:
            current = queue.pop()
            print(current)
            if current in graph:
                for node in graph[current]:
                    queue.insert(0, node)

    def has_path(self, graph, src, dst, visited_nodes=set()):

        if src in visited_nodes:
            return False

        visited_nodes.add(src)

        if src == dst:
            return True

        if src in graph:
            for neighbor in graph[src]:
                if self.has_path(graph, neighbor, dst, visited_nodes):
                    return True

        return False

    def connected_components_count(self, graph):
        connected = set()
        count = 0   
        for src in graph:
            if src not in connected:
                connected.add(src)
                for dst in graph:
                    if self.has_path(graph,src, dst, visited_nodes=set()):
                        connected.add(dst)
                count += 1
        return count


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
        ("1", "2"),
        ("4", "6"),
        ("5", "6"),
        ("6", "8"),
        ("7", "6"),
        ["3", "3"]
    ]
    routeGraph = Graph(routes)
    # # print(routeGraph.dfs("Toronto"))
    print(routeGraph.connected_components_count(routeGraph.undir_graph_dict))
