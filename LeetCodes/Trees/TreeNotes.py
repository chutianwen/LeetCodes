"""
Tips:

1. Recursive programming.
Given a function "do_something(root)"
we should find a structure that explains do_something(root) = do_something(root.children)
The recursive call should be processing the sub-problem (smaller part of problem).
Ex: DiameterBinaryTree:
getDiameter(root) = getHeight(root.left) + getHeight(root.right)
Because getDiameter not equal getHeight, so this equation cannot form a recursive algorithm. The recursive call is:
getHeight(root, max_diameter) = max(getHeight(root.left, max_diameter), getHeight(root.right, max_diameter) + 1
we can use a global variable "max_diameter" to store the result during each recursive calls.
We can also transfer this structure into :
findLargestDiameter(root):
    if root is None:
        return 0
    current_diameter = getHeight(root.left) + getHeight(root.left)
    return max(current_diameter, findLargestDiameter(root.left), findLargestDiameter(root.right))
* The most important tip of recursive call is: Don't think the real execution af first, believe the function does what
it supposed to be. If human thinks the details of each steps of recursive calls, then very easy to get lost. Priority is
to find the equation of solving bigger problem by combination of smaller sub-problems.

2. Comparing left branch and right branch together:
Use two pointer method. Instead calling function like "do_something(root)", we can call "do_something(p, q)"
Just pass root.left, root.right as p, q

3. BFS on Tree:
Usually recursive calls will perform in a DFS one, so using a Queue + Iterative method to solve the problem.
Queue will always storing the parent layer of nodes.
Methods will look like:
while Q_parent is not empty:
    while Q_parent pops until empty:
        current = Q.pop
        do_something with current node
    push all the current nodes into Q_parent

4. Problem of comparing order of left part with right part,
Pre-order, in-order, post-order traverse will usually help.
"""

