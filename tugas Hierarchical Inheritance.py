# Hierarchical Inheritance
def harga_prdk(uang):
    x = str(uang)
    if len(x) <= 3:
        return "Rp." + x
    else:
        a = x[:-3]
        b = x[-3:]
        return harga_prdk(a) + '.' + b


class ComputerPart:
    def __init__(self, pabrikan, nama, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga


class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def cetak(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga : {harga_prdk(self.harga)}")


class RandomAccessMemory(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas

    def cetak(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Kapasitas : {self.kapasitas}")
        print(f"Harga : {harga_prdk(self.harga)}")


class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas
        self.rpm = rpm

    def cetak(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Kapasitas : {self.kapasitas}")
        print(f"RPM : {self.rpm}")
        print(f"Harga : {harga_prdk(self.harga)}")


p = Processor('Intel', 'Corei7 7740X', 10000000)
ram = RandomAccessMemory("V-Gen", "DDR4 SODImm PC19200/2400MHz", 328000, "4GB")
hdd = HardDiskSATA("Seagate", "HDD 2.5 inch ", 295000, "50BG", 7200)

parts = [p, ram, hdd]
print("\n\t\t\tMULTILEVEL COMPUTER PART")
print()
for part in parts:
    part.cetak()
    print("")
