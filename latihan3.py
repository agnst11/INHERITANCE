#Hierarchical Inheritance

#CLASS parent
class Induk:
    def fungsiinduk(self):
        print('Fungsi pada parent class.')
        
#class turunan 1
class Anak1(Induk):
    def fungsianak1(self):
        print('Fungsi pada anak 1.')
        
#class turunan 2
class Anak2(Induk):
    def fungsianak2(self):
        print('Fungsi pada anak 2.')
        
a1=Anak1()
a2=Anak2()

a1.fungsiinduk()
a1.fungsianak1()

a2.fungsiinduk()
a2.fungsianak2()
    
    