
def earliest_ancestor(ancestors, starting_node):
    heritage = {}

    for i in ancestors:
        if i[-1] not in heritage:
            heritage[i[-1]] = {i[0]}
        else:
            heritage[i[-1]].add(i[0])
    print(heritage)

# def bft/dft