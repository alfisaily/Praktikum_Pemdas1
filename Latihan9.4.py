#Menampilkan status lulus
nama = "Andi"
umur = 21
program_studi = "Sistem Informasi"
jenis_kelamin = "Laki-laki"
tinggi = 170
kelas = "SI-3B"
lulus = False

nama = "Budi"
umur = 22
tinggi = 175
kelas = "DI-3C"
lulus = True

print("Nama:", nama)
print("Umur:", umur, "tahun")
print("Tinggi badan:", tinggi, "cm")
print("Program Studi:", program_studi)
print("kelas:", kelas)
print("jenis Kelamin:", jenis_kelamin)

if lulus:
    print("status: Alumni")
else:
    print("Status: Mahasiswa aktif")