from DoubleNode import DoubleNode

class Lista_Doble:
    def __init(self):
        self.__head = NodoDoble(None, None, None)
        self.__tail = NodoDoble(None, None, None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty(self):
        if len(self.__data) == 0:
            return True
        else:
            return False

    def insert(self, value):
        if self.__size == 0:
            nuevo = NodoDoble(value, self.__head, self.__tail)
            self.__head.next = nuevo
            self.__tail.prev = nuevo
        else:
            nuevo = NodoDoble(value, self.__tail.prev, self.__tail)
            self.__tail.prev.next = nuevo
            self.__tail.prev = nuevo
        self.__size += 1

    def find_from_tail(self, value):
        if self.get_size() == 0:
            return False
        else:
            index = self.get_size()
            found = False
            curr_node = self.__tail.prev
            while found == False and index >= 0:
                if curr_node.data == value:
                    return index
                    found = True
                else:
                    if index == 0:
                        return False
                index--
                curr_node = curr_node.prev

    def find_from_head(self, value):
        if self.get_size() == 0:
            return False
        else:
            index = 0
            found = False
            curr_node = self.__head.next
            while found == False and index <= self.get_size():
                if curr_node.data == value:
                    return index
                    found = True
                else:
                    if index == self.get_size():
                        return False
                index++
                curr_node = curr_node.next

    def remove_from_head(self, value):
        nodoIndex = self.find_from_head(value)
        if nodoIndex != False and nodoIndex != -1:
            return False
        else:
            self.remove(nodoIndex)
            
    def remove_from_tail(self, value):
        nodoIndex = self.find_from_tail(value)
        if nodoIndex != False and nodoIndex != -1:
            return False
        else:
            self.remove(nodoIndex)

    def insert_between(self, value, predecesor, sucesor):
        nuevo = NodoDoble(value, predecesor, sucesor)
        predecesor.next = nuevo
        sucesor.prev = nuevo
        self.__size += 1

    def transversal(self):
        curr_node = self.__head.next
        while curr_node.next != None:
            print(curr_node.data, "->", end=" ")
            curr_node = curr_node.next
        print("")

    def reverse_transversal(self):
        curr_node = self.__tail.prev
        while curr_node.prev != None:
            print(curr_node.data, "->", end=" ")
            curr_node = curr_node.prev
        print("")
