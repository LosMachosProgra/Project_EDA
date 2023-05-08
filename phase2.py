"""
@author: Esteban Gómez Buitrago
@author: Pedro Gabriel Mantese Masegosa
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
        self.node = self.search(n)
        # We will use k in the move_down_k_positions method.
        self.k = k

        if self.node==self.root:
            self.move_down_k_positions(self.node,k)
        else:
            self.depth_node = self.depth(self.node)
            self.desired_depth = self.depth_node - self.k
            self.upwards_output(self.root, 0, 0 > self.desired_depth, False)

        return self.output

    def upwards_output(self, node_It: BinaryNode, depth_It: int, in_range:bool, check_root):
        if node_It:
            next_depth= (depth_It + 1 > self.desired_depth) and (depth_It + 1 < self.depth_node)
            if node_It.right:
                n_in_the_right = self._search(node_It.right, self.node.elem)
            else:
                n_in_the_right = False

            print(in_range)

            if not check_root:
                if in_range:
                    print("root in range")
                    if not n_in_the_right:
                        print("node in the left, so we go {} right".format(self.k - self.depth_node))
                        self.move_down_k_positions(node_It.right, self.k - self.depth_node-1)
                        self.upwards_output(node_It.left, depth_It + 1, next_depth, True)
                    elif n_in_the_right:
                        print("node in the rigth, so we go {} left".format(self.k - self.depth_node))
                        self.move_down_k_positions(node_It.left, self.k - self.depth_node-1)
                        self.upwards_output(node_It.right, depth_It + 1, next_depth, True)
                else:
                    print("root NOT in range")
                    if depth_It==self.desired_depth:
                        self.output.append(node_It.elem)
                    if not n_in_the_right:
                        self.upwards_output(node_It.left, depth_It + 1, next_depth, True)
                    if n_in_the_right:
                        self.upwards_output(node_It.right, depth_It + 1, next_depth, True)

            if in_range and check_root:
                if n_in_the_right:
                    print("lado derecho")
                    self.move_down_k_positions(node_It.left, self.k - self.depth_node)
                    self.upwards_output(node_It.right, depth_It + 1 , next_depth,True)
                elif not n_in_the_right:
                    print("lado izquierdo")
                    self.move_down_k_positions(node_It.right, self.k - self.depth_node )
                    self.upwards_output(node_It.left, depth_It + 1, next_depth,True)

            if not in_range and check_root:
                if depth_It < self.desired_depth:
                    print("acercandose")
                    self.upwards_output(node_It.left, depth_It + 1, next_depth,True )
                    self.upwards_output(node_It.right, depth_It + 1, next_depth,True)
                if depth_It == self.desired_depth:
                    print("print, desired depth", node_It.elem)
                    self.output.append(node_It.elem)
                    self.upwards_output(node_It.left, depth_It + 1, next_depth,True)
                    self.upwards_output(node_It.right, depth_It + 1, next_depth,True)
                if node_It==self.node:
                    print("abajo")
                    self.move_down_k_positions(self.node, self.k)

            print("end")

        # With this search method we will move k positions down in the tree and store the last values in a DList.
    def move_down_k_positions(self, node: BinaryNode, k: int):
        """Returns the elements k steps further down the tree."""
        if not node:
            print("nada")
            return

        if k > 0:
            self.move_down_k_positions(node.left, k - 1)
            self.move_down_k_positions(node.right, k - 1)

        if k == 0:
            print("print", node.elem)
            self.output.append(node.elem)


# Some usage examples
if __name__ == '__main__':
    input_list_01 = [5, 2, 3, 1, 7, 9, 6, 23, 30, 4, 8, 10, 24, 22, 19, 11]

    # Build and draw first tree
    tree1 = BST2()
    for x in input_list_01:
        tree1.insert(x)
    tree1.draw()
    print(tree1.find_dist_k(8, 4))


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

# Tried to do the first exercise using DLists, but there is a simpler approach.
