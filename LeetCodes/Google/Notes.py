"""
Python closure, 'a' in below as to be a reference type of variable, otherwise, error as "reference before assignment"
shows up.
"""
def fun():
    '''
    a is good here
    :return:
    '''
    a = [4]
    def funny():
        a[0] = 2
        print(a)
    funny()
    print(a)
fun()

def fun():
    '''
    a is good here
    :return:
    '''
    a = [4]
    def funny():
        a[0] += 2
        print(a)
    funny()
    print(a)
fun()

def fun():
    '''
    a cannot be referenced
    :return:
    '''
    a = 4
    def funny():
        global a
        print(a)
        a += 2
        # print(a)
    funny()
    print(a)
# fun()

class NODE:
    def __init__(self):
        self.visited = False
        self.neighbors = None

from queue import deque
def bfs(nodes, target):
    '''

    :param nodes: list[NODE]
    :return:
    '''
    q = deque([nodes[0]])
    while q:
        cur_node = q.popleft()
        for node in cur_node.neighbors:
            if not node.visited:
                if node == target:
                    return True
                q.append(node)
                node.visited = True

def dfs(nodes, target):
    '''

    :param nodes: list[NODE]
    :param target:
    :return:
    '''
    stack = []
    start = nodes[0]
    while start or stack:
        if start:
            stack.append(start)
            for node in start.neighbors:
                if not node.visited:
                    if node == target:
                        return True
                    stack.append(node)
                    start = node
                    break

        else:
            start = stack.pop()

'''
Priority queue, heapq
'''
import heapq
a = []
heapq.heappush(a, 4)
heapq.heappush(a, -1)
heapq.heappush(a, 5)
min = heapq.heappop(a)

listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)

a = 1
def fun4():
    print(a)
fun4()

def fun5():
    global a
    a += 1
    print(a)
fun5()