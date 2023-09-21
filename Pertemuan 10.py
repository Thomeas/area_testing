class  Template:
    def cek(self): pass
    def cek_khusus(self): pass
    def info(self): pass

    def go(self):
        self.cek()
        self.cek_khusus()
        self.info()

class Komputer(Template):
    def __init__(self,jenis,ip,stok,harga,kode_pembuatan):
        self.jenis = jenis
        self.ip = ip
        self.stok = stok
        self.harga = harga
        self.kode = kode_pembuatan

    def cek(self):
        print(f"Merek Komputer\t\t: {self.jenis}")
        print(f"IP Address Komputer\t: {self.ip}")
        print(f"Stok Komputer\t\t: {self.stok}")
        print(f"Harga Komputer\t\t: {self.harga}")
    def cek_khusus(self):
        print(f"Kode Komputer\t\t: {self.kode}")
    def info(self):
        if (self.stok < 10):
            print("Stok masih ada !!")
        else:
            print("Stok tidak cukup !!")
        print("="*50)

class Kabel(Template):
    def __init__(self,jenis,ip,stok,harga,panjang):
        self.jenis = jenis
        self.ip = ip
        self.stok = stok
        self.harga = harga
        self.panjang = panjang

    def info(self):
        print("Program input data Kabel berhasil jalan")
    def cek(self):
        print(f"Merek Kabel\t\t: {self.jenis}")
        print(f"Jenis Kabel\t\t: {self.ip}")
        print(f"Stok Kabel\t\t: {self.stok}")
        print(f"Harga Kabel\t\t: {self.harga}")
    def cek_khusus(self):
        print(f"Panjang Kabel\t\t: {self.panjang} m")
    def info(self):
        if (self.stok < 10):
            print("Stok masih ada !!")
        else:
            print("Stok tidak cukup !!")
    
a = Komputer("Asus","192.168.254.104",3,40000000,"78086318577")
a.go()
b = Kabel("Unicron","Kabel Kuningan",11,30000,5)
b.go()