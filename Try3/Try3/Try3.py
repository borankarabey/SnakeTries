import math
import random as rnd

##### GİTHUB KAYIT ŞEKLİ 'OTOKOÇ BAŞVURU' #####
# ana menü = giriş ekranı
# kullanıcı adı-şifre kontrolu
## kullanıcı bulunuyorsa giriş
## kullanıcı bulunmuyorsa yeni üye ekranı
# ikinci ekran = araç menüsü (arabalar, kamyonlar, motorsikletler) ve ana menüye dönme seçeneği
# ararçların menülerinde 10-5-5 halinde araçların markaları ve ana menüye dönme seçeneği ve bir önceki dönme seçeneği
# araç seçildiğinde araç hakkında bilgiler(isim, renk, model, motor gücü) ve bir önceki dönme seçeneği ve ana menüye dönme seçeneği
# araç bilgi ekranında sepete ekleme seçeneği ve ana menüye dönme seçeneği
# ödeme ekranı ve ana menüye dönme seçeneği


# toplam ekran sayısı = 9+20 {giriş, şifre, üye, araçlar, araba, kamyon, moto, hepsine ayrıntı ekranı, sepet, ödeme}



class araclar:
    
    class araba:

        def __init__(self, name, idnumber):

            self.name = name
            self.idnumber = idnumber




