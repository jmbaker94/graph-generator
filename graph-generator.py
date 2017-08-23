import random
from Graph import Graph, Vertex

## UNTESTED ## 


class GraphGenerator:
    def __init__(self):
        self.__method_list = ["random"]

        self.__n = None
        self.__m = None
        self.__connected = None
        self.__method = None

    def generate_erdos_renyi_graph(self, n=None, p=None, connected=True):
        """

        :param n: number of nodes in the resulting graph
        :param p: probability of two nodes being connected
        :param connected: whether the graph is required to be connected
        :return: None

        To produce such a graph we add in new vertices and connected them to each
        other vertex in the graph with probability p.

        If the graph is not required to be connected, return.

        If the graph is required to be connected...

        """
        if n is None or type(n) is not int:
            print("GraphGenerator.generate_erdos_renyi_graph: invalid vertices type")
            raise TypeError

        if type(p) is not float:
            print("GraphGenerator.generate_erdos_renyi_graph: invalid p (probability) type")
            raise TypeError
        elif 0 > p or p > 1:
            print("GraphGenerator.generate_erdos_renyi_graph: invalid p (probability) value")
            raise ValueError

        if connected not in [True, False]:
            print("GraphGenerator._check_parameters: invalid type for connected, defaulting to True.")
            self.__connected = True

        g = Graph()
        for i in range(1, n + 1):
            g.add_vertex(Vertex(i, None))
            for j in range(i + 1, n + 1):
                k = random.Random()
                if k < p:
                    g.add_edge(g[i], g[j])

        if len(self._find_connected_components(g)) != 1:
            pass

    @staticmethod
    def _find_connected_components(g):
        components = []
        frontier = [g[1]]

        while len(frontier) > 0:
            c = []
            f = []
            c.append(frontier[0])
            f.append(frontier[0])
            while len(f) > 0:
                for v in g[f[0]]:
                    if v not in c:
                        c.append(v)
                        f.append(v)
                f.pop(0)
            frontier.pop(0)

            component_g = Graph()

            for v in c:
                component_g.add_vertex(v)
                component_g.set_adjacency_set(v, g[v])

            components.append(component_g)
            used_v = []

            for l in components:
                for k in l.vertices:
                    used_v.append(k)

            for v in g.vertices:
                if v not in used_v:
                    frontier.append(v)
                    break

        return components

    def _generate_random_graph(self):
        pass

    def generate_random_tree(self, n):
        pass

    def _set_parameters(self, vertices, edges, connected, method):
        if type(vertices) is not int or type(edges) is not int:
            raise TypeError

        if connected not in [True, False]:
            print("GraphGenerator._check_parameters: invalid type for connected, defaulting to True.")
            self.__connected = True

        if method not in self.__method_list:
            print("GraphGenerator._check_parameters: invalid generation method type.")
            raise ValueError

        self.__n = vertices
        self.__m = edges
        self.__connected = connected
        self.__method = method
