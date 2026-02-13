#========================
#Praktikum 3:linked list
#latihan 1
#========================

#single linked list
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None # Tambahkan pointer tail

    #fungsi untuk menambah data di akhir
    def insert_at_end(self, data):
        new_node = node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node # Tail juga menunjuk ke node pertama
        else:
            self.tail.next = new_node # Sambungkan tail ke node baru
            self.tail = new_node # Update tail ke node baru

    #fungsi untuk memperlihatkan node
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    
    #fungsi untuk menghapus node tertentu
    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

#contoh penggunaan
ll = linkedlist()
print("sebelum dihapus")
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(13)
ll.insert_at_end(2)
ll.display()

#menghapus node 13
print("setelah dihapus")
ll.delete_node(13)
ll.display()