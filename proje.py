class Sozluk:
    def __init__(self):
        with open('proje.txt', 'r') as dosya:
            satirlar = dosya.readlines()
        self.sozluk = {}
        for satir in satirlar:
            kelime, tanim = satir.strip().split(":")
            self.sozluk[kelime]=tanim
        self.kelime_defteri = []
    
    def cumleEkle(self):
        kelime = input("Hakkinda cumle eklemek istediginiz kelimeyi giriniz:")
        kelime=kelime.capitalize()
        if kelime not in self.sozluk:
            print("Aradiginiz kelime bulunamadi!\n Eger kelimeyi sozluge eklemek istiyorsaniz kelime ekle kismina gidebilirsiniz.")
        else:
            with open('proje.txt','r') as dosya:
                satirlar=dosya.readlines()
            with open('proje.txt','w') as dosya:
                for satir in satirlar:
                    if kelime in satir:
                        cumle=input("Eklemek istediginiz cumleyi giriniz:")
                        dosya.write(satir.strip() + f",ornek cumle = {cumle}\n")
                        print(f"'{cumle}' cümlesi,{kelime} kelimesine eklendi.")   
                    else:
                        dosya.write(satir)
                    
    def yorumEkle(self):
        kelime = input("Hakkinda yorum eklemek istediginiz kelimeyi giriniz:")
        kelime=kelime.capitalize()
        if kelime not in self.sozluk:
            print("Aradiginiz kelime bulunamadi!\n Eger kelimeyi sozluge eklemek istiyorsaniz kelime ekle kismina gidebilirsiniz.")
        else:
            with open('proje.txt','r') as dosya:
                satirlar=dosya.readlines()
            with open('proje.txt','w') as dosya:
                for satir in satirlar:
                    if kelime in satir:
                        yorum=input("Eklemek istediginiz yorumu giriniz:")
                        dosya.write(satir.strip() + f",yorum = {yorum}\n")
                        print(f"'{yorum}' yorumu,{kelime} kelimesine eklendi.")   
                    else:
                        dosya.write(satir)        
    
    def kelime_bilgi_goster(self):
        kelime=input("lutfen aratmak istediginiz kelimeyi giriniz:")
        kelime=kelime.capitalize()
        if kelime in self.sozluk:
            print(f"{kelime} kelimesi için bilgiler:{self.sozluk[kelime]}")  
def main():
    sozluk=Sozluk()
    #sozluk.kelime_bilgi_goster()
    #sozluk.cumleEkle()
    #sozluk.yorumEkle()
    
main()
