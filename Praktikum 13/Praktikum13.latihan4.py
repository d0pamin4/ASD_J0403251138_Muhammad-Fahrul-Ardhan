# Nama  : Muhammad Fahrul Ardha
# NIM : J0403251138
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree

import heapq   # untuk Priority Queue pada algoritma Prim

#Representasi Weighted Graph
graph_gedung = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1},
}

#Tampilkan Data Awal (semua kemungkinan koneksi)
print("=" * 60)
print("STUDI KASUS: JARINGAN KABEL ANTAR GEDUNG KAMPUS")
print("=" * 60)
print("\nData semua kemungkinan koneksi kabel:")
print(f"  {'Koneksi':<28} {'Biaya (juta Rp)':>16}")
print("  " + "-" * 46)
 
# Gunakan set untuk menghindari duplikasi (karena undirected)
ditampilkan = set()
total_semua = 0
for gedung, koneksi in graph_gedung.items():
    for tujuan, biaya in koneksi.items():
        key = tuple(sorted([gedung, tujuan]))
        if key not in ditampilkan:
            ditampilkan.add(key)
            label = f"{gedung} - {tujuan}"
            print(f"  {label:<28} {biaya:>16}")
            total_semua += biaya
 
print(f"\n  Total biaya jika SEMUA kabel dipasang : {total_semua} juta Rp")
print(f"  (Ini adalah biaya boros karena ada cycle)")

#Implementasi Algoritma Prim
def prim_gedung(graph, start):
    visited = set([start])   # gedung yang sudah terhubung ke jaringan
 
    # Priority queue berisi kandidat kabel yang bisa dipasang
    # Format: (biaya, gedung_asal, gedung_tujuan)
    heap = []
    for tetangga, biaya in graph[start].items():
        heapq.heappush(heap, (biaya, start, tetangga))
 
    mst = []
    total_weight = 0
 
    print(f"\n{'='*60}")
    print(f"PROSES PRIM (Mulai dari: {start})")
    print(f"{'='*60}")
    print(f"\nTahap awal: {start} sudah terhubung ke jaringan.")
    print(f"Kandidat kabel pertama dari {start}:")
    for tetangga, biaya in graph[start].items():
        print(f"  {start} - {tetangga} = {biaya} juta Rp")
 
    step = 1
 
    while heap:
        biaya, u, v = heapq.heappop(heap)
 
        if v not in visited:
            # Gedung v belum terhubung → kabel ini aman dipasang
            visited.add(v)
            mst.append((u, v, biaya))
            total_weight += biaya
 
            print(f"\nLangkah {step}: Pasang kabel {u} → {v}")
            print(f"  Biaya kabel    : {biaya} juta Rp")
            print(f"  Gedung terhubung sekarang: {sorted(visited)}")
            step += 1
 
            # Daftarkan kandidat kabel baru dari gedung yang baru terhubung
            for tetangga, b in graph[v].items():
                if tetangga not in visited:
                    heapq.heappush(heap, (b, v, tetangga))
                    print(f"  → Kandidat baru: {v} - {tetangga} = {b} juta Rp")
        else:
            # Gedung v sudah terhubung → memasang kabel ini akan membuat loop
            print(f"\n  [SKIP] Kabel {u}-{v} ({biaya} juta Rp) "
                  f"dilewati — {v} sudah terhubung")
 
    return mst, total_weight

#Tampilkan Hasil
# Mulai dari GedungA sebagai titik sentral (gedung utama/server room)
kabel_terpilih, total_biaya = prim_gedung(graph_gedung, 'GedungA')
 
print("\n" + "=" * 60)
print("REKOMENDASI JARINGAN KABEL (MST)")
print("=" * 60)
print("\nKabel yang harus dipasang:")
print(f"  {'No':<4} {'Koneksi':<30} {'Biaya':>12}")
print("  " + "-" * 48)
for i, (u, v, w) in enumerate(kabel_terpilih, 1):
    print(f"  {i:<4} {u + ' - ' + v:<30} {w:>10} juta Rp")
print("  " + "-" * 48)
print(f"  {'TOTAL BIAYA MINIMUM':<34} {total_biaya:>10} juta Rp")
 
# Hitung penghematan dibandingkan memasang semua kabel
penghematan = total_semua - total_biaya
print(f"\n  Total jika semua kabel dipasang : {total_semua} juta Rp")
print(f"  Total dengan MST                : {total_biaya} juta Rp")
print(f"  Penghematan                     : {penghematan} juta Rp "
      f"({penghematan/total_semua*100:.1f}%)")
 
# Verifikasi MST
all_nodes = set()
for u, v, w in kabel_terpilih:
    all_nodes.add(u)
    all_nodes.add(v)
print(f"\n  Semua gedung terhubung : {sorted(all_nodes)}")
print(f"  Jumlah kabel dipasang  : {len(kabel_terpilih)}")
print(f"  MST Valid (n-1 edge)   : {len(kabel_terpilih) == len(all_nodes) - 1}")

#JAWABAN ANALISIS
# 1. Algoritma apa yang digunakan?
"""Algoritma PRIM digunakan pada latihan ini.
Alasan pemilihan Prim untuk kasus jaringan kabel kampus:
Kasus ini bersifat NODE-CENTRIC — kita mulai dari satu gedung utama dan memperluas
jaringan secara bertahap ke gedung-gedung sekitarnya."""

# 2. Edge mana saja yang dipilih?
"""Tiga kabel yang dipilih untuk MST:
1. GedungA - GedungC = 2 juta Rp
2. GedungC - GedungD = 1 juta Rp
3. GedungD - GedungB = 3 juta Rp"""

# 3. Berapa total biaya minimum?
#    Total biaya minimum = 2 + 1 + 3 = Rp6 juta

# 4. Mengapa MST cocok digunakan pada kasus ini?
"""Kita ingin semua gedung terhubung, bukan mencari rute terpendek
antar dua gedung tertentu dan menghilangkan semua loop yang bisa memberi redudandsi"""

