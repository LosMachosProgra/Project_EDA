
import unittest
from phase1 import SList2



class Test_for_delLargestSeq(unittest.TestCase):
        #This Class will check the possible cases where we could have errors for the function delLargestSequence

    def setUp(self):
        #This is the list that we're going to use as base in most of the tests
        self.input=SList2()


    def test_for_empty(self):
        """This function checks if the method works for an empty list"""
        self.input.delLargestSeq()
        #The assertEqual method help us to see if our expected value is the same that we got as result
        self.assertEqual(len(self.input),0)
        self.assertEqual(str(self.input), "")

    def test_for_len_1(self):
        """This method help us check if the function works for list of 1 element"""
        self.expected = SList2()
        #We add 1 element as we want to prove it works for 1 node lists.
        self.input.addFirst(1)
        self.input.delLargestSeq()
        self.expected= ""
        self.assertEqual(str(self.input),str(self.expected))

    def test_for_len_2_equal(self):
        """This method help us check if the function works for list of 2 elements that are equal"""
        self.expected = SList2()
        #The loop was made with the objective of adding two nodes to the list
        for i in range(2):
            self.input.addFirst(1)
        self.input.delLargestSeq()
        #We expect the method eliminates all the list
        self.expected= ""
        self.assertEqual(str(self.input),str(self.expected))

    def test_for_len_2_distinct(self):
        """Checks if the method works for lists of two nodes of different values"""
        self.expected = SList2()
        #The loop was made with the objective of adding two nodes to the list
        self.input.addFirst(1)
        self.input.addLast(2)
        self.input.delLargestSeq()
        #We expect that the method eliminates the last element of the list
        self.expected= 1
        self.assertEqual(str(self.input),str(self.expected))



    def test_for_1_sequence(self):
        """Checks if the method works for lists with only one sequence"""
        self.expected = SList2()
        for i in [1,2,4,4,4,2,3]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates the sequence
        self.expected= "1,2,2,3"
        self.assertEqual(str(self.input),str(self.expected))

    def test_for_big_sequence(self):
        """Checks if the method works for lists with only one sequence"""
        self.expected = SList2()
        for i in [1,2,4,4,4,4,4,4,4,4,2,3]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates the big sequence
        self.expected= "1,2,2,3"
        self.assertEqual(str(self.input),str(self.expected))


    def test_for_2_size_sequences(self):
        """Checks if the method works for two sequences of different sizes"""
        self.expected = SList2()
        for i in [1,3,3,4,4,4,3]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates the biggest sequence
        self.expected= "1,3,3,3"
        self.assertEqual(str(self.input),str(self.expected))


    def test_for_3_size_sequences(self):
        """Checks if the method works for 3 lists of different sizes"""
        self.expected = SList2()
        for i in [1,3,3,3,6,5,6,4,4,4,4,4,4,4,4,2,3,4,4,4,4,2]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates the biggest sequence
        self.expected= "1,3,3,3,6,5,6,2,3,4,4,4,4,2"
        self.assertEqual(str(self.input),str(self.expected))

    def test_for_same_size_sequences(self):
        """Checks if the method works for list with two sequences of same size"""
        self.expected = SList2()
        for i in [1,3,3,4,4,3]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates from both sequences the one that is more to the right
        self.expected= "1,3,3,3"
        self.assertEqual(str(self.input),str(self.expected))

    def test_for_3_same_sequences(self):
        """Checks if the method works for lists with only one sequence"""
        self.expected = SList2()
        for i in [1,3,3,3,4,4,4,2,2,2,1]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates the biggest sequence
        self.expected= "1,3,3,3,4,4,4,1"
        self.assertEqual(str(self.input),str(self.expected))

    def test_for_begginning(self):
        """Checks if the method works for lists that start with the biggest sequence"""
        self.expected = SList2()
        for i in [3,3,3,4,4,3]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates the biggest sequence, that is the first one
        self.expected= "4,4,3"
        self.assertEqual(str(self.input),str(self.expected))

    def test_for_ending(self):
        """Checks if the method works for lists that end in the biggest sequence"""
        self.expected = SList2()
        for i in [1,3,3,4,6,6,6,6]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates the biggest sequence, that is the last one
        self.expected= "1,3,3,4"
        self.assertEqual(str(self.input),str(self.expected))

    def test_for_all_same(self):
        """Checks if the method works for lists with only the same element"""
        self.expected = SList2()
        for i in [6, 6, 6, 6]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        # We expect that it eliminates the biggest sequence
        self.expected = ""
        self.assertEqual(str(self.input), str(self.expected))
