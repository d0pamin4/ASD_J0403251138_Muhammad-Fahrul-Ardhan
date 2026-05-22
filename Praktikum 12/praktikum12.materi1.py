#=======================================================================================
# Nama    : Muhammad Fahrul Ardhan
# NIM     : J0403251138
# Kelas   : A1
#=======================================================================================

import heapq  # Library untuk menggunakan priority queue (heap)

# Representasi graph dalam bentuk dictionary
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    # Menyimpan jarak minimum dari node awal ke semua node
    distances = {node: float('inf') for node in graph}

    # Jarak node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue untuk memilih node dengan jarak terkecil
    pq = [(0, start)]

    # Perulangan selama queue masih berisi node
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Memeriksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():

            # Menghitung total jarak baru
            distance = current_distance + weight

            # Jika jarak baru lebih kecil, update jarak
            if distance < distances[neighbor]:

                distances[neighbor] = distance

                # Menambahkan node ke priority queue
                heapq.heappush(pq, (distance, neighbor))

    # Mengembalikan hasil jarak minimum
    return distances

# Menjalankan algoritma Dijkstra dari node A
hasil = dijkstra(graph, 'A')

# Menampilkan hasil jarak minimum
print(hasil)