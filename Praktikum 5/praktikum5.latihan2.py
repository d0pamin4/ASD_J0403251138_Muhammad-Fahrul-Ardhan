#=======================================================================================
# Nama    : Muhammad Fahrul Ardhan
# NIM     : J0403251138
# Kelas   : A1
#=======================================================================================

# ==========================================================
# Latihan 2: Tracing Rekursi
# Diskusi dan jelaskan: Mengapa output 'Keluar' muncul terbalik?
# ==========================================================
def countdown(n):
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)

countdown(3)
#Saat countdown(3) dijalankan, ia mencetak Masuk: 3 dan menunda baris print("Keluar:", n) untuk memanggil countdown(2). Proses ini terus berlanjut ke dalam hingga mencapai base case yang mencetak Selesai.