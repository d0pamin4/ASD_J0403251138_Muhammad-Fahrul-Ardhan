#=======================================================================================
# Nama    : Muhammad Fahrul Ardhan
# NIM     : J0403251138
# Kelas   : A1
#=======================================================================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# Diskusi dan jelaskan: bagaimana jumlah kombinasi yang dihasilkan.
# ==========================================================
def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return

    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)
#Karena di dalam fungsi ada 2 pilihan cabang (tambah "A" dan tambah "B"), maka kombinasinya mengikuti rumus. Untuk n = 2, hasilnya adalah 2^2 = 4 kombinasi (AA, AB, BA, BB).