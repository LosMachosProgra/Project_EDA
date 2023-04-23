"""
@author: EDA Team
"""
"""
Estéban Gómez Buitrago 
Pedro Gabriel Mantese Masegosa
"""

from bintree import BinaryNode
from bst import BinarySearchTree


class BST2(BinarySearchTree):

    def find_dist_k(self, n: int, k: int) -> list:
        output = []

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

        self.move_down_k_positions(node, k, output)
        # To obtain more outputs, we have to climb up the tree k positions, for that we simply go down less positions
        # from the root using the searchit method.

        depth= self.depth(node)
        self.upwards_output(self.root, node, output, 0, depth)


        return output


    # Since we can only use .right and .left, we will create a parent of the node by linking it to the previous
    # element. This will allow us to track our steps easier.

    # With this search method we will move k positions down in the tree and store the last values in a DList.
    def move_down_k_positions(self, node: BinaryNode, k: int, output: list):
        """Returns the elements k steps further down the tree."""
        if not node:
            return
        if k > 0:
            self.move_down_k_positions(node.left, k - 1, output)
            self.move_down_k_positions(node.right, k - 1, output)

        if k == 0:
            output.append(node.elem)


    def _search_from_current_node(self, node:BinaryNode, elem:object):
        if node is None or node.elem == elem:
            return node
        elif elem < node.elem:
            return self._search_from_current_node(node.left, elem)
        elif elem > node.elem:
            return self._search_from_current_node(node.right, elem)


    def upwards_output(self,node_It:BinaryNode, node:BinaryNode, output:list, depth_It: int, depth_node: int ) -> list:
        """This method adds to the output the value of the elements that are directly "k" positions above it."""
        if node_It:
            desired_depth = depth_node - self.k
            if depth_It < desired_depth:
                self.upwards_output(node_It.left, node, output, depth_It + 1, depth_node)

                self.upwards_output(node_It.right, node,output,depth_It + 1, depth_node)

            if depth_It == desired_depth:
                if self._search_from_current_node(node_It, node.elem) != None:
                    output.append(node_It.elem)
                    self.upwards_output(node_It.left, node, output, depth_It + 1, depth_node)
                    self.upwards_output(node_It.right, node, output, depth_It + 1, depth_node)

            #It is adding the elements that are in the same line that the one from were we start
           # if depth_It > desired_depth and depth_It != depth_node:
            #    if self._search_from_current_node(node_It, node.elem) != None:
             #       self.move_down_k_positions(node_It,depth_It, output)

            if node_It== node:
                return output
            


#Some usage examples
if __name__ == '__main__':
    input_list_01 = [5, 2,3, 1, 7, 9, 6, 23]

    # Build and draw first tree
    tree1 = BST2()
    for x in input_list_01:
        tree1.insert(x)
    tree1.draw()
    print(tree1.find_dist_k(7,2))



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

