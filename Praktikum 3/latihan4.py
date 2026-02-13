#========================
#Praktikum 3
#Latihan 4:menggabungkan 2 single linked list jadi baru
#==========================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        if not self.head:
            print("kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def merge(self, other_list):
        # Jika list pertama kosong
        if not self.head:
            return other_list

        # Jika list kedua kosong
        if not other_list.head:
            return self

        # Sambungkan tail list pertama ke head list kedua
        self.tail.next = other_list.head
        self.tail = other_list.tail

        return self
    
#contoh penggunaan
sll1 = SingleLinkedList()
sll2 = SingleLinkedList()

data1 = input("Masukkan elemen untuk linked list 1: ").split(",")
data2 = input("Masukkan elemen untuk linked list 2: ").split(",")
for num in data1:
    sll1.insert_at_end(int(num.strip()))

for num in data2:
    sll2.insert_at_end(int(num.strip()))

merged = sll1.merge(sll2)
print("linked list setelah berhasil digabungkan")
merged.display()