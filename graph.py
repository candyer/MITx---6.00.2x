class Node():
    def __init__(self, name):
        self.name = name
        self.kids = []
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
a.kids.append(b)
a.kids.append(c)
b.kids.append(d)
b.kids.append(c)
c.kids.append(e)
c.kids.append(a)
d.kids.append(c)
d.kids.append(d)
e.kids.append(a)


# a = Node('A')
# b = Node('B')
# c = Node('C')
# d = Node('D')
# e = Node('E')
# a.kids.append(b)
# b.kids.append(c)
# c.kids.append(a)
# c.kids.append(d)
# c.kids.append(e)
# e.kids.append(a)

# doesnt search for anything and loop forever
def DFS1(n):
    """n is a node"""
    for kid in n.kids:
        DFS1(kid)

# loop forever
def DFS2(n, dest):
    """n: the current node
       dest: what we are searching for
    """
    if n == dest:
        print 'I found it'
    for kid in n.kids:
        DFS2(kid, dest)

# it doesnt give the path, it's useless
def DFS3(n, dest, seen=[]):
    """n: the current node
       dest: what we are searching for
       seen: all the node we already visited
    """
    if n in seen:
        # we already came here !
        return
    seen.append(n)

    if n == dest:
        print 'I found it'
    for kid in n.kids:
        DFS3(kid, dest, seen)


# we dont know if its the shortest path
def DFS4(n, dest, seen=[], path=[]):
    """n: the current node
       dest: what we are searching for
       seen: all the node we already visited
       path: to the current node n
    """
    if n in seen:
        # we already came here !
        return
    seen.append(n)

    path.append(n)
    if n == dest:
        print 'I found it'
        print path
    for kid in n.kids:
        DFS4(kid, dest, seen, path)
    path.pop()


def DFS4p5(n, dest, path, solutions):
    """n: the current node
       dest: what we are searching for
       path: to the current node n
       solutions: all paths to dest
    """
    path.append(n)
    if n == dest:
        print 'I found it'
        print path
        solutions.append(path[:])

    if n in path[:-1]:
        # we already came here !
        path.pop()
        return

    for kid in n.kids:
        DFS4p5(kid, dest, path, solutions)
    path.pop()
    if path == []:
        # we finished searching everything
        return best(solutions)


def DFS5(n, dest, path, solutions):
    """n: the current node
       dest: what we are searching for
       path: to the current node n
       solutions: all paths to dest
    """
    path.append(n)
    if n == dest:
        print 'I found it'
        print path
        solutions.append(path[:])

    for kid in n.kids:
        if kid not in path:
            DFS5(kid, dest, path, solutions)
    path.pop()
    if path == []:
        # we finished searching everything
        return best(solutions)

def best(solutions):
    """return the shortest solution"""
    # return min(solutions, key=len)
    if solutions == []:
        return []
    shortest_path = solutions[0]
    shortest_len = len(solutions[0])
    for solution in solutions:
        if len(solution) < shortest_len:
            shortest_len = len(solution)
            shortest_path = solution
    return shortest_path


# print best([[a,b,a],[a,b],[a,d,e,b]])

def DFS(n, dest):
    return DFS5(n, dest, [], [])

# print DFS(a, c)
# print DFS(b, e)
