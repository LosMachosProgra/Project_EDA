"""
Created by (Esteban Gómez) in  ${2022}
"""
from slistH import SList
import time


class SList2(SList):
    def delLargestSeq(self):
        #This check the case in which the list is empty
        if self.isEmpty():
            print("The list is empty, you can not remove anything")
        #This is for the case in which the list is of lenght two
        elif len(self)==2:
            previous = self._head
            nodeIt= self._head.next
            #If both elements are equal, it will remove both
            if previous.elem==nodeIt.elem:
                self.removeFirst()
                self.removeLast()
            #If both elements are different, it will remove the last one
            else:
                self.removeLast()
        else:
            # We start by head and head_next because we have already covered the cases in which we have 2
            # elements (head.next will not be none)
            previous_1 = self._head
            nodeIt_1 = self._head.next
            #We create a variable that will tell the index of each element (index), and one that tells the index of the
            #first element of the longest sequence (high_index). The index starts at one because, we start iterating
            # at index 1 with the position of nodeIt_1
            index, high_index=1, 0
            #We have a variable that tells the longitude of each sequence (number sequence), and one that stores the
            # longitude of the largest one (max_sequence). Both start at 1 because we can't have a sequence of 0
            # elements
            number_sequence, max_sequence=1, 1
            #We go through the list looking for the largest sequence
            while nodeIt_1:
                #If the element is equal to the next one it will keep in the loop and store the longitude and initial
                # index of the sequence
                while nodeIt_1 and nodeIt_1.elem == previous_1.elem:
                    number_sequence +=1
                    index += 1
                    previous_1 = nodeIt_1
                    nodeIt_1 = nodeIt_1.next
                #If the previous sequence is the longest one, it will store the value in the max_sequence variable,
                # and the initial index on the high_index variable
                if max_sequence <= number_sequence:
                    max_sequence = number_sequence
                    high_index = index - max_sequence
                #The index will keep increasing even if the elements are different
                index+=1
                #We reset the number of the sequence to 1, in order to start counting again how many elements belong
                # to the next sequence
                number_sequence=1
                #We need to keep iterating even if the elements are different
                if nodeIt_1:
                    previous_1 = nodeIt_1
                    nodeIt_1 = nodeIt_1.next


            previous_2=self._head
            nodeIt_2=self._head.next

            # If the biggest sequence starts at zero
            if high_index == 0:
                nodeIt_2 = self._head
                #We skip the number of elements of the max_sequence
                for i in range(max_sequence):
                    nodeIt_2 = nodeIt_2.next
                self._head = nodeIt_2

            else:
            #When it doesn't start with the greater sequence
                #It iterates until one element before the first element of the largest sequence
                for i in range(high_index-1):
                    previous_2 = nodeIt_2
                    nodeIt_2=nodeIt_2.next

                #From the element before the first one of the largest list, we will skip the number of elements that
            # belong to the longest sequence (we know this thanks to the variable max_sequence). nodeIt_2 will end at
            # the first element after the sequence. We also put the parameter that nodeIt_2 should exist to take into
            # account the case in which the longest sequence is at the end.
                i=0
                while i< max_sequence and nodeIt_2:
                    nodeIt_2 = nodeIt_2.next
                    if nodeIt_2 == None:
                        previous_2.next = None
                    i+=1
                #The next of the last element before the longest sequence, will lead to the first element after the
            # sequence
                if nodeIt_2:
                    previous_2.next = nodeIt_2

            #We subtract to size the amount of elements we removed
            self._size-= max_sequence

            #This was used to check if the method was identifying the correct largest sequence at the correct index
            #return (str(max_sequence) + " en el " + str(high_index),"en este tiempo")


    def create_loop(self, position):
        # this method is used to force a loop in a singly linked list
        if position < 0 or position > len(self) - 1:
            raise ValueError(f"Position out of range [{0} - {len(self) - 1}]")

        current = self._head
        i = 0

        # We reach position to save the reference
        while current and i < position:
            current = current.next
            i += 1

        # We reach to tail node and set the loop
        start_node = current
        print(f"Creating a loop starting from {start_node.elem}")
        while current.next:
            current = current.next
        current.next = start_node


    def fix_loop(self):
        # In an empty list there are no loops
        if self.isEmpty():
            output = "The list is empty, there is no loop"
        else:
            # This fixes a loop if the element creates a loop with itself
            static = self._head
            if static == static.next:
                static.next = None
                output = "There was a loop"
            # This loop works to detect any loop that goes from the end to the begginning
            else:
                static = self._head
                non_static=self._head
                nodeIt = self._head.next
                loop = False
                # It iterates and if it finds self.head (static) again, there will be a loop
                i=0
                while nodeIt and static and not loop:
                    nodeIt = nodeIt.next
                    if i % (len(self)-1) == 0:
                        non_static = non_static.next
                    if nodeIt:
                        if nodeIt.next == static or nodeIt.next==non_static:
                            loop = True
                    i+=1

                # if there was loop, we fix it by making the next of the last element of the list equal to None
                if loop:
                    nodeIt.next = None
                    output = "There Was a loop"
                if not loop:
                    output = "There was no loop"

        print(output)




test_list= SList2()

for i in [2,5,3,2,4,5,5,5,2,4,4,4,4,4,4,4,4,4,4,4,5,3,3,3,3]:
    test_list.addLast(i)
print("We're going to prove the list: ",test_list)

start= time.time()

test_list.delLargestSeq()

end = time.time()

print("End time was: ",end)
print("Start time was: ",start)
print("Total time was: ",end-start)

print("The new list: ", test_list, "has a length of ", len(test_list))


#This is for Fix loop definition
print("\n\nFix loop Examples: \n")

list_prove = SList2()

for i in range(1,20):
    list_prove.addLast(i)

print("We're searching for loop in this list: ",list_prove)

list_prove.create_loop(16)
