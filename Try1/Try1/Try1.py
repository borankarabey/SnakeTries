import random

torba = {}

def takim_ekle(isim, numara):
  global torba
  if not isim in torba.keys():
    torba[isim] = numara
    print(" Yeni takım eklendi.")
  else: print(" Böyle bir takım zaten var.")

def takim_sil(isim):
  global torba
  try:
    del torba[isim]
    print(" Takım silindi.")
  except KeyError:
    print(" Takım bulunamadı.")

def isim_guncelle(isim, yeni_isim):
  global torba
  if isim in torba.keys():
    if not yeni_isim in torba.keys():
      torba[yeni_isim] = torba[isim]
      del torba[isim]
      print(" Takım güncellendi.")
    else: print(" Yeni takım isminde zaten bir kullanıcı mevcut.")
  else: print(" Takım bulunamadı.")

def numara_guncelle(isim, yeni_numara):
    global torba
    if isim in torba.keys():
        torba[isim] = yeni_numara
        print(" Numara güncellendi.")
    else: print(" Kişi bulunamadı.")

def rastgele_takim_sec():
  isim = random.choice(list(torba.keys()))
  return isim, torba[isim]

def takimlari_goruntule():
  global torba
  if not len(torba) == 0:
    print(" Torba:\n")
    i = 1
    for key,value in torba.items():
      print(f"{i})\n\tİsim: {key}\n\tNumara: {value}")
      i += 1
    return
  print(" Torba Boş")

def main():
  global torba

  menu = '''
   _________________________
  | 1: Takim ekle           |
  | 2: Takim Sil            |
  | 3: İsim Güncelle        |
  | 4: Numara Güncelle      |
  | 5: Rastgele Takim Seç   | 
  | 6: Takimlari Görüntüle  |
  | q: Çıkış Yap            |
   _________________________
  '''
  print(menu)
  while True:
    secim = input(" Lütfen seçim yapınız: ")
    print("*"*50+"\n")
    if secim == "1":
      isim = input(" Yeni takim ismi giriniz: ")
      numara = input(" Numarayı giriniz: ")
      takim_ekle(isim,numara)

    elif secim == "2":
      isim = input(" Silmek istediğiniz takimin ismini giriniz: ")
      takim_sil(isim)

    elif secim == "3":
      isim = input(" Değiştirmek istediğiniz ismi giriniz: ")
      yeni_isim = input(" Yeni ismi giriniz: ")
      isim_guncelle(isim,yeni_isim)

    elif secim == "4":
      isim = input(" Numarasını değiştirmek istediğiniz takimin ismini giriniz: ")
      yeni_numara = input(" Yeni numarayı giriniz: ")
      numara_guncelle(isim,yeni_numara)
    
    elif secim == "5":
      isim, numara = rastgele_takim_sec()
      print(f"\n\tİsim: {isim}\n\tNumara: {numara}")
    
    elif secim == "6":
      takimlari_goruntule()
    
    elif secim == "q":
      break
    
    else: print(" Geçersiz seçim yaptınız. Lütfen tekrar deneyiniz")
    print(menu)


main()