# Nama  : Muhammad Fahrul Ardha
# NIM : J0403251138
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree

# KASUS 2: JARINGAN KOMPUTER (ROUTER)
# Algoritma: PRIM

import heapq   # untuk Priority Queue pada algoritma Prim

def prim_router(graph, start, keterangan=""):
    visited = set([start])
    heap = []
 
    for neighbor, weight in graph[start].items():
        heapq.heappush(heap, (weight, start, neighbor))
 
    mst = []
    total_weight = 0
 
    print(f"\n{'='*60}")
    print(f"PRIM — {keterangan}")
    print(f"{'='*60}")
    print(f"\nMulai dari router: {start}")
 
    step = 1
 
    while heap:
        weight, u, v = heapq.heappop(heap)
 
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
 
            print(f"\nStep {step}: Sambungkan {u} → {v} (latensi: {weight} ms)")
            print(f"  Router aktif: {sorted(visited)}")
            step += 1
 
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (w, v, neighbor))
        else:
            print(f"  [SKIP] Koneksi {u}-{v} ({weight} ms) "
                  f"— {v} sudah terhubung")
 
    return mst, total_weight

# Jalankan
graph_router = {
    'RouterA': {'RouterB': 3, 'RouterC': 2},
    'RouterB': {'RouterA': 3, 'RouterD': 5, 'RouterC': 4},
    'RouterC': {'RouterA': 2, 'RouterD': 1, 'RouterB': 4},
    'RouterD': {'RouterB': 5, 'RouterC': 1},
}
 
mst_router, total_router = prim_router(
    graph_router,
    'RouterA',
    "Jaringan Komputer (Router)"
)
 
print(f"\n{'='*60}")
print("HASIL MST — Jaringan Komputer")
print(f"{'='*60}")
print(f"\n  {'Koneksi':<28} {'Latensi (ms)':>14}")
print("  " + "-" * 44)
for u, v, w in mst_router:
    print(f"  {u + ' - ' + v:<28} {w:>12} ms")
print("  " + "-" * 44)
print(f"  {'TOTAL LATENSI MINIMUM':<28} {total_router:>12} ms")
 
nodes_router = set()
for u, v, w in mst_router:
    nodes_router.add(u)
    nodes_router.add(v)
print(f"\n  Router terhubung     : {sorted(nodes_router)}")
print(f"  Jumlah koneksi aktif : {len(mst_router)}")

#JAWABAN ANALISIS
# 1. Kasus apa yang dipilih?
#    Kasus 2: Jaringan Komputer — 4 router (RouterA, B, C, D)

# 2. Algoritma apa yang digunakan?
"""Algoritma PRIM karena:
- Ada satu router utama (RouterA) sebagai gateway/entry point
jaringan. Prim cocok karena bekerja dari satu titik pusat.
- Pola "mulai dari router pusat, sambungkan router terdekat satu
per satu" sesuai dengan cara merancang topologi jaringan nyata."""

# 3. Edge mana saja yang dipilih dalam MST?
"""Tiga koneksi yang dipilih:
1. RouterA - RouterC = 2 ms  ← latensi terkecil dari RouterA
2. RouterC - RouterD = 1 ms  ← latensi terkecil dari {A,C}
3. RouterA - RouterB = 3 ms  ← latensi terkecil ke RouterB"""

# 4. Berapa total bobot MST?
"""Total latensi MST = 2 + 1 + 3 = 6 ms
Dibandingkan total semua koneksi = 3+2+5+1+4 = 15 ms"""

# 5. Mengapa edge tertentu tidak dipilih?
"""- RouterB-RouterC (4 ms):
Menambahkan B-C akan membuat cycle: A-B-C-A.
- RouterB-RouterD (5 ms):
jalur RouterC→RouterD lebih murah (1 ms) dibanding sambungan langsung RouterB-RouterD (5 ms).
"""