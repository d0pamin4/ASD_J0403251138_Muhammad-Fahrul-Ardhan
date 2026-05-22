# Nama  : Muhammad Fahrul Ardhan
# NIM : J0403251138
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + \
weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B?
#    Bobot langsung A ke B = 5 (edge langsung A -> B dengan weight 5).

# 2. Berapa total bobot jalur A -> C -> B?
    """Total bobot jalur A -> C -> B = graph['A']['C'] + graph['C']['B']
    = 4 + (-2) = 2."""

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
    """Jalur A -> C -> B menghasilkan jarak lebih kecil menuju B, yaitu 2,
    dibandingkan jalur langsung A -> B yang bobotnya 5.
    Bellman-Ford berhasil menemukan jalur optimal ini melalui proses
    relaksasi berulang."""

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
    """Karena Bellman-Ford tidak mengasumsikan jarak sudah final saat node
    diproses. Algoritma ini melakukan relaksasi semua edge sebanyak
    (|V| - 1) kali, sehingga setiap kemungkinan jalur termasuk yang
    menggunakan edge berbobot negatif pasti dievaluasi dan diperbarui
    jika ditemukan jalur yang lebih pendek."""

# 5. Apa yang dimaksud dengan proses relaksasi edge?
    """Relaksasi edge adalah proses memeriksa apakah jarak ke suatu node
    tetangga dapat diperpendek melalui node saat ini. Jika
    distances + weight < distances, maka jarak ke
    neighbor diperbarui. Proses ini diulang (|V| - 1) kali untuk
    memastikan semua jalur terpendek ditemukan, bahkan yang melewati
    banyak node."""

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
    """- Bellman-Ford: kompleksitas O(V*E), dapat menangani bobot negatif,
      dapat mendeteksi negative cycle, cocok untuk graph umum.
    - Dijkstra:dengan priority queue,TIDAK dapat menangani bobot negatif, lebih cepat untuk graph
      dengan bobot positif. Dijkstra menggunakan greedy (proses node
      jarak terkecil duluan), sedangkan Bellman-Ford melakukan relaksasi
      semua edge secara berulang tanpa urutan prioritas."""
# ==========================================================