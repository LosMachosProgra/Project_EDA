"""
Created by (Esteban Gómez) in  ${2022}
"""
from slistH import SList


class SList2(SList):

    def delLargestSeq(self):
        # implement here your solution
        if self.isEmpty():
            print("The list is empty, you can not remove anything")
        elif len(self)==1:
            #If the list has one element, then it has 1  list of elements to remove
            self.removeFirst()
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
            previous_1=self._head
            nodeIt_1 = self._head.next
            index=1
            high_index=0
            number_sequence=1
            max_sequence=1
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

            # If the biggest sequence starts at zero
            previous_2=self._head
            nodeIt_2=self._head.next

            if high_index == 0:
                nodeIt_2 = self._head
                for i in range(max_sequence):
                    nodeIt_2 = nodeIt_2.next
                self._head = nodeIt_2

            #IT SEEMS THAT WE DON'T NEED THIS CONDITION

            # #If the largest sequence are in the last numbers
            # if index == len(self) - 1:
            #     nodeIt_2 = self._head
            #     for i in range(high_index):
            #         nodeIt_2=nodeIt_2.next
            #     nodeIt_2.next= None

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

            return (str(max_sequence) + " en el " + str(high_index))



        pass

test_list= SList2()

for i in [2,3,4, 1,1,1]:
    test_list.addLast(i)
print(test_list)

print(test_list.delLargestSeq())

print(test_list)
