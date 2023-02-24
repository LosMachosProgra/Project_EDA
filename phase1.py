from slistH import SList


class SList2(SList):

    def delLargestSeq(self):
        # implement here your solution
        if self.isEmpty():
            print("The list is empty, you can not remove anything")
        if len(self)==1:
            self.removeFirst()
        if len(self)==2:
            self.removeLast()
        else:
            # We start by head and head_next because we have already covered the cases in which we have 1 and 2
            # elements respectively
            previous=self._head
            nodeIt_1 = self._head.next
            index=1
            high_index=0
            number_sequence=1
            max_sequence=1
            while nodeIt_1:
                while nodeIt_1.elem==previous.elem:
                    number_sequence +=1
                    previous = nodeIt_1
                    nodeIt_1 = nodeIt_1.next
                    index+=1

                if max_sequence <= number_sequence:
                    max_sequence = number_sequence
                    high_index = index - max_sequence
                index+=1
                number_sequence=1

                previous = nodeIt_1
                nodeIt_1 = nodeIt_1.next
            return str(max_sequence) +" en el " + str(high_index)






        pass

test_list= SList2()

for i in [3,3,4,5,6,7,7,7,2]:
    test_list.addLast(i)
print(test_list)

print(test_list.delLargestSeq())



