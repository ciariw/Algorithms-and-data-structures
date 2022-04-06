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
            pairs.append(Heap.Node(i[0], i[1]))
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
        tempnode = Heap.Node(node.problem, node.priority)
        # Copy all attributes ove to tempnode
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

    def heapify(self):
        last_internal_node = int((len(self.pairs) - 2) / self.d)
        for i in reversed(range(last_internal_node + 1)):
            self.push_down(self.pairs, i, self.pairs[i])
            print([x.index for x in self.pairs], [x.priority for x in self.pairs],
                  [f"{x.priority}:{[self.pairs[j].priority for j in x.child]}" for x in self.pairs])


if __name__ == '__main__':
    a = Heap(2, ("forment unrest", 1), ("Kill neighbors", -7), ("Test school speed limit", 9),
             ("Kill trees for paper", 1), ("sell a best seller", 10), ("apples", 11), ("oranges", 48),
             ("trees", -2), ("homies", 62))
    a.heapify()
