#=======================================================================================
# Nama    : Muhammad Fahrul Ardhan
# NIM     : J0403251138
# Kelas   : A1
#=======================================================================================

def bellman_ford(graph, start):

    # Menyimpan jarak minimum dari node awal ke semua node
    distances = {node: float('inf') for node in graph}

    # Jarak node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Proses relaksasi dilakukan sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Menelusuri setiap node pada graph
        for node in graph:

            # Memeriksa setiap tetangga dan bobot jalurnya
            for neighbor, weight in graph[node].items():

                # Jika ditemukan jarak yang lebih kecil
                if distances[node] + weight < distances[neighbor]:

                    # Update jarak minimum
                    distances[neighbor] = distances[node] + weight

    # Mengembalikan hasil jarak minimum
    return distances