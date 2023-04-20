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
        output=[]

        if k < 1:
            raise TypeError("k must be a positive integer.")
        # Case 1: Let's find the ones below in the tree.
        # For that purpose, we first need to find the number itself by using the searchit method.
        node = self.search(n)
        # We will use k in the move_down_k_positions method.
        self.k = k
        # And now that we have the element, we go through the children k times until we find the elements we desire.
        # This is the second case

        # depth_to_node, node_n = self.depth_to_node()

        self.move_down_k_positions(node,k, output)
        # To obtain more outputs, we have to climb up the tree k positions, for that we simply go down less positions
        # from the root using the searchit method.
        return output

    # Since we can only use .right and .left, we will create a parent of the node by linking it to the previous
    # element. This will allow us to track our steps easier.

    # With this search method we will move k positions down in the tree and store the last values in a DList.
    def move_down_k_positions(self, node:BinaryNode, k: int, output:list) :
        """Returns the elements k steps further down the tree."""
        if not node:
            return

        if k > 0:
            self.move_down_k_positions(node.left,k-1,output)
            self.move_down_k_positions(node.right, k-1,output)

        if k == 0:
            output.append(node.elem)
        
    def search_from_current_node(self, elem):
        return self._search_from_current_node(self.node, elem)

    def _search_from_current_node(self, node, elem):
        if node is None or node.elem == elem:
            return node
        elif elem < node.elem:
            return self._search_from_current_node(node.left, elem)
        elif elem > node.elem:
            return self._search_from_current_node(node.right, elem)

    def upwards_output(self) -> str:
        """This method adds to the output the value of the elements that are directly "k" positions above it."""
        node_n = self.search(self.n)
        n_depth = self.depth(node_n)
        desired_depth = n_depth - self.k
        if self.depth(self.node) != desired_depth:
            self.upwards_output(self.node.left)
            self.upwards_output(self.node.right)

        if self.depth(self.node) == desired_depth:
            if self.search_from_current_node(self.n) != None:
                self.output += str(self.node)
                return self.output
            if self.search_from_current_node(self.n) == None:
                return
    #
    # def _search(self, node: BinaryNode, elem: object) -> BinaryNode and str:
    #     """Recursive function"""
    #     # We will add a counter to know how many steps took us to find the number 'n'.
    #     downwards_counter = 0
    #     # We create the DList we will use to store the elements as we go down in the branches.
    #     # downwards_list = self.DList()
    #     # We store the values as part of the output.
    #     output = '['
    #
    #     for index in range(0, self.k):
    #         # We write self.k - 1 because the range goes from 0 to self.k, last not included, so self.k - 1 is the
    #         # penultimate iteration.
    #         if node.right is None and node.left is None and index != self.k - 1:
    #             return node
    #         elif elem < node.elem and index != self.k - 1:
    #             return self._search(node.left, elem)
    #         elif elem > node.elem and index != self.k - 1:
    #             return self._search(node.right, elem)
    #         # For this last iteration, we store the elements as part of the output
    #         elif index == self.k - 1:
    #             output += str(node) + ', '
    #         downwards_counter += 1
    #     return output and downwards_counter
    # #
    # def depth_to_node(self, node: BinaryNode, elem: object):
    #     #This function returns the depth at which the element "n" is.
    #     node = self._root
    #     depth_to_node = 0
    #     if node == None:
    #         # In this case the tree does not exist or does not have a root.
    #         return 0
    #     elif node.elem == elem:
    #         return depth_to_node, node
    #     elif elem < node.elem:
    #         node = node.left
    #         depth_to_node += 1
    #     elif elem > node.elem:
    #         node = node.right
    #         depth_to_node += 1
    #
    # def k_movements(self):
    #     starting_node = self.node_n
    #     #As we move in the tree, k_counter will decrease until it reaches 0.
    #     k_counter = self.k
    #     #The answers will be writen in the output.
    #     output = '['
    #     if k_counter == 0:
    #         output += self.node.elem
    #
    #     # In here we include the possibilities in which it goes down and up.
    #     if 0 < k < self.node_n.depth_to_node():
    #         # We go down in the tree k movements
    #         while k_counter > 0:
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

        include_tree(output_tree,input_tree1.root)
        difference(output_tree, input_tree1, input_tree2.root)

        return output_tree
    elif opc == "intersection":
        insert_repeated( input_tree2, output_tree, input_tree1.root)
        return output_tree


    else:   # opc== ""difference
        difference(output_tree, input_tree2, input_tree1.root)
        return output_tree

def include_tree(tree:BinarySearchTree, node:BinaryNode):
    """This function insert an entire tree in the output_tree"""
    if node:
        tree.insert(node.elem)

        include_tree(tree, node.left)

        include_tree(tree, node.right)

    return None


def difference(output_tree:BinarySearchTree, tree2:BinarySearchTree, node:BinaryNode):
    """This function insert in the output tree the elements that are not repeated in the other"""
    if node:
        if tree2.search(node.elem)==None:
            output_tree.insert(node.elem)

        difference(output_tree, tree2, node.left)

        difference(output_tree,tree2, node.right)
    return

def insert_repeated(tree2:BinarySearchTree, output_tree: BinarySearchTree, node:BinaryNode):
    """This function insert in the output tree all the elements that are in both trees"""
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
#
# input_list_01 = [18, 9, 12,4,3,2,1,50]
# input_list_02 =  [2,8,7,50, 4,13,9,11,18]
#
# # Build and draw first tree
# tree1 = BinarySearchTree()
# for x in input_list_01:
#     tree1.insert(x)
# tree1.draw()
#
# # Build and draw second tree
# tree2 = BinarySearchTree()
# for x in input_list_02:
#     tree2.insert(x)
# tree2.draw()
#
# function_names = ["merge", "intersection", "difference"]
#
#
#
#
# for op_name in function_names:
#     res = create_tree(tree1, tree2, op_name)
#     print(f"-- Result for {op_name} method. #{res.size()} nodes")
#     res.draw()

# Tried to do the first exercise using DLists, but there is a simpler approach.

