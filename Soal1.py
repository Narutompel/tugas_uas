mahasiswa = [
    {
        "nama": "David Nyoman",
        "nimMahasiswa": "42130001",
        "Jurusan": "Teknik Informatika"
    },
    {
        "nama": "Made Mahendrata",
        "nimMahasiswa": "42130002",
        "Jurusan": "Teknik Informatika"
    },
    {
        "nama": "Jaya Kusugi",
        "nimMahasiswa": "42130003",
        "Jurusan": "Teknik Informatika"
    }

]

print("Silahkan Pilih daftar nama mahasiswa berikut di bawah ini : ")
print("1. David Nyoman")
print("2. Made Mahendrata")
print("3. Jaya Kusugi")

input = input("\nMasukkan Angka 1-3 :")


if input == '1':
    print("Nama = ", mahasiswa[0]['nama'])
    print("Nim = ", mahasiswa[0]['nimMahasiswa'])
    print("Jurusan = ", mahasiswa[0]['Jurusan'])

elif input == '2':
    print("Nama = ", mahasiswa[1]['nama'])
    print("Nim = ", mahasiswa[1]['nimMahasiswa'])
    print("Jurusan = ", mahasiswa[1]['Jurusan'])
else:
    print("Nama = ", mahasiswa[2]['nama'])
    print("Nim = ", mahasiswa[2]['nimMahasiswa'])
    print("jJurusan = ", mahasiswa[2]['Jurusan'])
