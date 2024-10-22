#Menampilkan sewa angkutan
def hitung_biaya_sewa(jarak):
    if jarak <= 1:
        biaya = 4500 #Harga untuk 1 km pertama
    else:
        #Harga untuk 1 km pertama + (jarak - 1) * harga per km selanjutnya
        biaya = 4500 + (jarak - 1) *2000
        
        return biaya
    
    #Meminta input dari pengguna
    jarak = float(input("MAsukkan jarak yang ditempuh (dalam km): "))
    
    #Menghitung biaya sewa
    biaya_sewa = hitung_biaya_sewa(jarak)
    
    #menampilkan hasil
    print("Biaya sewa angkutan untuk jarak {jarak} km adalah: Rp.{biaya_sewa:.2f}")