class Disjoint():
    def __init__(self):
        self.sets = []
        self.nodes = {}

    def make_set(self, vertex):
        new_node = Node(vertex, None)
        self.sets.append(new_node)
        self.nodes[vertex] = new_node

    def find_set(self, vertex):
        node = self.nodes[vertex]
        if node.parent != None:
            node.parent = self.find_set(node.parent.data)

        return node

    def union(self, vertex1, vertex2):
        parent1 = self.find_set(vertex1)
        parent2 = self.find_set(vertex2)

        if parent1 == parent2:
            return False
        else:
            if parent1.rank == parent2.rank:
                parent1.parent = parent2
                parent2.rank += 1
            elif parent1.rank > parent2.rank:
                parent2.parent = parent1
            else:
                parent1.parent = parent2
            return True
        
class Node():

    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.rank = 0