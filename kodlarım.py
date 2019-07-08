def toplama(*sayı):
    toplam= 0
    for i in sayı:
        toplam += i
    return toplam

def çarpma(*sayı):
    çarpım= 1
    for i in sayı:
        çarpım *= i
    return çarpım

def bölme(bölünen, bölen):
    if (bölen == 0):
        print("0 ile bölme işlemi tanımsızdır.")
    else :
        return bölünen / bölen

def çıkarma(sayı1,sayı2):
    return(sayı1 - sayı2)

def Toplama_Çarpma(a):
    liste = []
    sayı_adedi = 0
    çıkış = 0
    while True:
        sayı = input("Sayı giriniz (çıkmak için q'ya basın):")

        if(sayı == 'q'):
            break
        try:
            int(sayı)
        except ValueError:
            print("Girdi sayı olmalı.")
            continue

        liste.append(int(sayı))
        sayı_adedi += 1
        if (sayı_adedi >= 2):
            while True:
                giriş = input("Sonucu öğrenmek için t'ye devam etmek için d'ye basınız: ")
                if (giriş == 't'):
                    print("Girdiğiniz sayılar:",liste)
                    if(a == toplama):
                        print("Toplama işleminin sonucu:{}".format(a(*liste)))
                    else:
                        print("Çarpma işleminin sonucu:{}".format(a(*liste)))
                    çıkış = 1
                    break
                elif (giriş == 'd'):
                    break
                else:
                    print("Yanlış bir giriş yaptınız tekrar deneyin.\n")
            if (çıkış):
                break

def Çıkarma_Bölme(b):
    while True:
        sayı1 = input("Birinci sayı: ")
        sayı2 = input("İkinci sayı: ")
        try:
            sayı1=float(sayı1)
            sayı2=float(sayı2)
        except:
            print("İkisi de sayı olmalı, tekrar deneyin")
            continue
        break
    if(b == çıkarma):
        print("{0}-{1} = {2}".format(sayı1, sayı2, b(sayı1, sayı2)))
    else:
        print("{0}/{1} = {2}".format(sayı1, sayı2, b(sayı1, sayı2)))
while True :
    print("""
    <<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>
        İşlemler:
        1:Toplama 
        2:Çıkarma
        3:Çarpma
        4:Bölme
        
    <<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>
   """)
    seçim = int(input("Yapmak istediğiniz işlemi seçin:"))

    if(seçim == 1):
        Toplama_Çarpma(toplama)
    elif(seçim ==2):
        Çıkarma_Bölme(çıkarma)
    elif(seçim ==3):
        Toplama_Çarpma(çarpma)
    elif(seçim ==4):
        Çıkarma_Bölme(bölme)







