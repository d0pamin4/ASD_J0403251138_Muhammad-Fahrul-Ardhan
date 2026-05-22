# Nama  : Muhammad Fahrul Ardhan
# NIM : J0403251138
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# ==========================================================
# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
    """Lokasi paling dekat dari Gerbang adalah KANTIN dengan jarak 2 menit
    (edge langsung Gerbang -> Kantin = 2 menit)."""

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
    """Waktu tempuh terpendek dari Gerbang ke Aula = 7 menit.
    Jalur: Gerbang -> Kantin -> Lab -> Aula = 2 + 4 + 1 = 7 menit.
    Lebih cepat dibanding: Gerbang -> Kantin -> Aula = 2 + 7 = 9 menit,
    atau: Gerbang -> Perpustakaan -> Lab -> Aula = 6 + 3 + 1 = 10 menit."""

# 3. Apakah jalur yang menghasilkan jarak paling kecil selalu
#    menggunakan edge paling sedikit? Jelaskan.
    """TIDAK. Jalur dengan edge paling sedikit belum tentu paling hemat
    waktu. Algoritma Dijkstra mengoptimalkan TOTAL BOBOT, bukan jumlah edge."""

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
    """Dijkstra cocok karena semua bobot pada graph ini bernilai POSITIF. Dijkstra efisien untuk kasus
    seperti ini. Selain itu, graph lokasi kampus relatif kecil sehingga Dijkstra sangat praktis dan
    memberikan hasil yang tepat dan cepat."""
# ==========================================================