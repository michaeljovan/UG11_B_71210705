def sisipkt(ka, ksip, ind) : 
    proses = ka[:ind-1] + ksip + ka[ind-1:]
    print(proses)

kalawal = input("Masukkan kalimat awal :  ") 
katsisip = input("Masukkaan kata untuk disisipkan : ") 
index = int(input("Masukan indek : ")) 

sisipkt(kalawal, katsisip, index)