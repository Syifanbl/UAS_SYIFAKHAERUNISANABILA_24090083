
mahasiswa = []
def tampilkan_data():
    print("\nData Mahasiswa:")

    
while True:
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")

    mahasiswa.append({'nim': nim, 'nama': nama})

    tambah_lagi = input("Ingin tambah data lagi? (ya/tidak): ") == 'tidak'
    if tambah_lagi != "ya":
        break

for data in mahasiswa_data:
    print(f"NIM: {data['NIM']}, Nama: {data['Nama']}")

tampilkan_data()

print("\nProgram selesai.")


