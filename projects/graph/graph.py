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
             #node: 0, #neighbors: 1, 3
            if v1 not in self.vertices:
                print(f"{v1} not real vertex!")
                return
            if v2 not in self.vertices:
                print(f"{v2} not real vertex!")
                return
            self.vertices[v1].add(v2)
            # pass  # TODO

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
        # create a queue to hold nodes to visit
        to_visit = Queue()
        # create a set to hold visited nodes
        visited = set()
        # enqueue the starting node 
        to_visit.enqueue(starting_vertex)
        #if that starting node isn't in the vertices, return an error
        if starting_vertex not in self.vertices:
            print(f"Error! {starting_vertex} not in current graph.")
            return
        # to_visit gets initialized with 1 node in it.
        # SO
        # while to_visit is greater than 0
        while to_visit.size() > 0:
            # make that first node the variable v
            # and set it up to be dequeued'
            v = to_visit.dequeue()
        # if the node hasn't been visited
            if v not in visited:
                # print the node
                print(v)
                # add it to visited
                visited.add(v)
                # then loop through each of the node's neighbors
                # and enqueue each of them
                for each_neighbor in self.vertices[v]:

                    to_visit.enqueue(each_neighbor)
        # pass  # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack to hold the nodes to visit
        to_visit = Stack()
        # use this to hold visited nodes
        visited = set()
        # push the starting node to the stack
        to_visit.push(starting_vertex)
        # while the stack exists
        while to_visit.size() > 0:
            # pop the first value, hold it as "v"
            v = to_visit.pop()
        # if v isn't in the visited set
            if v not in visited:
                #print it
                print(v)
                # and add it to visited
                visited.add(v)
                # push all of it's neighbors
                for n in self.vertices[v]:
                    to_visit.push(n)
        # pass  # TODO

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()

        if starting_vertex in visited:
            return
        
        print(starting_vertex)

        for n in self.vertices[starting_vertex]:
            visited.add(starting_vertex)
            self.dft_recursive(n, visited)
        # pass  # TODO

    def bfs(self, starting_vertex, target_vertex):
        # Create an empty queue
        to_visit = Queue()
        # enqueue A PATH TO the starting vertex ID
        to_visit.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while to_visit.size() > 0:
        # Dequeue the first PATH
            v = to_visit.dequeue()
        # Grab the last vertex from the PATH
            v2 = v[-1]
        # If that vertex has not been visited...
            if v2 not in visited:
            # CHECK IF IT'S THE TARGET
                if v2 == target_vertex:
                # IF SO, RETURN PATH
                    return v
            # Mark it as visited...
                visited.add(v2)
            # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.vertices[v2]:
                    to_visit.enqueue(v+[neighbor])     
                # COPY THE PATH
                # APPEND THE NEIGHOR TO THE BACK

    def dfs(self, starting_vertex, destination_vertex):
        # Create an empty stack
        to_visit = Stack()
        # push A PATH TO the starting vertex ID
        to_visit.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while to_visit.size() > 0:
        # Pop the first PATH
            v = to_visit.pop()
        # Grab the last vertex from the PATH
            v2 = v[-1]
        # If that vertex has not been visited...
            if v2 not in visited:
            # CHECK IF IT'S THE TARGET
                if v2 == destination_vertex:
                # IF SO, RETURN PATH
                    return v
            # Mark it as visited...
                visited.add(v2)
            # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.vertices[v2]:
                    to_visit.push(v+[neighbor])     
                # COPY THE PATH
                # APPEND THE NEIGHOR TO THE BACK

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # For recursion...
        # to start, visited is blank
        # if visited has items, this skips
        if visited == None:
            visited = set()

        # start by adding starting_vertex to visited
        visited.add(starting_vertex)
        # if the starting vertex is destination, we're done
        if starting_vertex == destination_vertex:
            return [starting_vertex]
        
        # for each of the starting vertex neighbor
        for each_neighbor in self.vertices[starting_vertex]:
            #if the neighbor hasnt been visited
            if each_neighbor not in visited:
                # recurse, using the new visited, and each neighbor
                x = self.dfs_recursive(each_neighbor, destination_vertex, visited)
                # if recurse is successful
                if x != None:
                    # return the starting vertex plus the recurse vertex to build path
                    return [starting_vertex]+x
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))