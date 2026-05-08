#=======================================================================================
# Nama    : Muhammad Fahrul Ardhan
# NIM     : J0403251138
# Kelas   : A1
#=======================================================================================

"""Pak Budi adalah seorang manager sumber daya manusia di suatu perusahaan. Ia
saat ini harus menseleksi pelamar kerja berdasarkan skor tes potensi akademik
mereka. Skor tersebut disajikan dalam bentuk list dengan rentang nilai 0 - 100.
Berikut adalah data hasil tes potensi akademik yang tersedia:"""
nilai = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# 1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah
# skor lima kandidat tersebut dari yang paling tinggi hingga terendah.


# Implementasi Bubble Sort Descending
def bubbleSort(alist):
    exchanges = True

    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]<alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1

bubbleSort(nilai)
print(nilai[:5]) # Print 5 kandidat dengan nilai tertinggi

# 2. Kandidat berapa saja yang lolos?
print("Kandidat yang lolos adalah kandidat dengan skor:", nilai[:5])