# Nama  : Muhammad Fahrul Ardhan
# NIM : J0403251138
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# 1. Berapa jarak terpendek dari A ke B?
    """Jarak terpendek dari A ke B = 4 (langsung A -> B, bobot 4).
    Tidak ada jalur lain yang lebih pendek menuju B."""

# 2. Berapa jarak terpendek dari A ke C?
#   Jarak terpendek dari A ke C = 2 (langsung A -> C, bobot 2).

# 3. Berapa jarak terpendek dari A ke D?
    """Jarak terpendek dari A ke D = 3.
    Dicapai melalui jalur A -> C -> D (2 + 1 = 3),
    bukan A -> B -> D (4 + 5 = 9)."""

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
    """Karena total bobot jalur A -> C -> D (2 + 1 = 3) jauh lebih kecil
    dari jalur A -> B -> D (4 + 5 = 9). Meskipun A->C bukan tetangga
    langsung D, kombinasi bobot A->C dan C->D menghasilkan total yang
    lebih optimal."""

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
    """Priority queue berfungsi untuk selalu memproses node dengan jarak
    terkecil (tentative distance) terlebih dahulu. Dengan struktur
    min-heap (heapq), node yang jaraknya paling kecil akan di-pop
    pertama kali, menjamin bahwa ketika suatu node diproses, jarak
    yang tercatat sudah merupakan jarak terpendek finalnya."""

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
    """Dijkstra mengasumsikan bahwa sekali sebuah node diproses (di-pop
    dari priority queue), jaraknya sudah final dan tidak akan berkurang
    lagi. Dengan bobot negatif, asumsi ini bisa dilanggar karena edge
    negatif dapat menciptakan jalur yang lebih pendek ke node yang
    sudah diproses sebelumnya, sehingga hasil Dijkstra menjadi salah.
    Untuk bobot negatif, gunakan algoritma Bellman-Ford."""
# ==========================================================