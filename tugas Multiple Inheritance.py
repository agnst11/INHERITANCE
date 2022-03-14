# Multiple Inheritance
def harga_prdk(uang):
    x = str(uang)
    if len(x) <= 3:
        return "Rp." + x
    else:
        a = x[:-3]
        b = x[-3:]
        return harga_prdk(a) + '.' + b


class ComputerPart1():
    def __init__(self, pabrikan, nama):
        self.pabrikan = pabrikan
        self.nama = nama


class ComputerPart2():
    def __init__(self, harga):
        self.harga = harga


class Processor(ComputerPart1, ComputerPart2):
    def __init__(self, pabrikan, nama, harga):
        ComputerPart1.__init__(self, pabrikan, nama)
        ComputerPart2.__init__(self, harga)

    def cetak(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga : {harga_prdk(self.harga)}\n")


class RandomAccessMemory(ComputerPart1, ComputerPart2):
    def __init__(self, pabrikan, nama, harga):
        ComputerPart1.__init__(self, pabrikan, nama)
        ComputerPart2.__init__(self, harga)

    def cetak(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga : {harga_prdk(self.harga)}\n")


class HardDiskSATA(ComputerPart1, ComputerPart2):
    def __init__(self, pabrikan, nama, harga):
        ComputerPart1.__init__(self, pabrikan, nama)
        ComputerPart2.__init__(self, harga)

    def cetak(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga : {harga_prdk(self.harga)}")


p = Processor('Intel', "Core i5 7740X", 1000000)
ram = RandomAccessMemory('V-Gen', 'DDR4 SODIMM PC19200/2400 MHz', 475000)
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000)

parts = [p, ram, hdd]
print("\n\t\t\tMULTIPLE COMPUTER PART\n")
for part in parts:
    part.cetak()

