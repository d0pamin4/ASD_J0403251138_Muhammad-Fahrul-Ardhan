# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Muhammad Fahrul Ardhan
# NIM     : J0403251138
# Kelas   : TPL A1
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]

nama_file = "buku.txt"
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    # Membaca file buku.txt dan memetakan datanya ke dalam struktur Dictionary
    database_buku = {}
    # TODO: Implementasikan kode pembacaan file di sini
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.split(',')
            kode_buku, judul, harga = baris
            database_buku[kode_buku] = {"judul": judul, "harga": int(harga)}
    return database_buku

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
    def __init__(self, judul):
        # Menyimpan data judul dan pointer ke node selanjutnya
        self.judul = judul
        self.next = None
        pass

class LinkedListPromosi:
    def __init__(self):
         # Inisialisasi awal Linked List dengan head kosong
         self.head = None


    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi (Linked List)"""
        # TODO: Implementasikan penambahan node
        node_baru = Node(judul)
        # Menambahkan node promosi baru di posisi paling akhir (tail)
        if self.head is None:
            self.head = node_baru
            print(f"[Sukses] '{judul}' ditambahkan sebagai promosi pertama.")
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = node_baru
        print(f"[Sukses] '{judul}' ditambahkan ke daftar promosi.")
        pass

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        # TODO: Implementasikan traversal linked list
        # Melakukan traversal (penelusuran) untuk mencetak semua node
        if self.head is None:
            print("[Info] Daftar promosi saat ini kosong.")
            return

        print("\n--- Daftar Buku Promosi ---")
        current = self.head
        indeks = 1
        while current:
            print(f"{indeks}. {current.judul}")
            current = current.next
            indeks += 1

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:
    def __init__(self):
        self.antrean = []# Inisialisasi list kosong sebagai penampung antrean


    def tambah_antrean(self, nama_pelanggan):
        """Menambah antrean (Enqueue)"""
        # TODO: Implementasikan prinsip FIFO
        self.antrean.append(nama_pelanggan)#Menambahkan pelanggan baru ke indeks paling akhir (belakang) dari antrean menggunakan metode .append().
        print(f"[Sukses] Pelanggan '{nama_pelanggan}' masuk ke dalam antrean.")
        pass

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue)"""
        # TODO: Implementasikan prinsip FIFO
        if len(self.antrean) == 0:
            print("[Info] Antrean kosong. Tidak ada pelanggan yang dilayani.")
            return None
        
        pelanggan_dilayani = self.antrean.pop(0)#Mengeluarkan dan melayani pelanggan dari indeks ke-0 (depan) menggunakan metode .pop(0)
        print(f"[Info] Melayani pelanggan: '{pelanggan_dilayani}'")
        return pelanggan_dilayani
        pass

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga secara manual menggunakan 
    Insertion Sort atau Merge Sort.
    """
    # TODO: Implementasikan algoritma sorting secara manual
    #Mengurutkan elemen secara Ascending menggunakan algoritma Insertion Sort
    n = len(list_harga)
    for i in range(1, n):
        key = list_harga[i]
        j = i - 1

        while j >= 0 and list_harga[j] > key:
            list_harga[j + 1] = list_harga[j]
            j -= 1
        list_harga[j + 1] = key
        
    return list_harga

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\nKatalog Buku:")
            if not data_buku:
                print("Katalog kosong atau file tidak ditemukan.")
            else:
                for kode, info in data_buku.items():
                    print(f"Kode: {kode} | Judul: {info['judul']} | Harga: Rp{info['harga']}")
        
        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':
            print("1. tambah antrean")
            print("2. hapus pelanggan")
            pilihan = int(input("masukkan pilihan 1/2 : "))

            if pilihan == 1:
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama)
            
            elif pilihan == 2:
                antrean_toko.layani_pelanggan()
            
            else:
                print("Aksi tidak valid.")

        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()