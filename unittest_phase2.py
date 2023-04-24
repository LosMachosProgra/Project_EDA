
# Classes provided by EDA Team
from phase2 import create_tree
from phase2 import BST2
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.input1= BST2()
        self.input2 = BST2()
        self.expected1= []
        self.expected2= BST2()
    #Exercise 1

    def test_for_not_at_distance(self):
        input_list_01 = [1, 2, 3, 4, 5]
        for x in input_list_01:
            self.input1.insert(x)
        for x in []:
            self.expected1.append(x)

        self.assertEqual(self.expected1 ,self.input1.find_dist_k(3,4))

    def test_for_only_down(self):
        input_list_01 = [5,3,2,4,6]
        for x in input_list_01:
            self.input1.insert(x)
        for x in [3,6]:
            self.expected1.append(x)

        self.assertEqual(self.expected1 ,self.input1.find_dist_k(5,1))

    def test_for_only_up(self):
        input_list_01 = [1,2,3,4]
        for x in input_list_01:
            self.input1.insert(x)
        for x in [2]:
            self.expected1.append(x)

        self.assertEqual(self.expected1 ,self.input1.find_dist_k(4,2))

    def test_for_only_up_and_down(self):
        input_list_01 = [1, 2, 3, 4, 5]
        for x in input_list_01:
            self.input1.insert(x)
        for x in [5,1]:
            self.expected1.append(x)

        self.assertEqual(self.expected1, self.input1.find_dist_k(3, 2))

    #Exercise 2
    #Tests for merge

    def test_for_same_amount_of_element(self):
        #This method checks if merge works for the same number of elements (merge)

        input_list_01 = [1, 2, 3, 4, 9, 12, 18, 50, 55]
        input_list_02 = [2, 4, 7, 8, 9, 11, 13, 18, 50]

        for x in input_list_01:
            self.input1.insert(x)

        for x in input_list_02:
            self.input2.insert(x)
        for x in [1,2,3,4,9,12,18,50,55,7,8,11,13]:
            self.expected2.insert(x)

        self.assertEqual(self.expected2.inorder_list() ,create_tree(self.input1, self.input2, "merge").inorder_list())

    def test_for_repeated_root(self):
        #This method checks if merge works for two trees were the root of one tree is repeated in the other (merge)

        input_list_01 = [1, 2, 3, 4, 9, 12, 18, 50, 55]
        input_list_02 = [1, 2, 4, 7, 8, 9, 11, 13, 18, 50]

        for x in input_list_01:
            self.input1.insert(x)

        for x in input_list_02:
            self.input2.insert(x)

        for x in [1,2,3,4,9,12,18,50,55,7,8,11,13]:
            self.expected2.insert(x)

        self.assertEqual(self.expected2.inorder_list() ,create_tree(self.input1, self.input2, "merge").inorder_list())

    def test_equal_trees(self):
        #This method checks if merge works for equal trees (merge)
        input_list_01 = [1, 2, 3, 4]
        input_list_02 = [1, 2, 3, 4]

        for x in input_list_01:
            self.input1.insert(x)

        for x in input_list_02:
            self.input2.insert(x)

        for x in [1,2,3,4]:
            self.expected2.insert(x)

        self.assertEqual(self.expected2.inorder_list() ,create_tree(self.input1, self.input2, "merge").inorder_list())

    def test_not_equal_elements(self):
        #Here we're checking if it works when we don't have equal elements (merge)
        input_list_01 = [1, 2, 3, 4]
        input_list_02 = [5, 6, 7]

        for x in input_list_01:
            self.input1.insert(x)

        for x in input_list_02:
            self.input2.insert(x)

        for x in [1, 2, 3, 4, 5, 6, 7]:
            self.expected2.insert(x)

        self.assertEqual(self.expected2.inorder_list(), create_tree(self.input1, self.input2, "merge").inorder_list())

    #For intersection

    def test_for_not_repeated_elements(self):
        #This method checks if intersection works for two trees with no repeated elements (intersection)

        input_list_01 = [1, 2, 3, 4, 5, 6]
        input_list_02 = [7, 8, 9, 10]

        for x in input_list_01:
            self.input1.insert(x)

        for x in input_list_02:
            self.input2.insert(x)

        for x in []:
            self.expected2.insert(x)

        self.assertEqual(self.expected2.inorder_list() ,create_tree(self.input1, self.input2,
                                                                   "intersection").inorder_list())

    def test_for_all_repeated(self):
        #This method checks if intersection works for two trees with the same elements (intersection)

        input_list_01 = [1, 2, 3, 4]
        input_list_02 = [1, 2, 3, 4]

        for x in input_list_01:
            self.input1.insert(x)

        for x in input_list_02:
            self.input2.insert(x)

        for x in [1,2,3,4]:
            self.expected2.insert(x)

        self.assertEqual(self.expected2.inorder_list() ,create_tree(self.input1, self.input2, "merge").inorder_list())

    def test_for_different_sizes(self):
        #This method checks if intersection works for trees of different size (intersection)
        input_list_01 = [1, 2, 3, 4, 5]
        input_list_02 = [3, 4, 5, 6, 7, 8, 9, 10]

        for x in input_list_01:
            self.input1.insert(x)

        for x in input_list_02:
            self.input2.insert(x)

        for x in [3, 4, 5]:
            self.expected2.insert(x)

        self.assertEqual(self.expected2.inorder_list() ,create_tree(self.input1, self.input2,
                                                                   "intersection").inorder_list())

    def test_1_repeated_elem(self):
        #Test for the case in which we have only one repeated element
        input_list_01 = [1, 2, 3, 4, 8, 6, 5]
        input_list_02 = [1, 15, 20, 22, 25]

        for x in input_list_01:
            self.input1.insert(x)

        for x in input_list_02:
            self.input2.insert(x)

        for x in [1]:
            self.expected2.insert(x)

        self.assertEqual(self.expected2.inorder_list(), create_tree(self.input1, self.input2,
                                                                   "intersection").inorder_list())


    def test_same_root(self):
        #Test for two trees with the same root (intersection)
        input_list_01 = [1, 2, 3, 4, 8, 6, 5]
        input_list_02 = [1, 5, 8, 6, 7, 10]

        for x in input_list_01:
            self.input1.insert(x)

        for x in input_list_02:
            self.input2.insert(x)

        for x in [1, 5, 8, 6]:
            self.expected2.insert(x)

        self.assertEqual(self.expected2.inorder_list(), create_tree(self.input1, self.input2,
                                                                   "intersection").inorder_list())

    #For difference

    def test_for_not_all_dist_elements(self):
        # This method checks if difference works for two trees with all different elements (difference)

        input_list_01 = [1, 2, 3, 4, 5, 6]
        input_list_02 = [7, 8, 9, 10]

        for x in input_list_01:
            self.input1.insert(x)

        for x in input_list_02:
            self.input2.insert(x)

        for x in [1, 2, 3, 4, 5, 6]:
            self.expected2.insert(x)

        self.assertEqual(self.expected2.inorder_list(), create_tree(self.input1, self.input2,
                                                                   "difference").inorder_list())

    def test_for_elems_repeated_in_tree2(self):
        # This method checks if difference works for two trees where all the elements are in the second tree (difference)

        input_list_01 = [1, 5, 8, 10, 15 ,14 ]
        input_list_02 = [12, 1, 2, 3, 4, 5, 8, 10, 15 ,14]

        for x in input_list_01:
            self.input1.insert(x)

        for x in input_list_02:
            self.input2.insert(x)

        for x in []:
            self.expected2.insert(x)

        self.assertEqual(self.expected2.inorder_list(),
                         create_tree(self.input1, self.input2, "difference").inorder_list())

    def test_for_some_repeated(self):
        # This method checks if difference works with one tree that have some elements repeated on the second (difference)
        input_list_01 = [1, 2, 3, 4, 5]
        input_list_02 = [3, 4, 5, 6, 7, 8, 9, 10]

        for x in input_list_01:
            self.input1.insert(x)

        for x in input_list_02:
            self.input2.insert(x)

        for x in [1, 2]:
            self.expected2.insert(x)

        self.assertEqual(self.expected2.inorder_list(), create_tree(self.input1, self.input2,
                                                                   "difference").inorder_list())

    def test_of_repeated_root(self):
        #Here we check if the method works for two trees that have the root repeated (difference)
        input_list_01 = [1, 2, 3, 4, 8, 6, 5]
        input_list_02 = [1, 5, 8, 6, 7, 10]

        for x in input_list_01:
            self.input1.insert(x)

        for x in input_list_02:
            self.input2.insert(x)

        for x in [2, 3, 4]:
            self.expected2.insert(x)

        self.assertEqual(self.expected2.inorder_list(), create_tree(self.input1, self.input2,
                                                                   "difference").inorder_list())
    def test_of_bigger_tree1(self):
        #Says if it works for a big tree 1, and a relatively small tree2 with some repeated elements (difference)
        input_list_01 = [1, 2, 3, 4, 8, 6, 5, 10, 15, 19]
        input_list_02 = [1, 6, 10]

        for x in input_list_01:
            self.input1.insert(x)

        for x in input_list_02:
            self.input2.insert(x)

        for x in [2, 3, 4, 8, 5, 15, 19]:
            self.expected2.insert(x)

        self.assertEqual(self.expected2.inorder_list(), create_tree(self.input1, self.input2,
                                                                   "difference").inorder_list())
# Some usage examples
if __name__ == '__main__':
    unittest.main()
