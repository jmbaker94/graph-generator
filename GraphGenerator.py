

class GraphGenerator:
    def __init__(self):
        self.__method_list = ["random"]

        self.__n = None
        self.__m = None
        self.__connected = None
        self.__method = None

    def generate_graph(self, vertices=None, edges=None, connected=True, method=None):
        self._check_parameters(vertices, edges, connected, method)
        if method == "random":
            return self._generate_random_graph()

    def _check_parameters(self, vertices, edges, connected, method):
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
