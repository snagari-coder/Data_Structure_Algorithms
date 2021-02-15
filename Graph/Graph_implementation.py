# A graph can be represented in three ways: Edge list, adjaceny list; adjaceny matrix
# The following graph implementation is using adjaceny list.


class Graph():
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}

    def insert_node(self, data):
        if data not in self.adjacency_list:
            self.adjacency_list[data] = []
            self.number_of_nodes += 1
            return

    def insert_edge(self, node1, node2):
        if node2 not in self.adjacency_list[node1]:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)
            return
        else:
            return "Edge already exists"

    def show_connections(self):
        for node in self.adjacency_list:
            print(f'{node} --> {" ".join(map(str, self.adjacency_list[node]))}')


my_graph = Graph()
my_graph.insert_node(0)
my_graph.insert_node(1)
my_graph.insert_node(2)
my_graph.insert_node(3)
my_graph.insert_node(4)
my_graph.insert_node(5)
my_graph.insert_node(6)
my_graph.insert_edge(3, 1)
my_graph.insert_edge(3, 4)
my_graph.insert_edge(4, 2)
my_graph.insert_edge(4, 5)
my_graph.insert_edge(1, 2)
my_graph.insert_edge(1, 0)
my_graph.insert_edge(0, 2)
my_graph.insert_edge(6, 5)

my_graph.show_connections()
print(my_graph.adjacency_list)
print(my_graph.number_of_nodes)
