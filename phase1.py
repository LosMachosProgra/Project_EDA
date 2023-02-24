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
                while nodeIt_1.elem==previous_1.elem and nodeIt_1:
                    number_sequence +=1
                    previous_1 = nodeIt_1
                    nodeIt_1 = nodeIt_1.next
                    index+=1

                if max_sequence <= number_sequence:
                    max_sequence = number_sequence
                    high_index = index - max_sequence
                index+=1
                number_sequence=1

                if nodeIt_1:
                    previous_1 = nodeIt_1
                    nodeIt_1 = nodeIt_1.next

            previous_2=self._head
            nodeIt_2=self._head.next

            #When it doesn't star nor end with the greater sequence
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


            return str(max_sequence) +" en el " + str(high_index)


        pass

test_list= SList2()

for i in [3,1,1,1,2]:
    test_list.addLast(i)
print(test_list)

print(test_list.delLargestSeq())

print(test_list)




#for i in range(max_sequence):
             #   nodeIt_2 = nodeIt_2.next
              #  if nodeIt_2==None:
              #      previous_2.next=None
