# Multilevel Inheritance
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

    def Tampil(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"harga :  {harga_prdk(self.harga)}\n")


class RandomAccessMemory(Processor):
    def __init__(self, pabrikan, nama, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def Tampil(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"harga :  {harga_prdk(self.harga)}\n")


class HardDiskSATA(RandomAccessMemory):
    def __init__(self, pabrikan, nama, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def Tampil(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"harga :  {harga_prdk(self.harga)}")


p = Processor('Intel', 'Core i7 7740X', 10000000)
ram = RandomAccessMemory('V-Gen', 'DDR4 SODIMM PC19200/2400 MHz', 328000)
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000)

parts = [p, ram, hdd]
print("\n\t\t\tMULTILEVEL COMPUTER PART\n")

for part in parts:
    part.Tampil()
print("")
