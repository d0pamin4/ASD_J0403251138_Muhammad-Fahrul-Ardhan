#=====================
#Praktikum 2
"""Latihan 2: implementasi pencarian pada node
tertentu single circular linked list"""
#=====================

#single circular linked list
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circularsinglelinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    #menambahkan elemen di akhir
    def insert_at_end(self,data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head 
        else:
            self.tail.next = new_node
            self.tail = new_node 
            self.tail.next = self.head 
    
    #menampilkan elemen
    def display(self):
        if not self.head:
            print("List kosong")
            return
        print("Circular Linked List Traversal:")
        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next

        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("... (back to head)")

    #fungsi mencari elemen
    def search(self, key):
        if not self.head:
            print("tidak boleh kosong. Tidak dapat mencari elemen.")
            return

        temp = self.head
        position = 0
        while temp:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam single circular linked list.")
                return
            temp = temp.next
            position += 1
        print(f"Elemen {key} tidak ditemukan dalam single circular linked list")

#contoh penggunaan
cll = circularsinglelinkedlist()

angkaUser = input("Masukkan elemen: ").split(",")
for num in angkaUser:
    cll.insert_at_end(int(num.strip()))

key = input("Masukkan elemen yang ingin dicari: ").strip()
cll.search(int(key))
