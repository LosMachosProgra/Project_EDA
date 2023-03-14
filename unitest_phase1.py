import unittest
from phase1 import SList2


class Tests(unittest.TestCase):
        #This Class will check the possible cases where we could have errors for the function delLargestSequence

    def setUp(self):
        #This is the list that we're going to use as base in most of the tests
        self.input=SList2()
        self.expected = SList2()


    def test_for_empty(self):
        """This function checks if the method works for an empty list"""
        self.input.delLargestSeq()
        #The assertEqual method help us to see if our expected value is the same that we got as result
        self.assertEqual(0,len(self.input))
        self.assertEqual("",str(self.input))

    def test_for_len_1(self):
        """This method help us check if the function works for list of 1 element"""
        #We add 1 element as we want to prove it works for 1 node lists.
        self.input.addFirst(1)
        self.input.delLargestSeq()
        self.expected= ""
        self.assertEqual(str(self.expected),str(self.input))

    def test_for_len_2_equal(self):
        """This method help us check if the function works for list of 2 elements that are equal"""
        #The loop was made with the objective of adding two nodes to the list
        for i in range(2):
            self.input.addFirst(1)
        self.input.delLargestSeq()
        #We expect the method eliminates all the list
        self.expected= ""
        self.assertEqual(str(self.expected),str(self.input))

    def test_for_len_2_distinct(self):
        """Checks if the method works for lists of two nodes of different values"""
        #The loop was made with the objective of adding two nodes to the list
        self.input.addFirst(1)
        self.input.addLast(2)
        self.input.delLargestSeq()
        #We expect that the method eliminates the last element of the list
        self.expected= 1
        self.assertEqual(str(self.expected),str(self.input),)



    def test_for_1_sequence(self):
        """Checks if the method works for lists with only one sequence"""
        for i in [1,2,4,4,4,2,3]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates the sequence
        self.expected= "1,2,2,3"
        self.assertEqual(str(self.expected),str(self.input),)

    def test_for_big_sequence(self):
        """Checks if the method works for lists with only one sequence"""
        for i in [1,2,4,4,4,4,4,4,4,4,2,3]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates the big sequence
        self.expected= "1,2,2,3"
        self.assertEqual(str(self.expected),str(self.input),)


    def test_for_2_size_sequences(self):
        """Checks if the method works for two sequences of different sizes"""
        for i in [1,3,3,4,4,4,3]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates the biggest sequence
        self.expected= "1,3,3,3"
        self.assertEqual(str(self.expected),str(self.input),)


    def test_for_3_size_sequences(self):
        """Checks if the method works for 3 lists of different sizes"""
        for i in [1,3,3,3,6,5,6,4,4,4,4,4,4,4,4,2,3,4,4,4,4,2]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates the biggest sequence
        self.expected= "1,3,3,3,6,5,6,2,3,4,4,4,4,2"
        self.assertEqual(str(self.expected),str(self.input))

    def test_for_same_size_sequences(self):
        """Checks if the method works for list with two sequences of same size"""
        for i in [1,3,3,4,4,3]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates from both sequences the one that is more to the right
        self.expected= "1,3,3,3"
        self.assertEqual(str(self.expected),str(self.input))

    def test_for_3_same_sequences(self):
        """Checks if the method works for lists with only one sequence"""
        for i in [1,3,3,3,4,4,4,2,2,2,1]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates the biggest sequence
        self.expected= "1,3,3,3,4,4,4,1"
        self.assertEqual(str(self.expected),str(self.input))

    def test_for_begginning(self):
        """Checks if the method works for lists that start with the biggest sequence"""
        for i in [3,3,3,3,4,4,3]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates the biggest sequence, that is the first one
        self.expected= "4,4,3"
        self.assertEqual(str(self.expected),str(self.input))

    def test_for_ending(self):
        """Checks if the method works for lists that end in the biggest sequence"""
        for i in [1,3,3,4,6,6,6,6,6,6]:
            self.input.addLast(i)

        self.input.delLargestSeq()
        #We expect that it eliminates the biggest sequence, that is the last one
        self.expected= "1,3,3,4"
        self.assertEqual(str(self.expected),str(self.input))

    def test_for_all_same(self):
        """Checks if the method works for lists with only the same element"""
        for i in [6, 6, 6, 6]:
            self.input.addLast(i)
        self.input.delLargestSeq()
        # We expect that it eliminates the biggest sequence
        self.expected = ""
        self.assertEqual(str(self.expected),str(self.input))

    def test_for_complete_loop(self):
        """Checks if the method of fixing loop works for a loop that end in the last node and starts at self_head"""
        for i in [1, 2, 3, 4, 5, 6]:
            self.input.addLast(i)
        self.input.create_loop(0)
        self.input.fix_loop()
        self.expected="1,2,3,4,5,6"
        self.assertEqual(str(self.expected),str(self.input))

    def test_for_loop_at_beggining(self):
        """Checks if the method of fixing loop works for a loop that is at the begginning og the list"""
        for i in range(1,20):
            self.input.addLast(i)
        self.input.create_loop(2)
        self.input.fix_loop()
        self.expected="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19"
        self.assertEqual(str(self.expected),str(self.input))


    def test_for_loop_at_almost_end(self):
        """Checks if the method of fixing loop works for a loop that is almost at the end"""
        for i in range(1,20):
            self.input.addLast(i)
        self.input.create_loop(17)
        self.input.fix_loop()
        self.expected="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19"
        self.assertEqual(str(self.expected),str(self.input))


    def test_for_loop_at_middle_odd(self):
        """Checks if the method of fixing loop works for a loop that goes from the middle of the sequence and
        starts at the final element"""
        for i in range(1,20):
            self.input.addLast(i)
        self.input.create_loop(11)
        self.input.fix_loop()
        self.expected="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19"
        self.assertEqual(str(self.expected),str(self.input))

    def test_for_loop_at_almostmiddle_even(self):
        """Checks if the method of fixing loop works for a loop that goes from the end to the middle node plus one """
        for i in range(1, 21):
            self.input.addLast(i)
        self.input.create_loop(11)
        self.input.fix_loop()
        self.expected = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20"
        self.assertEqual(str(self.expected), str(self.input))

    def test_for_loop_at_last(self):
        """Checks if the method of fixing loop works for a loop in the end of the list """
        for i in range(1, 21):
            self.input.addLast(i)
        self.input.create_loop(len(self.input)- 1)
        self.input.fix_loop()
        self.expected = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20"
        self.assertEqual(str(self.expected), str(self.input))

    def test_for_Empty_lrs(self):        #lrs=left-right_shift
        """Checks if the method works for an empty list"""
        self.input.leftrightShift(True,1)
        #We expect to return an empty list
        self.expected= ""
        self.assertEqual(str(self.expected),str(self.input))

    def test_for_n_equal_len(self):
        """Checks if the method works for n==len(self)"""
        for i in [1, 2, 3, 4, 5, 6]:
            self.input.addLast(i)
            self.expected.addLast(i)
        self.input.leftrightShift(True, 6)
        # We should end up with the same list
        self.assertEqual(str(self.expected), str(self.input))

    def test_for_len1(self):
        """Checks if the method works for lists with only the same element"""
        self.input.addLast(1)
        self.input.leftrightShift(True,1)
        # We expect that it returns the same list
        self.expected = "1"
        self.assertEqual(str(self.expected),str(self.input))

    def test_for_n0(self):
        """Checks if the method works for n=0"""
        for i in [1, 2, 3, 4, 5, 6]:
            self.input.addLast(i)
        self.input.leftrightShift(True,0)
        self.expected="1,2,3,4,5,6"
        self.assertEqual(str(self.expected),str(self.input))

    def test_for_n_bigger(self):
        """Checks if the method works for n>len(self)"""
        for i in [1, 2, 3, 4, 5, 6]:
            self.input.addLast(i)
            self.expected.addLast(i)
        self.input.leftrightShift(True, 7)
        #We should end up with the same list
        self.assertEqual(str(self.expected), str(self.input))


    def test_for_left_small_n(self):
        """Checks if the method is correct when applying a small n and saying that left =True"""
        for i in range(1,20):
            self.input.addLast(i)
        self.input.leftrightShift(True,2)
        self.expected="3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,1,2"
        self.assertEqual(str(self.expected),str(self.input))

    def test_for_left_big_n(self):
        """Checks if the method is correct when applying a big n and saying that left =True"""
        for i in range(1, 20):
            self.input.addLast(i)
        self.input.leftrightShift(True, 10)
        self.expected = "11,12,13,14,15,16,17,18,19,1,2,3,4,5,6,7,8,9,10"
        self.assertEqual(str(self.expected), str(self.input))


    def test_for_left_false_small_n(self):
        """Checks if the method is correct when applying a small n and saying that left =False"""
        for i in range(1, 20):
            self.input.addLast(i)
        self.input.leftrightShift(False, 2)
        self.expected = "18,19,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17"
        self.assertEqual(str(self.expected), str(self.input))

    def test_for_left_false_big_n(self):
        """Checks if the method is correct when applying a big n and saying that left =False"""
        for i in range(1, 20):
            self.input.addLast(i)
        self.input.leftrightShift(False, 14)
        self.expected = "6,7,8,9,10,11,12,13,14,15,16,17,18,19,1,2,3,4,5"
        self.assertEqual(str(self.expected), str(self.input))
