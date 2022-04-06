# This is my attempt at making a heap data structure
import time


class Heap:
    class Node:
        def __init__(self, problem, priority):
            self.problem = problem
            self.priority = priority
            self.child = []
            self.index = 0
            self.level = None
            self.parent = None

    def __init__(self, tree_width=2, *args):
        pairs = []
        self.object_mapper = {}
        for index, i in enumerate(args):
            # go through the args and assign relationships based on the index of pairs
            pairs.append(self.Node(i[0], i[1]))
            pairs[index].index = index
            self.object_mapper[i[0]] = pairs[index]
            if len(pairs) > 1:
                # Set parent index, set current index as child node of parent
                pairs[index].parent = int((index - 1) / tree_width)
                pairs[int((index - 1) / tree_width)].child.append(index)
        self.pairs = pairs
        self.d = tree_width

    def push_down(self, pairs=None, index=None, node=None):
        d = self.d
        # Create a temporary node
        tempnode = self.Node(node.problem, node.priority)
        # Copy all attributes over to tempnode
        tempnode.__dict__.update(node.__dict__)
        first_leaf_index = int((len(pairs) - 2) / d) + 1

        while 0 <= index < first_leaf_index:
            bc_priority = max([(pairs[x].priority, x) for x in pairs[index].child])

            # Select biggest child
            # compare with biggest child
            # if smaller than biggest child, swap positions and child locations

            if bc_priority[0] > tempnode.priority:
                pairs[index].__dict__["problem"] = pairs[bc_priority[1]].problem
                pairs[index].__dict__["priority"] = bc_priority[0]
                index = int(bc_priority[1])
                tempnode.child = list(pairs[index].child)
                tempnode.index = index
                pairs[index].child = tempnode.child

            else:
                break

        pairs[index] = tempnode
        self.pairs = pairs

    def bubble_up(self,node=None,index=None):
        # copy the values of the node to be pasted later at the correct index
        values = dict(node.__dict__)
        # If the index isnt selected, we just need the node object
        if not index:
            i = int(node.index)
        else:
            i = int(index)
        # pairs definition so i dont have to type self. all the time
        pairs = self.pairs

        while i > 0:

            parent_node_index = int((i - 1) / self.d)
            if values["priority"] >= pairs[parent_node_index].priority:
                pairs[i].__dict__["priority"] = pairs[parent_node_index].__dict__["priority"]
                pairs[i].__dict__["problem"] = pairs[parent_node_index].__dict__["problem"]
                i = parent_node_index
            else:
                pairs[i].__dict__["priority"] = values["priority"]
                pairs[i].__dict__["problem"] = values["problem"]
                break
            if i == 0:
                pairs[i].__dict__["priority"] = values["priority"]
                pairs[i].__dict__["problem"] = values["problem"]

        # save changes
        self.pairs = pairs

    def heapify(self):
        last_internal_node = int((len(self.pairs) - 2) / self.d)
        for i in reversed(range(last_internal_node + 1)):
            self.push_down(self.pairs, i, self.pairs[i])

    def add(self, *args):
        for i in args:
            index = len(self.pairs)
            self.pairs.append(self.Node(i[0], i[1]))
            self.pairs[index].index = index
            self.object_mapper[i[0]] = self.pairs[index]
            # Set parent index, set current index as child node of parent
            self.pairs[index].parent = int((index - 1) / self.d)
            self.pairs[int((index - 1) / index)].child.append(index)
            self.bubble_up(self.pairs[index])

if __name__ == '__main__':
    a = Heap(2, ("forment unrest", 1), ("Kill neighbors", -7), ("Test school speed limit", 9),
             ("Kill trees for paper", 1), ("sell a best seller", 10), ("apples", 11), ("oranges", 48),
             ("trees", -2), ("homies", 62))
    a.heapify()
    a.add(("homies", 629),("homies", 29),("homies", -629))

    '''
    Pretty cool check for all items in the priority queue put in order of index
    I thought I would have to do something about the duplicate problems.
    print("| -> |".join([f"{x.priority} : {x.index}" for x in a.pairs]))
    print([(j.index,j.priority, j.problem) for j in a.object_mapper.values()])'''
    print("| -> |".join([f"{x.priority} : {x.index}" for x in a.pairs]))
