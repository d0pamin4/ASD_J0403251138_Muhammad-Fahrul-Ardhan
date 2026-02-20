#========================================================
#Nama : Muhammad Fahrul Ardhan
#Nim  : J0403251138
#Kelas: TPL A1
#========================================================

#=======================================================
#IMPLEMENTASI DASAR : NODE PADA LINKED LIST
#========================================================
class Node:
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil 
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer menunjuk ke note berikutnya (awal = none)

#1 )cara membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) mendefiniskan head dan menghubungkan node : A ->B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) Traversal = menelusuri node dari head sampai ke none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya
