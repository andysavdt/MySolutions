'''
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:

1   2   4
 \ /   / \
  3   5   8
   \ / \   \
    6   7   10


parentChildPairs = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (8, 10)
]

Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

Sample input and output:

hasCommonAncestor(parentChildPairs, 3, 8) => false
hasCommonAncestor(parentChildPairs, 5, 8) => true
hasCommonAncestor(parentChildPairs, 6, 8) => true
hasCommonAncestor(parentChildPairs, 1, 3) => false

'''


parent_child_pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (8, 10)
]

def findNodesWithZeroAndOneParents(parentChildPairs):
    total_parents = {}
    for pair in parentChildPairs:
        if pair[1] in total_parents:
            total_parents[pair[1]] += 1
        else:
            total_parents[pair[1]] = 1

        if pair[0] not in total_parents:
            total_parents[pair[0]] = 0

    zero_parent = []
    single_parent = []
    for member in total_parents:
        if total_parents[member] == 0:
            zero_parent.append(member)
        if total_parents[member] == 1:
            single_parent.append(member)
    return (zero_parent, single_parent)

def hasCommonAncestor(parentChildPairs, member1, member2):
    print member1
    print member2
    anscestor1 = {}
    ans1 = ancestors(parentChildPairs,member1)
    ans2 = ancestors(parentChildPairs,member2)
    for member in ans1 :
        if member not in anscestor1:
            anscestor1[member] = True
    for i in range(len(ans2)):
        if ans2 in anscestor1:
            return True
    '''for i in range(len(ans1)):
        for j in range(len(ans2)):
            if ans1[i] == ans2[j]:
                return True'''
    return False



def ancestors(parentChildPairs,member):
    ans = []
    to_check = []
    check = None
    to_check.insert(0,member)
    while len(to_check)>0:
        check = to_check[0]
        to_check.pop()
        for members in parentChildPairs:
            if members[1] == check:
                ans.append(members[0])
                to_check.insert(0,members[0])
    return ans

print hasCommonAncestor(parent_child_pairs, 1, 3)

#


#print  findNodesWithZeroAndOneParents(parent_child_pairs)
