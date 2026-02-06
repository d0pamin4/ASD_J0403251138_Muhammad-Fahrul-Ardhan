#====================================================
#Praktikum 1 : Konsep ADT dan file handling
#Latihan Dasar : Membaca seluruh isi file data
#====================================================

print("Membuka file dalam satu string")
with open("data_mahasiswa.txt","r", encoding= "UTF-8") as file:
    isi_file = file.read() #mengambil data dan menyimpan semua data dalam 1 variabel

print(isi_file)

print(type(isi_file))

print("=================================================")
print("membuka file per baris")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding='utf-8') as file:
    for baris in file:
        jumlah_baris = jumlah_baris+ 1
        baris = baris.strip()# menghilanngkan karakter baris baru
        print("baris ke-", jumlah_baris)
        print("isinya:",baris)
\
print("=================================================")
#parsing baris menjadi data satuan
with open("data_mahasiswa.txt", "r", encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip('')
        nim, nama, nilai = baris.split(',')
        print("nim", nim, "nama", nama, "nilai", nilai )

print("=================================================")
data_list = [] 
with open("data_mahasiswa.txt", "r", encoding='utf-8') as file:
    
    for baris in file:
        baris = baris.strip('')
        nim, nama, nilai = baris.split(',')
        print("nim", nim, "nama", nama, "nilai", nilai )
        data_list.append([nim,nilai,int(nilai)])
print("=================================================")

print("menampilkan data list")
print(data_list)
print('record ke 1', data_list[0])


print("=================================================")
data_dict = {}

with open("data_mahasiswa.txt", "r", encoding = "utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_dict[nim]= {
            "nama": nama,
            "nilai":int(nilai)
        }
print("menampilkan data dictionary")
print(data_dict)