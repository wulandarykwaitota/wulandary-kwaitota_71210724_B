class Karyawan:

    _nama =  None
    _umur = None
    _jenisKelamin = None
    _upahPerhari = None

    def __init__(self,Nama=None,Umur=None,JenisKelamin=None,UpahPerhari=None):
        self._nama = Nama
        self._umur = Umur
        self._jenisKelamin = JenisKelamin
        self._upahPerhari = UpahPerhari
        
    def printInfo(self):
        print("============INFO============")
        print("Nama           : ", self.getNama())
        print("Umur           : ", self.getUmur())
        print("Jenis Kelamin  : ", self.getJenisKelamin())
        print("Upah Per Hari  : ",self.getUpahPerhari())

    def getNama(self):
        return self._nama

    def getUmur(self):
        return self._umur

    def getJenisKelamin(self):
        return self._jenisKelamin

    def setJenisKelamin(self,JenisKelamin):
        self.jenisKelamin = JenisKelamin 
        return self._jenisKelamin
    
              
    def getUpahPerhari(self):
        return self._upahPerhari

    def setUpahPerhari(self,UpahPerHari):
        self._upahPerhari = UpahPerHari
    
    def hitungGajiBulanan(self,gaji):
        if self.hitungGajiBulanan == None:
            print("ERROR! Upah Per Hari belum di input")
        else:
            a = gaji*self._hitungGajiBulanan
            print("gaji ", self._hitungGajiBulanan, "liter")
            print("Total Gaji Bulan ini :",a )


if __name__ == "__main__":
    orang1 = Karyawan("Haniif", 90)
    orang1.printInfo()
    orang2 = Karyawan("Sindu", 190)
    orang2.setJenisKelamin("Laki-laki")
    orang2.setUpahPerhari(30000)
    orang2.printInfo()
    orang1.hitungGajiBulanan(28)
    orang2.hitungGajiBulanan(30)