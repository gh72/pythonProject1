class Node:

    def __init__(self, data ):
        self.data = data
        self.next_node = None

class LinkedList:

    def __init__(self):
        self.anzahl = 0
        self.head = None

    def insert(self, data):

        self.anzahl =  self.anzahl + 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head =  new_node

    def size_of_list(self):
        return self.anzahl

    def traverse(self):

        actual_node = self.head
        print("Head is",actual_node.data)

        while actual_node is not None :
            print(actual_node.data)
            actual_node = actual_node.next_node

    def reverse_list(self):

        # Falls die Liste leer wäre
        if self.head is None:
            return

        current_node = self.head
        previous_node = None
        next_node = None

        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node



    def remove(self, data):

        #liste ist leer
        if self.head is None:
            return
        actual_node = self.head

        #pointer auf voriger Node
        previous_node = None

        #finde den Datensatz
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        if actual_node is None:
            return

        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node



if __name__ == '__main__':

    meine_liste = LinkedList()
    meine_liste.insert(1)
    meine_liste.insert(2)
    meine_liste.insert(3)
    meine_liste.insert(4)

    meine_liste.traverse()

    meine_liste.reverse_list()
    print("\n")
    meine_liste.traverse()
