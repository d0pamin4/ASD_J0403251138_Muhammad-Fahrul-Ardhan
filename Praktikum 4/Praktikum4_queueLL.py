#========================================================
#Nama : Muhammad Fahrul Ardhan
#Nim  : J0403251138
#Kelas: TPL A1
#========================================================

#========================================================
#IMPLEMENTASI DASAR: QUEUE
#========================================================
class Node:
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil 
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer menunjuk ke note berikutnya (awal = none)

class queue:
    #buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #node paling depan
        self.rear = None #node paling belakang

    def is_empty(self):
        return self.front is None
    
    #membuat fungsi untuk menambahkan data baru bagian paling belakang
    def enqueue(self,data):
        nodeBaru = Node(data)

        #jika queque kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #jika queque tidak kosong, maka letakkandata baru ke setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru #letakkan data baru pada setelahnya rear
        self.rear = nodeBaru

    def dequeue(self):
        #menghapus data dari depan/front
        data_terhapus = self.front.data #lihat data paling depan

        #geser front ke node berikutnya
        self.front = self.front.next

        #jika setelah geser front menjadi none , maka queue ksong
        if self.front is None :
            self.rear = None
        return data_terhapus

    
    def tampilkan(self):
        current = self.front 
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end= "->")
            current = current.next
        print("Rear")

#instantiasi  class queque
q = queue()
q.enqueue("A")
q.tampilkan()
print("dequeued :", q.dequeue())
q.tampilkan()
