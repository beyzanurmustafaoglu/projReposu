class Sozluk:
    def __init__(self):
        with open('proje.txt', 'r') as dosya:
            satirlar = dosya.readlines()
        self.sozluk = {}
        for satir in satirlar:
            kelime, tanim = satir.strip().split(":")
            self.sozluk[kelime]=tanim
        self.kelime_defteri = []
    
    def cumleEkle():
        
    def yorumEkle():
    
    def kelime_bilgi_goster(self):
        kelime=input("lutfen aratmak istediginiz kelimeyi giriniz:")
        if kelime in self.sozluk:
            print(f"{kelime} kelimesi için bilgiler:{self.sozluk[kelime]}")  
def main():
    sozluk=Sozluk()
    sozluk.kelime_bilgi_goster()
    
main()
