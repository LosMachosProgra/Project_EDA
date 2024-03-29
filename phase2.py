"""
@author: Esteban Gómez Buitrago
@author: Pedro Gabriel Mantese Masegosa
"""

# Classes provided by EDA Team
from bintree import BinaryNode
from bst import BinarySearchTree


# Exercise #1


class BST2(BinarySearchTree):

    def find_dist_k(self, n: int, k: int) -> list:
        # The desired elements will be added to this list.
        self.output = []

        if k < 1:
            raise TypeError("k must be a positive integer.")
        # We first need to find the number itself by using the searchit method.
        self.node = self.search(n)
        # We will use k in the move_down_k_positions method.
        self.k = k

        if self.node == self.root:
            self.move_down_k_positions(self.node,k)
        else:
            self.depth_node = self.depth(self.node)
            self.desired_depth = self.depth_node - self.k
            self.upwards_output(self.root, 0, 0 > self.desired_depth)

        return self.output

    def upwards_output(self, node_It: BinaryNode, depth_It: int, in_range:bool):
        """This method returns the desired elements directly above n, the ones obtained by going up and down in the 
        tree, and the ones k number of positions down in the tree, if they exist."""
        if node_It:
            # Next_depth tells us if we are in the interval to analyze elements we geet by going up and down in the tree
            next_depth = (depth_It + 1 > self.desired_depth) and (depth_It + 1 < self.depth_node)
            if node_It.right:
                # This variable confirms us which way to go in the branch.
                n_in_the_right = self._search(node_It.right, self.node.elem)
            else:
                n_in_the_right = False
            if in_range:
                # We move in the opposite direction to n in order to find the up and down elements
                if n_in_the_right:
                    self.move_down_k_positions(node_It.left, self.k - 1 -(self.depth_node - depth_It))
                    self.upwards_output(node_It.right, depth_It + 1 , next_depth)
                elif not n_in_the_right:
                    self.move_down_k_positions(node_It.right, self.k - 1 - (self.depth_node - depth_It))
                    self.upwards_output(node_It.left, depth_It + 1, next_depth)

            if not in_range:
                if depth_It == self.desired_depth:
                    self.output.append(node_It.elem)
                if n_in_the_right:
                    self.upwards_output(node_It.right, depth_It + 1, next_depth)
                if not n_in_the_right:
                    self.upwards_output(node_It.left, depth_It + 1, next_depth,)

            if node_It == self.node:
                self.move_down_k_positions(self.node, self.k)

        #
    def move_down_k_positions(self, node: BinaryNode, k: int):
        """Returns the elements k steps further down the tree."""
        if not node:
            return

        if k > 0:
            self.move_down_k_positions(node.left, k - 1)
            self.move_down_k_positions(node.right, k - 1)

        if k == 0:
            self.output.append(node.elem)

if __name__ == '__main__':
    input_list_01 = [20, 10, 30, 15, 26, 25, 35, 5, 4, 6, 2, 3, 1, 8, 7, 9, 13, 12, 17, 16, 19, 21, 24, 23, 18, 27, 29,
                     32, 33, 31, 34, 38, 36, 37, 39, 40]

    # Build and draw first tree
    tree1 = BST2()
    for x in input_list_01:
        tree1.insert(x)
    tree1.draw()
    print(tree1.find_dist_k(20, 4))

@property
def n(self):
    return self.__n

@n.setter
def n(self, n: int):
    if type(n) != int:
        TypeError("n must be an integer.")
    elif self._search(self.root, n) is None:
        ValueError("n must be an element of the tree.")

@property
def k(self):
    return self.k

@k.setter
def k(self, k: int):
    if type(k) != int:
        TypeError("k must be an integer.")



# # Some usage examples
# if __name__ == '__main__':
#     input_list_01 = [5, 2, 3, 1, 7, 9, 6, 23, 30, 4, 8, 10, 24, 22, 19, 11]
#
#     # Build and draw first tree
#     tree1 = BST2()
#     for x in input_list_01:
#         tree1.insert(x)
#     tree1.draw()
#     print(tree1.find_dist_k(5, 3))


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
        if tree2.search(node.elem) is None:
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
