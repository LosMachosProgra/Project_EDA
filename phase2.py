"""
@author: EDA Team
"""
"""
Estéban Gómez Buitrago 
Pedro Gabriel Mantese Masegosa
"""

# Classes provided by EDA Team
from bintree import BinaryNode
from bst import BinarySearchTree


# Exercise #1
class BST2(BinarySearchTree):
    def find_dist_k(self, n: int, k: int) -> list:
        if k < 1:
            raise TypeError("k must be a positive integer.")
        # Case 1: Let's find the ones below in the tree.
        # For that purpose, we first need to find the number itself by using the searchit method.
        self.searchit(n)
        # We will use k in the move_down_k_positions method.
        self.k = k
        #And now that we have the element, we go through the children k times until we find the elements we desire.
        # This is the second case

        self.move_down_k_positions(k)
        # To obtain more outputs, we have to climb up the tree k positions, for that we simply go down less positions
        # from the root using the searchit method.



    # With this search method we will move k positions down in the tree and store the last values in a DList.
    def move_down_k_positions(self, elem: object) -> str:
        """Returns the elements k steps further down the tree."""
        return self._search(self._root, elem)

    def _search(self, node: BinaryNode, elem: object) -> BinaryNode | str:
        """Recursive function"""
        # We will add a counter to know how many steps took us to find the number 'n'.
        downwards_counter = 0
        # We create the DList we will use to store the elements as we go down in the branches.
        #downwards_list = self.DList()
        # We store the values as part of the output.
        output = '['
        for index in range(0, self.k):
            # We write self.k - 2 because the range goes from 0 to self.k - 1, both included, so self.k - 2 is the
            # penultimate iteration.
            if node.right is None and node.left is None and index != self.k - 1:
                return node
            elif elem < node.elem and index != self.k - 1:
                return self._search(node.left, elem)
            elif elem > node.elem and index != self.k - 1:
                return self._search(node.right, elem)
            # For this last iteration, we store the elements as part of the output
            elif index == self.k -1:
                output += str(node) + ', '
            downwards_counter += 1
        return output and downwards_counter









@property
def n(self) -> int:
    return self._n
# First case, when n is not an integer, or it does not exist as an element of the tree.
@n.setter
def n(self, n):
    if n != int:
        raise TypeError("'n' must be an integer")
    #If n is not in the given range, it returns an empty list.
    elif n < 0 or n > self.BinaryTree.size:
        return "[]"
    else:
        self._n = n

























# Exercise #2
def create_tree(input_tree1: BinarySearchTree, input_tree2: BinarySearchTree, opc: str) -> BinarySearchTree:
    # Here your code
    output_tree=BinarySearchTree()
    if opc=="merge":
        print("Here it starts the process of merge")
        output_tree = input_tree1
        node = input_tree2.root
        merge(output_tree.root, node)
        if node.left:
            node=node.left                              #Only missing to iterate the second tree
            merge(output_tree.root, node)



        return output_tree

    elif opc == "intersection":
        ...
    else:
        ...


def merge(compare: BinaryNode, node: BinaryNode):
    print("__", node.elem)
    if compare is None:
        return BinaryNode(node.elem)

    if compare.elem == node.elem:
        return None

    elif node.elem < compare.elem:
        compare.left = merge(compare.left, node)

    elif node.elem > compare.elem:
        compare.right = merge(compare.right, node)

    return compare
    

# Some usage examples
if __name__ == '__main__':
    # input_list_01 = [5, 1, 7, 9, 23]
    # input_list_02 = [1, 9, 11]
    input_list_01 = [5, 12, 2, 1, 3, 9]
    input_list_02 = [9, 3, 21]

    # Build and draw first tree
    tree1 = BinarySearchTree()
    for x in input_list_01:
        tree1.insert(x)
    tree1.draw()

    # Build and draw second tree
    tree2 = BinarySearchTree()
    for x in input_list_02:
        tree2.insert(x)
    tree2.draw()

    function_names = ["merge", "intersection", "difference"]

    for op_name in function_names:
        res = create_tree(tree1, tree2, op_name)
        print(f"-- Result for {op_name} method. #{res.size()} nodes")
        res.draw()































#Tried to do the first exercise using DLists, but there is a simpler approach.

"""
         #If 'n' has been correctly provided, we do the following:
        #we have to find the node 'n' inside the tree, and for that we use a modified version of the searchit method
        #from bst so that we store the values it goes through in a DList. 
        def searchit(self, elem: object) -> BinaryNode:
            #iterative function to search an elem in a BST. It
            #returns the node that contains this elem.
            #node = self._root
            # We use a DList to store the values as we go down the tree to later find more elements in superior branches
            # This way we can go back without having to use the parent attribute.
            backwards_list = self.DList()
            new_head = self.DNode(self.root)
            new_head = self.backwards_list.head

            while node:
                if node.elem == elem:
                    # we have found it!!! we can return it and leave the function
                    return node

                if elem < node.elem:
                    node = node.left
                else:
                    node = node.right
            return node
        self.searchit(n)
        """
