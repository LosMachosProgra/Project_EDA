
from slistH import SList
import time

#This method have a lot of comments because programming class the teacher usually asked for a huge amount of
# comments on the code. After talking with the teacher responsible for the grading of this project we were
# instructed that for the next methods we don't make this amount of comments, but we were also told to let the
# comments that we had make at that moment.
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
            #one element before the first element of the longest sequence (high_index), we use one before because
            # later we're going to iterate until this previous element in order to skip the elements of the longest
            # sequence. The index starts at one because, we start iterating at index 1 with the position of nodeIt_1
            index, aux_high_index=1, 0
            #We have a variable that tells the longitude of each sequence (number sequence), and one that stores the
            # longitude of the largest one (max_sequence). Both start at 1 because we can't have a sequence of 0
            # elements
            number_sequence, max_sequence=1, 1
            #We go through the list looking for the largest sequence
            while nodeIt_1:
                #If the element is equal to the next one it will add a number to the number of sequence
                if nodeIt_1.elem == previous_1.elem:
                    number_sequence +=1
                #If the numbers are different, it will reset the variable
                else:
                    number_sequence = 1
                #If the previous sequence is the longest one, it will store the value in the max_sequence variable,
                # and the initial index on the aux_high_index variable
                if max_sequence <= number_sequence:
                    max_sequence = number_sequence
                    #This will give us the index of the element that goes before the first element of the longest
                    # sequence
                    aux_high_index = index - max_sequence

                #The index will keep increasing even if the elements are different
                index += 1

                #We reset the number of the sequence to 1, in order to start counting again how many elements belong
                # to the next sequence
                #We need to keep iterating even if the elements are different
                if nodeIt_1:
                    previous_1 = nodeIt_1
                    nodeIt_1 = nodeIt_1.next


            previous_2=self._head
            nodeIt_2=self._head.next

            # If the biggest sequence starts at zero; we put <= because aux_high_index gives the index element before
            # the longest sequence, in this case this subtraction (index-max-sequence) will give a negative number.
            if aux_high_index <= 0:
                nodeIt_2 = self._head
                #We skip the number of elements of the max_sequence
                for i in range(max_sequence):
                    nodeIt_2 = nodeIt_2.next
                self._head = nodeIt_2

            else:
            #When it doesn't start with the greater sequence
                #It iterates until one element before the first element of the largest sequence
                for i in range(aux_high_index):
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
        output= None
        if self.isEmpty():
            output = "The list is empty, there is no loop"
        else:
            # This fixes a loop if the element creates a loop with itself
            first = self._head
            if first == first.next:
                first.next = None
                output = "There was a loop"
            # This loop works to detect any loop that goes from the end to the begginning
            else:
                non_static = self._head
                nodeIt = self._head
                loop = False
                complete_loop = False

                # It iterates and looks if it founds the same element, if so, there is a loop. For this we iterate a
                # variable at a higher speed that the otherr, until they find each other.
                while nodeIt and not loop and not complete_loop:
                    nodeIt = nodeIt.next.next
                    non_static = non_static.next
                    if nodeIt:
                        if nodeIt.next.next == non_static.next and nodeIt.next.next == self._head:
                            complete_loop=True
                        elif nodeIt == non_static:
                            loop = True

                #If there is a loop that is not complete, we will start again the iteration of two variables,
                # the place where this two variable will find each other, is the place where the loop starts.

                if not complete_loop and loop:
                    non_static = self._head
                    while non_static.next != nodeIt.next:
                        non_static = non_static.next
                        nodeIt = nodeIt.next


                # if there was a complete loop, we fix it by making the next of the last element of the list equal to
                # None
                if complete_loop:
                    nodeIt.next.next= None
                    output = "There was a complete loop"
                #If there is a loop that is not complete, we will say that the next of the element that is before the
                # one where the loop begins will be zero.
                if loop:
                    nodeIt.next = None
                    output = "There Was a loop"

                if not loop and not complete_loop:
                    output = "There was no loop"

        print(output)


    def leftrightShift(self,left,n):
        if self.isEmpty() or n==0 or len(self)==1:
            pass
        #If n is equal to the len(self) the list will remain the same
        elif n > len(self) or n==len(self):
            pass

        elif len(self) == 2:
            nodeIt=self._head.next
            self._head.next=None
            nodeIt.next=self._head
            self._head=nodeIt
        else:
            previous=self._head
            node_It=previous.next
            #You need to iterate until one element becomes the one before the first one you will change of side,
            # and the other, the new head.
            if left==True:
                for i in range(n-1):
                    previous = node_It
                    node_It=node_It.next
                newhead = node_It

            if left==False:
                for i in range(len(self)-n-1):
                    previous=node_It
                    node_It=node_It.next

                newhead = node_It

            while node_It.next:
                node_It=node_It.next
            previous.next=None
            node_It.next=self._head
            self._head = newhead









#This are tests we used to find errors in the Delete Largest Sequence method
print("\nDelete largest sequence Example: \n")


list_prove= SList2()

for i in [4,4,4,4,4,4,4,4,4,4,5,3,3,3,3]:
    list_prove.addLast(i)
print("We're going to prove the list: ",list_prove)

start= time.time()

list_prove.delLargestSeq()

end = time.time()

print("End time was: ",end)
print("Start time was: ",start)
print("Total time was: ",end-start)

print("The new list: ", list_prove, "has a length of ", len(list_prove))


#This is for Fix loop definition
print("\n\nFix loop Examples: \n")

list2_prove = SList2()

for i in range(1,20):
    list2_prove.addLast(i)

print("We're searching for loop in this list: ",list2_prove)

list2_prove.create_loop(0)


start_1=time.time()

list2_prove.fix_loop()

end_1=time.time()

print("The end time was: ",end_1)
print("The start time was: ",start_1)
print("The total time was: ",end_1-start_1)

print("The final result is: ",list_prove)

list3_prove=SList2()

for i in range(1,20):
    list3_prove.addLast(i)

print("The list we're going to change is:",list3_prove)

list3_prove.leftrightShift(True,1)

print("The remaining list will be: ",list3_prove)
