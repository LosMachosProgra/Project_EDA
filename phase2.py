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






# Exercise #2

@property
def opc(self) -> str:
    return self._n


# First case, when n is not an integer, or it does not exist as an element of the tree.
@opc.setter
def opc(self, opc):
    if opc != "merge" and opc != "intersection" and opc != "difference":
        raise TypeError("'n' must be merge, intersection, or difference")
    else:
        self._opc = opc


def create_tree(input_tree1: BinarySearchTree, input_tree2: BinarySearchTree, opc: str) -> BinarySearchTree:
    # Here your code
    output_tree=BinarySearchTree()
    if opc == "merge":
        print("Here it starts the process of merge")

        include_tree(output_tree,input_tree1.root)

        difference(output_tree, output_tree.root, input_tree2.root)

        return output_tree

    elif opc == "intersection":
        print("Here it starts the process of intersection")
        insert_repeated( input_tree2, output_tree, input_tree1.root)
        return output_tree


    else:   # opc== ""difference
        print("Here it starts the process of difference")
        insert_not_repeated(input_tree2, output_tree,input_tree1.root)
        return output_tree

def include_tree(tree:BinarySearchTree, node:BinaryNode):
    if node:
        tree.insert(node.elem)

        include_tree(tree, node.left)

        include_tree(tree, node.right)

    return None


def difference(tree: BinarySearchTree, node_tree1: BinaryNode, node_tree2: BinaryNode):
    if node_tree2:

        if tree.search(node_tree2.elem) == None:
            tree.insert(node_tree2.elem)

        difference(tree, node_tree1, node_tree2.left)
        difference(tree, node_tree1, node_tree2.right)

    return    #It is reduntant, but we put it for better understanding


def insert_not_repeated(tree2:BinarySearchTree, output_tree:BinarySearchTree,node:BinaryNode):
    if node:
        if tree2.search(node.elem)==None:
            output_tree.insert(node.elem)

        insert_not_repeated(tree2,output_tree, node.left)

        insert_not_repeated(tree2, output_tree, node.right)
    return

def insert_repeated(tree2:BinarySearchTree, output_tree: BinarySearchTree, node:BinaryNode):
    if node:
        if tree2.search(node.elem):
            output_tree.insert(node.elem)
        insert_repeated( tree2, output_tree, node.left)
        insert_repeated( tree2, output_tree, node.right)
    return



# Some usage examples
    #if __name__ == '__main__':
# input_list_01 = [5, 1, 7, 9, 23]
# input_list_02 = [1, 9, 11]

input_list_01 = [18, 9, 12,4,3,2,1,50]
input_list_02 =  [2,8,7,50, 4,13,9,11,18]

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

res = create_tree(tree1, tree2, "difference")
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
