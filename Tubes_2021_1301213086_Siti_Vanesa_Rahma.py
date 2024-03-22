#fungsi membaca file teks
def skorpemain(filename):
    buka_file = open (filename,"r")#membuka file lalu dibaca secara keseluruhan
    baca_file = buka_file.readlines()#membaca isi buka_file secara satu persatu lalu disimpan dalam 
    buka_file.close()#menutup file teks
    #nama=baca_file[0].replace("\n","").split("\t")
    pemain_golf=[]#membuat list kosong
    #pengulangan untuk memproses baris perbaris yang sudah dibaca
    for baris in baca_file:
        baris_file = baris.replace("\n","").split()
        #perulangan untuk merubah nilai dari index string menjadi angka/integer
        for y in range(len(baris_file)):
            PAR=5
            if baris_file[y]=="PAR":
                baris_file[y]=PAR+0
            elif baris_file[y]=="QD":
                baris_file[y]=PAR+4
            elif baris_file[y]=="TP":
                baris_file[y]=PAR+3
            elif baris_file[y]=="DB":
                baris_file[y]=PAR+2
            elif baris_file[y]=="ACE":
                baris_file[y]=PAR+1
            elif baris_file[y]=="BG":
                baris_file[y]=PAR+1
            elif baris_file[y]=="BR":
                baris_file[y]=PAR+(-1)
            elif baris_file[y]=="EG":
                baris_file[y]=PAR+(-2)
            elif baris_file[y]=="AL":
                baris_file[y]=PAR+(-3)
            elif baris_file[y]=="CN":
                baris_file[y]=PAR+(-4)
        skor_pemain = dict()
        for i in range (len(baris_file)):
            nama=baris_file[0]
            skor_pemain[nama]= baris_file[1:]
        pemain_golf.append(skor_pemain)
    return pemain_golf

#fungsi mencari pemenang
def pemenang(list_pemain):
    jumlah=[]
    for element in list_pemain:
        for k, v in element.items():
            jumlah.append(sum(v))
    #print(jumlah)
    #print(min(jumlah))
    juara=jumlah.index(min(jumlah))+1
    print("Peserta yang menang adalah peserta no", juara)
    #print(juara)
    return juara

#fungsi mencari nilai rata-rata
def rerata (list_nilai):
    nilai_akhir=[]
    for element in list_nilai:
        for k, v in element.items():
            nilai_akhir.append(sum(v))
    #print(nilai_akhir)
    #print(sum(nilai_akhir))
    #print(len(nilai_akhir))
    rata2=sum(nilai_akhir)/len(nilai_akhir)
    #print(rata2)
    print("Rata-rata skor pemain adalah ",rata2)
    return rata2

#main program
nama_file = ("Happy_Golf.txt")
skorpemain(nama_file)
print("pemain_golf","=",skorpemain(nama_file))
pemenang(skorpemain(nama_file))
rerata(skorpemain(nama_file))
