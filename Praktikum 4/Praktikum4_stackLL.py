#========================================================
#Nama : Muhammad Fahrul Ardhan
#Nim  : J0403251138
#Kelas: TPL A1
#========================================================

#=======================================================
#IMPLEMENTASI DASAR : STACK
#=======================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil 
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer menunjuk ke note berikutnya (awal = none)

#stack ada operasi push(memasukkan head baru) dan pop (menghapus head)
class stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)
    
    def push(self,data): #memasukkann data baru pada stack
        #1 membuat node baru
        nodeBaru = Node(data)#instantiasi/memanggil konstruktor pada class Node

        #2 node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top 

        #3 geser top pindah ke node baru
        self.top = nodeBaru

    def is_empty(self):
        return self.top is None #stack kosong jika top = None
    
    def pop(self): #mengambil/menghapus node paling atas (top/head)
        
        if self.is_empty():
            print("stack kosong, tidak bisa pop")
            return None
        
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel
        #B -> A -> None
        self.top.next 
        self.top = self.top.next 
        return data_terhapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        #Top -> A ->B
        current = self.top 
        print("Top ->", end=" ")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

#instantiasi class stack
stack = stack()
stack.push("A")
stack.push("B")
stack.push("C")
stack.tampilkan()
stack.pop()
stack.tampilkan()
print("top saaat ini:", stack.peek())#melihat top tanpa menghapus
