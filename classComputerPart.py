class ComputerPart :
     def __init__(self, pabrikan, nama, jenis, harga):
          self.pabrikan = pabrikan
          self.nama = nama
          self.jenis = jenis
          self.harga = harga

class Processor(ComputerPart):
     def __init__(self, pabrikan, nama, harga, jumlah_core, speed):
          super().__init__(pabrikan, nama,"processor", harga)
          self.jumlah_core = jumlah_core
          self.speed = speed

class RandomAccessMemory(ComputerPart):
     def __init__(self, pabrikan, nama, harga, kapasitas):
          super().__init__(pabrikan, nama, "RAM", harga)
          self.kapasitas = kapasitas

class HardDiskSATA(ComputerPart):
     def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
          super().__init__(pabrikan, nama, "SATA", harga)
          self.kapasitas = kapasitas
          self.rpm =rpm

p = Processor("Intel", "Corei7 7740X",4530000, 4, "4.3GHz" )
m = RandomAccessMemory("V-Gen", "DDR4 SODImm PC19200/2400MHz", 328000, "4GB")
hdd = HardDiskSATA("Seagate", "HDD 2.5 inch ", 295000, "50BG", 7200)

parts = [p, m, hdd]
for part in parts:
     print("{} {} produksi{}" .format(part.jenis, part.nama, part.pabrikan))