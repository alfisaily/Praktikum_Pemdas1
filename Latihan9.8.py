#Menghitung gaji karyawan
def hitung_gaji_bersih(gaji_pokok, jumlah_karyawan):
    #Menghitung pajak (10% dari gaji pokok)
    pajak = 0.10 * gaji_pokok
    
    #Menghitung tunjangan (20% dari gaji pokok)
    tunjangan = 0.20 * gaji_pokok
    
    #Menghitung gaji bersih
    gaji_bersih = gaji_pokok + tunjangan - pajak
    
    #Menampilkan detail
    print("Gaji pokok:", gaji_pokok)
    print("Tunjangan:", tunjangan)
    print("Pajak:", pajak)
    print("Gaji Bersih:", gaji_bersih)
    print("Gaji total untuk (jumlah-karyawan) karyawan:", gaji_bersih * jumlah_karyawan)    
    
    #Meminta input dari pengguna
    gaji_pokok = float(input("Masukkan gaji pokok karyawan: "))
    jumlah_karyawan = float(input("Masukkan jumlah karyawan: "))
    
    #memanggil fungsi untuk menghitung gaji bersih
    hitung_gaji_bersih(gaji_pokok, jumlah_karyawan)
    