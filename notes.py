"""
Graphs
_______________

Nodes connected by edges



Directed graphs have one way edges.
If any node has a one way edge, it's directed.

Undirected graphs have no specific direction of relationship
between nodes.

If there are no arrows between two nodes in the visual representation
of the graph, it's an undirected graph.


Cyclic vs Acyclic Graphs:
    A "Cyclic" graph has a way to get back to a node that has already been visited.

    If there is a cycle anywhere in the graph, the whole graph can be 
    thought of as being cyclic.

    Linked lists are not cyclic. They are Acyclic. There is no way to
    loop back to a previously visited node.

    Weighted edges:
    "Cost" with traversing along an edge is the "weight" of that edge.


"""

"""
LL REVIEW

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

Graph Template
"""

# This is a node in the form of a graph node
class Node:
    # it gets initialized the same
    # instead of having a next value
    # it has a more general "self.neighbors" value
    # which can hold all other nodes which are neighbors
    def __init__(self, value):
        self.value = value
        #self.next = None
        # Here is the neighbors value.
        # this is known as
        # Adjacency list 
        self.neighbors = []

    def __repr__(self):
        # a nice printing function
         return f"Node({repr(self.value)})"

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


def bft(node):
    # create a queue to hold nodes to visit
    to_visit = Queue()

    # create a set to hold visited nodes
    visited = set()

    #initialize: add the starting node to the queue
    to_visit.enqueue(node)

    # while the queue is not empty
    while to_visit.size() > 0:

    # 1. dequeue the first edntry
        v = to_visit.dequeue()

    # 3. if it hasn't been visited:
        if v not in visited:

            # visit the node(print)
            print(v)

            # put it in the visited list.
            visited.add(v)

            # enqueue all of it's neighbors
            for n in v.neighbors:

                print(f"Adding: {n}")
                to_visit.enqueue(n)

    # and that's it! Finished a breadth first traversal.
    # this will enqueue the starting node, then it will encueue all of the neighbors
    # of the starting node.
    # this will print each node in breadth first fashion.


def dft(node):
    # create a stack to hold nodes to visit
    to_visit = Stack()

    # create a set to hold visited nodes
    visited = set()

    #initialize: push the starting node to the stack
    to_visit.push(node)

    # while the queue is not empty
    while to_visit.size() > 0:

    # 1. pop the first entry
        v = to_visit.pop()

    # 2. if it hasn't been visited:
        if v not in visited:

            # visit the node(print)
            print(v)

            # put it in the visited list.
            visited.add(v)

            # push all of it's neighbors
            for n in v.neighbors:
                print(f"Pushing: {n}")
                to_visit.push(n)


# making some nodes
# Node with value 'A'
a = Node('A')
# Node with value 'B'
b = Node('B')
# Node with value 'C'
c = Node('C')

# # putting neighbors into A so that it's connected
a.neighbors.append(b)
a.neighbors.append(c)
# here's a list of a's neighbors
print(a.neighbors)


# make some neighbors for b
# b connects to itsself
b.neighbors.append(b)

# b connecting to c
b.neighbors.append(c)
# c connects to b
c.neighbors.append(b)

bft(a)
### If you want to make an undirectional graph
### two nodes must be connected back and forth


"""
Think about traversing the graph.

Linked lists use .next. 

What would graphs use to traverse through?
How can you escape cycles?
Keep a list of the visited nodes. It'll help!

Depending on the application, we will always have a different
starter point.

Different Traversals:
Breadth-First Traversal
Depth-First Traversal

Breadth-first traversals visits all nodes in the same distance layer from the start
Visit all nodes distance 0 away from start
then visit all nodes distance 1 away from start
Order doesn't matter , as long as all nodes of the same distance are checked
before moving onto the next distance.
This is considered "layers". We are covering the graph at the breadth
over the depth of the graph.


Depth-First Traversals visit nodes at each distance layer until a deepest
layer node is hit with no further depth available. It'll traverse "down"
through the depths of each breadth, hitting one node at each layer, until
the end is it. We then turn back to the highest level node which has not 
been traversed, and then go all the way down again.

"""

# We've already made the class, and instantiated some nodes
# writing out some pseudo code for breadth first traversals
#BREADTH FIRST
# make a Queue and a Visited
# Remember First in first out for Queues


# 1. add the first node to the queue
# 2. If it's been visited, skip it. This step happens with all nodes.
# 3. if it hasn't been visited, put it in the visited list. 
# 4. take the first out of the queue. Add all of it's neighbors
# take the first neighbor, and repeat 1, 2, 3, 4.

# This works because of the queue functionality.
#  By adding in the neighbors to the end of our queue, we make sure
#  that all neighbors of the highest depth are visited.
# Another way to say the last sentence
# We make sure that all neighbors of the same breadth are visited
# Before moving onto the next breadth.
# A third re-phrasal.
# We make sure to check all neighbors of the same depth, before moving
# onto the next level of depth.

# Depth first traversals are great for pathfinding mazes
# also for maze - generation
# because we go all the way to an endpoint before going back up a
# graph
# in depth first, the stack gets first in first out treatment
# this means that the most recent things added are the things
# getting removed and moved into the visited section first
# Depth first traversals are very possible when using recursion

# heres some pseudo code for a recursive dft
# add a base case as a method of exiting the recursion
"""
def def_recursive(node):
    for n in node.neighbors:
        dft_recursive(n)
"""
###############################################

# Breadth first searches
# gets us the shortest path between two nodes
# use a variant of the breadth first traversal
# it's called a breadth first search

# keep track of the path taken so far for each of the nodes
# enqueue the whole path before throwing anything away.
# add the final element of a path to the visited list
# when all paths are enqueued
# This can be rephrased
# enqueue a tuple containing the path of the traversal
# before de-queue-ing a path, check if the last element of the path
# is in the visited set. if it is, delete it.
# as soon as the destination node is added into the queue, we're done!
# this is the shortest path to it.
# This is a vital property of BFT. In a breadth first search,
# the first time we come across our destination, it is automatically
# the shortest path to that node.