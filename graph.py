from collections import defaultdict

## UNTESTED ##


class Vertex:
    def __init__(self, index, value):
        self.index = index
        self.value = value


class Graph:
    """TODO: Consider creating an O(1) look up for index to vertex"""
    def __init__(self):
        self.__vertices = []
        self.__adj_list = defaultdict(set)
        self.__index_to_vertex = defaultdict(Vertex)
        self.__edge_set = set()

    def add_edge(self, u: Vertex, v: Vertex):
        if u not in self.__vertices or v not in self.__vertices:
            print("graph.add_edge: invalid vertices given.")
            return None

        self.__adj_list[u].add(v)
        self.__adj_list[v].add(u)

    def set_edge_list(self):
        self.__edge_set = set()
        for v in self.__vertices:
            for u in self.__adj_list[v]:
                self.__edge_set.add({u, v})

    def add_vertex(self, v: Vertex):
        self.__vertices.append(v)
        self.__adj_list[v] = set()
        self.__index_to_vertex[v.index] = v

    def get_vertex(self, index):
        if type(index) != int:
            raise TypeError

        return self._get_vertex_from_index(index)

    def _get_vertex_from_index(self, index):
        return self.__index_to_vertex[index]

    def set_adjacency_set(self, v, a_set):
        for s in a_set:
            if type(s) is not Vertex:
                raise TypeError

        if type(v) is not Vertex:
            raise TypeError

        self.__adj_list[v] = set(a_set)

    def __getitem__(self, item):
        if type(item) is int:
            return self.__adj_list[self._get_vertex_from_index(item)]
        elif type(item) is Vertex:
            return self.__adj_list[item]
        else:
            raise TypeError

    @property
    def edge_set(self):
        self.set_edge_list()
        return self.__edge_set

    @property
    def vertices(self):
        return self.__vertices

    def __contains__(self, edge):
        if type(edge) is set:
            if edge in self.__edge_set:
                return True
            else:
                return False
        elif type(edge) is tuple:
            if edge[0] in self.__adj_list[edge[1]] and edge[1] in self.__adj_list[edge[0]]:
                return True
            else:
                return False
        else:
            raise TypeError
