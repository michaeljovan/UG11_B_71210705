def hitung(huruf) : 
    jumlahhuruf = len(huruf) 
    return jumlahhuruf * 2 / 3 
huruf = input("Masukkan kalimat untuk dihitung : ")
print(int(hitung(huruf)))