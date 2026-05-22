# Nama  : Muhammad Fahrul Ardhan
# NIM : J0403251138
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 5: Studi Kasus dengan Program Shortest Path
# Mencari jalur terpendek antar kota menggunakan Dijkstra
# ==========================================================

import heapq

# -------------------------------------------------------
# Representasi graph berbobot menggunakan dictionary
# Bobot merepresentasikan jarak antar kota
# -------------------------------------------------------
graph = {
    'Bogor':   {'Jakarta': 5, 'Depok': 2},  # Bogor -> Jakarta = 5, Bogor -> Depok = 2
    'Depok':   {'Jakarta': 2, 'Bandung': 6}, # Depok -> Jakarta = 2, Depok -> Bandung = 6
    'Jakarta': {'Bandung': 7},               # Jakarta -> Bandung = 7
    'Bandung': {}                            # Bandung adalah node tujuan (tidak ada edge keluar)
}

# -------------------------------------------------------
# Fungsi Dijkstra
# Mengembalikan dictionary berisi jarak terpendek dari
# node 'start' ke semua node lain dalam graph
# -------------------------------------------------------
def dijkstra(graph, start):
    # Inisialisasi semua jarak sebagai tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue: menyimpan (jarak, node), diproses dari jarak terkecil
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika sudah ditemukan jarak yang lebih baik sebelumnya
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil, perbarui dan masukkan ke queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# -------------------------------------------------------
# Penentuan node awal: Bogor
# -------------------------------------------------------
node_awal = 'Bogor'
hasil = dijkstra(graph, node_awal)

# -------------------------------------------------------
# Output jarak terpendek dari node awal ke semua node
# -------------------------------------------------------
print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"  {node_awal} -> {kota} = {jarak}")

# ==========================================================
# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
#    Node awal yang digunakan adalah BOGOR. Semua jarak terpendek dihitung mulai dari Bogor ke setiap kota lainnya.

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
    """Node dengan jarak paling kecil dari Bogor adalah DEPOK
    dengan jarak = 2. Depok merupakan tetangga langsung Bogor
    dengan edge terpendek (Bogor -> Depok = 2)."""
#
# 3. Node mana yang memiliki jarak paling besar dari node awal?
    """Node dengan jarak paling besar dari Bogor adalah BANDUNG
    dengan jarak = 8. Jalur terpendek menuju Bandung adalah:
    Bogor -> Depok -> Bandung = 2 + 6 = 8."""

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus ini:
    """Langkah-langkah Dijkstra dari Bogor:
    - Inisialisasi: Bogor=0, Jakarta=inf, Depok=inf, Bandung=inf
    - Proses Bogor (jarak 0):
        Perbarui Jakarta = min(inf, 0+5) = 5
        Perbarui Depok   = min(inf, 0+2) = 2
      Queue: [(2, Depok), (5, Jakarta)]
    - Proses Depok (jarak 2, terkecil di queue):
        Perbarui Jakarta = min(5, 2+2) = 4  ← lebih kecil, diperbarui!
        Perbarui Bandung = min(inf, 2+6) = 8
      Queue: [(4, Jakarta), (5, Jakarta_lama), (8, Bandung)]
    - Proses Jakarta (jarak 4):
        Perbarui Bandung = min(8, 4+7) = 8  ← sama, tidak berubah
      Queue: [(5, Jakarta_lama), (8, Bandung)]
    - Jakarta_lama (jarak 5) dilewati karena 5 > distances[Jakarta]=4
    - Proses Bandung (jarak 8): tidak ada tetangga, selesai
    Hasil akhir: Bogor=0, Depok=2, Jakarta=4, Bandung=8"""
# ==========================================================