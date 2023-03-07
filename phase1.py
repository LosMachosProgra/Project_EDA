"""
Created by (Esteban Gómez) in  ${2022}
"""
from slistH import SList
import time


class SList2(SList):
    def delLargestSeq(self):

        if self.isEmpty():
            print("The list is empty, you can not remove anything")
        elif len(self)==2:
            previous = self._head
            nodeIt= self._head.next
            if previous.elem==nodeIt.elem:
                self.removeFirst()
                self.removeLast()
            else:
                self.removeLast()
        else:
            # We start by head and head_next because we have already covered the cases in which we have 1 and 2
            # elements respectively
            previous_1 = self._head
            nodeIt_1 = self._head.next
            index, high_index=1, 0
            number_sequence, max_sequence=1, 1
            while nodeIt_1:
                while nodeIt_1 and nodeIt_1.elem == previous_1.elem:
                    number_sequence +=1
                    index += 1
                    previous_1 = nodeIt_1
                    nodeIt_1 = nodeIt_1.next

                if max_sequence <= number_sequence:
                    max_sequence = number_sequence
                    high_index = index - max_sequence
                index+=1
                number_sequence=1

                if nodeIt_1:
                    previous_1 = nodeIt_1
                    nodeIt_1 = nodeIt_1.next

            #If the biggest sequence starts at zero
            previous_2=self._head
            nodeIt_2=self._head.next

            if high_index == 0:
                nodeIt_2 = self._head
                for i in range(max_sequence):
                    nodeIt_2 = nodeIt_2.next
                self._head = nodeIt_2
            else:
            #When it doesn't start nor end with the greater sequence


                for i in range(high_index-1):
                    previous_2 = nodeIt_2
                    nodeIt_2=nodeIt_2.next
                i=0
                while i<= max_sequence-1 and nodeIt_2:
                    nodeIt_2 = nodeIt_2.next
                    if nodeIt_2 == None:
                        previous_2.next = None
                    i+=1

                if nodeIt_2:
                    previous_2.next = nodeIt_2

            self._size-= max_sequence

            return (str(max_sequence) + " en el " + str(high_index),"en este tiempo")




test_list= SList2()

for i in [2,5,3,2,4,5,5,5,2,4,4,4,4,4,4,4,4,4,4,4,5,4,3,4,5,6,3,4]:
    test_list.addLast(i)
print(test_list)

start= time.time()

test_list.delLargestSeq()

end = time.time()

print(end)
print(start)
print(end-start)

print(test_list, "The list has length: ", len(test_list))
