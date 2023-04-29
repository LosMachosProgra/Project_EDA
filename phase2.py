"""
@author: EDA Team
"""
"""
Estéban Gómez Buitrago 
Pedro Gabriel Mantese Masegosa
"""
from bintree import BinaryNode
from bst import BinarySearchTree


# Exercise #1

class BST2(BinarySearchTree):

    def find_dist_k(self, n: int, k: int) -> list:
        self.output = []

        if k < 1:
            raise TypeError("k must be a positive integer.")
        # Case 1: Let's find the ones below in the tree.
        # For that purpose, we first need to find the number itself by using the searchit method.
        node = self.search(n)
        # We will use k in the move_down_k_positions method.
        self.k = k
        # And now that we have the element, we go through the children k times until we find the elements we desire.
        # This is the second case
        # This variable is to know if n is in the left part of the tree or the right part and search elements in
        # consecuence.
        self.n_in_the_right = self._search(self.root.right, node.elem)

        # depth_to_node, node_n = self.depth_to_node()

        self.move_down_k_positions(node, k)
        # To obtain more outputs, we have to climb up the tree k positions, for that we simply go down less positions
        # from the root using the searchit method.

        self.depth_node = self.depth(node)
        self.upwards_output(self.root, node, 0)
        self.intermediate_elements(node)

        return self.output

    # Since we can only use .right and .left, we will create a parent of the node by linking it to the previous
    # element. This will allow us to track our steps easier.

    # With this search method we will move k positions down in the tree and store the last values in a DList.
    def move_down_k_positions(self, node: BinaryNode, k: int):
        """Returns the elements k steps further down the tree."""
        if not node:
            return

        if k > 0:
            self.move_down_k_positions(node.left, k - 1)
            self.move_down_k_positions(node.right, k - 1)

        if k == 0:
            self.output.append(node.elem)

    def upwards_output(self, node_It: BinaryNode, node: BinaryNode, depth_It: int) -> list:
        """This method adds to the output the value of the elements that are directly "k" positions above it."""

        if node_It:
            desired_depth = self.depth_node - self.k
            # Desired_depth is positive
            if depth_It < desired_depth:
                self.upwards_output(node_It.left, node, depth_It + 1)

                self.upwards_output(node_It.right, node, depth_It + 1)

            if depth_It == desired_depth:
                if self._search(node_It, node.elem) != None:
                    self.output.append(node_It.elem)
                self.upwards_output(node_It.left, node, depth_It + 1)
                self.upwards_output(node_It.right, node, depth_It + 1)

            # In this case, we go through the other side of the tree, passing through the root
            # (desired_depth is negative)
            if depth_It > desired_depth:
                remaining_movements = abs(desired_depth)

                if self.n_in_the_right != None:
                    # We substact 1 from remaining_movements because we start the process from the child of the root,
                    # Thus, using one of the movements we had left.
                    self.move_down_k_positions(self.root.left, remaining_movements - 1)
                elif self.n_in_the_right == None:
                    self.move_down_k_positions(self.root.right, remaining_movements - 1)

    def intermediate_elements(self, node: BinaryNode):
        # This variable will be used when calculating the elements that appear when going up from n and afterwards down.
        intermediate_movements = self.k - self.depth_node

        # This case appears when we have no moves to go through an alternative path.
        # if intermediate_movements < 1:
        if self.n_in_the_right == None:
            self._intermediate_elements(self.root.left, node, intermediate_movements)
        elif self.n_in_the_right != None:
            self._intermediate_elements(self.root.right, node, intermediate_movements)

    # else: #intermediate-movements >= 1
    #   self.intermediate_elements(node)

    def _intermediate_elements(self, node_It, node: BinaryNode, intermediate_movements):
        """This method finds the elements that appear going up from the element n and down again, in the same side of
        the tree."""
        if node_It.elem == node.elem:
            return None
        elif intermediate_movements < 1:
            self._intermediate_elements(node_It.left, node, intermediate_movements + 1)
            self._intermediate_elements(node_It.right, node, intermediate_movements + 1)
        elif self._search(node_It, node) != None:
            # We add one to the movements available because we are getting closer to n.
            intermediate_movements += 1
            self._intermediate_elements(node_It.right, node, intermediate_movements + 1)
            self._intermediate_elements(node_It.left, node, intermediate_movements + 1)
        else: # self._search(node_It, node) == None
            intermediate_movements -= 1
            if intermediate_movements == 0:
                self.output.append(node.elem)
            else: # intermediate_movements != 0
                self._intermediate_elements(node_It.right, node, intermediate_movements - 1)
                self._intermediate_elements(node_It.left, node, intermediate_movements - 1)





















                """n_is_below = self._search(self.root.right, node.elem)
                if n_is_below == None:
                    # We use "desired_depth - 1" because we are analyzing what happens departing from the child of the
                    # root. If we started from te root, we would be using "desired_depth".
                    self.move_down_k_positions(self.root.left, abs(desired_depth))

                if n_is_below != None:
                    self.move_down_k_positions(self.root.right, abs(desired_depth))


                self.move_down_k_positions(node_It, abs(depth_It - self.depth_node))"""

        if node_It == node:
            return self.output


# Some usage examples
if __name__ == '__main__':
    input_list_01 = [5, 2, 3, 1, 7, 9, 6, 23, 30, 4, 8]

    # Build and draw first tree
    tree1 = BST2()
    for x in input_list_01:
        tree1.insert(x)
    tree1.draw()
    print(tree1.find_dist_k(2, 3))


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
    output_tree = BinarySearchTree()
    if opc == "merge":

        include_tree(output_tree, input_tree1.root)
        difference(output_tree, input_tree1, input_tree2.root)

        return output_tree
    elif opc == "intersection":
        insert_repeated(input_tree2, output_tree, input_tree1.root)
        return output_tree


    else:  # opc== ""difference
        difference(output_tree, input_tree2, input_tree1.root)
        return output_tree


def include_tree(tree: BinarySearchTree, node: BinaryNode):
    """This function insert an entire tree in the output_tree"""
    if node:
        tree.insert(node.elem)

        include_tree(tree, node.left)

        include_tree(tree, node.right)

    return None


def difference(output_tree: BinarySearchTree, tree2: BinarySearchTree, node: BinaryNode):
    """This function insert in the output tree the elements that are not repeated in the other"""
    if node:
        if tree2.search(node.elem) == None:
            output_tree.insert(node.elem)

        difference(output_tree, tree2, node.left)

        difference(output_tree, tree2, node.right)
    return


def insert_repeated(tree2: BinarySearchTree, output_tree: BinarySearchTree, node: BinaryNode):
    """This function insert in the output tree all the elements that are in both trees"""
    if node:
        if tree2.search(node.elem):
            output_tree.insert(node.elem)
        insert_repeated(tree2, output_tree, node.left)
        insert_repeated(tree2, output_tree, node.right)
    return

# Some usage examples
# if __name__ == '__main__':
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
