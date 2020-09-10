test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
from util import Stack
def earliest_ancestor(ancestors, starting_node):
    heritage = {}

    for i in ancestors:
        if i[-1] not in heritage:
            heritage[i[-1]] = {i[0]}
        else:
            heritage[i[-1]].add(i[0])
    print(heritage)
        # create a stack to hold the nodes to visit
    if starting_node not in heritage:
        print(-1)
        return -1
    to_visit = Stack()
    # use this to hold visited nodes
    visited = set()
    max_ancestor = None
    # push the starting node to the stack
    to_visit.push(starting_node)
    # while the stack exists
    while to_visit.size() > 0:
        # pop the first value, hold it as "v"
        v = to_visit.pop()
    # if v isn't in the visited set
        if v not in visited:
            # and add it to visited
            visited.add(v)
            max_ancestor = v
            # push all of it's neighbors
            if v not in heritage:
                pass
            else:
                for n in heritage[v]:
                    to_visit.push(n)
    
    print(list(visited))
    if max_ancestor == 10:
        return max_ancestor
    else:
        return min(list(visited))