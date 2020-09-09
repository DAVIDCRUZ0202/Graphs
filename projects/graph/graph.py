"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
# in the file 'graph.py', implement a 'Graph class'
class Graph:
# that supports the Application Programming Interface(API) in the example
# below.




# # This means there should be a field of 'vertices' that contains a dictionary
# mapping vertex labels to edges. For example:
# ```python
# {
# '0': {'1', '3'},
# '1': {'0'},
# '2': set(),
# '3': {'0'}
# This represents a graph with four vertices and two total (bidirectional) edges.
# The vertex ''2'' has no edges, while "0" is connected to both "1', and "3".
# }


# """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
# This means there should be a field 'vertices' that contains a dictionary
# mapping vertex labels to edges. For example:
        self.vertices = {}

    # # create add_vertex method , use this to add a Vertex Key to the graph
    # add a vertex to a graph here
    def add_vertex(self, vertex_id):
            """
            Add a vertex to the graph.
            """
            self.vertices[vertex_id] = set()
            # pass # TODO

    def add_edge(self, v1, v2):
            """
            Add a directed edge to the graph.
            """
            self.edge = (v1, v2)
                        #node: 0, #neighbors: 1, 3
            if v1 not in self.vertices:
                print(f"{v1} not real vertex!")
                return
            if v2 not in self.vertices:
                print(f"{v2} not real vertex!")
                return
            # pass  # TODO
            # make the connection here
            #self.vertices[1].add(0)
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        for each_id in self.vertices[vertex_id]:
            print(each_id)


        # pass  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # CHECK CLASS NOTES FOR DESCRIPTION ON WHAT EACH BIT DOES
        to_visit = Queue()

        visited = set()

        to_visit.enqueue(starting_vertex)

        if starting_vertex not in self.vertices:
            print(f"Error! {starting_vertex} not in current graph.")
            return

        while to_visit.size() > 0:

            v = to_visit.dequeue()

        if v not in visited:
            print(v)

            visited.add(v)

            for each_neighbor in self.get_neighbors(v):

                print(f"Enqueue-ing: {each_neighbor}")
                to_visit.enqueue(each_neighbor)
        # pass  # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # CHECK CLASS NOTES FOR DESCRIPTION ON WHAT EACH BIT DOES
        
        to_visit = Stack()

        visited = set()

        to_visit.push(starting_vertex)

        while to_visit.size() > 0:

            v = to_visit.pop()

        if v not in visited:

            print(v)

            visited.add(v)
            # push all of it's neighbors
            for n in self.get_neighbors(n):
                print(f"Pushing: {n}")
                to_visit.push(n)
        # pass  # TODO

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        to_visit = Stack()

        visited = set()

        to_visit.push(starting_vertex)

        v = to_visit.pop()

        if v not in visited or v != None:
            print(v)

            visited.add(v)

        
        for n in self.vertices[starting_vertex]:
            dft_recursive(n)
        # pass  # TODO

        
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('1', '0')
graph.add_edge('0', '3')
graph.add_edge('3', '0')
for vertex in graph.vertices:
    print(f"Graph Node:{vertex}. with neighbors {graph.vertices[vertex]}")
print(f"type 'graph.add_edge('0', '4') to see an error")
breakpoint()

#     def bfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing the shortest path from
#         starting_vertex to destination_vertex in
#         breath-first order.
#         """
#         pass  # TODO

#     def dfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing a path from
#         starting_vertex to destination_vertex in
#         depth-first order.
#         """
#         pass  # TODO

#     def dfs_recursive(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing a path from
#         starting_vertex to destination_vertex in
#         depth-first order.

#         This should be done using recursion.
#         """
#         pass  # TODO

# if __name__ == '__main__':
#     graph = Graph()  # Instantiate your graph
#     # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)
#     graph.add_vertex(4)
#     graph.add_vertex(5)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_edge(5, 3)
#     graph.add_edge(6, 3)
#     graph.add_edge(7, 1)
#     graph.add_edge(4, 7)
#     graph.add_edge(1, 2)
#     graph.add_edge(7, 6)
#     graph.add_edge(2, 4)
#     graph.add_edge(3, 5)
#     graph.add_edge(2, 3)
#     graph.add_edge(4, 6)

#     '''
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
#     print(graph.vertices)

#     '''
#     Valid BFT paths:
#         1, 2, 3, 4, 5, 6, 7
#         1, 2, 3, 4, 5, 7, 6
#         1, 2, 3, 4, 6, 7, 5
#         1, 2, 3, 4, 6, 5, 7
#         1, 2, 3, 4, 7, 6, 5
#         1, 2, 3, 4, 7, 5, 6
#         1, 2, 4, 3, 5, 6, 7
#         1, 2, 4, 3, 5, 7, 6
#         1, 2, 4, 3, 6, 7, 5
#         1, 2, 4, 3, 6, 5, 7
#         1, 2, 4, 3, 7, 6, 5
#         1, 2, 4, 3, 7, 5, 6
#     '''
#     graph.bft(1)

#     '''
#     Valid DFT paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
#     graph.dft(1)
#     graph.dft_recursive(1)

#     '''
#     Valid BFS path:
#         [1, 2, 4, 6]
#     '''
#     print(graph.bfs(1, 6))

#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
#     print(graph.dfs(1, 6))
#     print(graph.dfs_recursive(1, 6))