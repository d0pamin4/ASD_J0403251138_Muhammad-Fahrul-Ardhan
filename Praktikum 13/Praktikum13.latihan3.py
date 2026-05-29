# Nama  : Muhammad Fahrul Ardhan
# NIM : J0403251138
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree

import heapq 

graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 

def prim(graph, start): 
    visited = set([start]) 
    
    edges = [] 
    
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 
    
    mst = [] 
    total_weight = 0 
    
    while edges:
        weight, u, v = heapq.heappop(edges) 
        
        if v not in visited: 

            visited.add(v) 

            mst.append((u, v, weight)) 
            total_weight += weight 

            for neighbor, w in graph[v].items(): 
                
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 
    
    return mst, total_weight 

mst, total = prim(graph, 'A') 

print("Minimum Spanning Tree:") 

for edge in mst: 
    print(edge) 

print("Total bobot =", total)

#JAWABAN ANALISIS

# 1. Node awal apa yang digunakan?
"""Node awal yang digunakan adalah 'A'.
Pada algoritma Prim, pemilihan node awal BEBAS — tidak mempengaruhi
hasil akhir MST (total bobot tetap sama), namun bisa mempengaruhi
urutan edge yang dipilih selama proses berjalan."""

# 2. Edge mana yang dipilih pertama kali?
"""Edge pertama yang dipilih adalah A-C dengan bobot 2.
Alasannya: dari node awal A, terdapat 3 kandidat edge:
 - A-B (bobot 4)
 - A-C (bobot 2)  ← terkecil → dipilih
 - A-D (bobot 5)
Priority queue (min-heap) secara otomatis mengembalikan edge
dengan bobot terkecil, yaitu A-C = 2."""

# 3. Bagaimana Prim menentukan edge berikutnya?
"""Setiap kali sebuah node baru ditambahkan ke MST, semua edge dari
node tersebut ke node yang BELUM dikunjungi dimasukkan ke priority queue.
Priority queue selalu mengembalikan edge dengan bobot TERKECIL duluan."""

# 4. Berapa total bobot MST yang dihasilkan?
"""Total bobot MST = 2 (A-C) + 1 (C-D) + 3 (D-B) = 6
Sama dengan hasil Kruskal pada graph yang sama — keduanya
menghasilkan MST dengan total bobot minimum yang identik."""

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
"""Kruskal: memilih edge terkecil dari semua edge
prim : mengembangkan tree dari satu node awal"""
