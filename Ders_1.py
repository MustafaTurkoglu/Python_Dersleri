"""
    Temel veri tipleri
TAM SAYILAR:
*Python da tam sayılar için hane kısıtlaması yoktur.Bilgisayarın belleğinin izin verdiği büyüklükte
tam sayılar üretebilirsiniz.
"""

#Örnek tam sayı değişkeni tanımlama
x=10
y=5
z=5

#Standart kütüphanede aşağıdaki gibi operatörler ve sayısal fonksiyonlar kullanılmıştır.

x+y         # x ve ye sayılarını toplar.
x-y         # x sayısından y sayısının çıkarılması.
x*y         # x ile y sayısını çarpar.
x/y         # x sayının y sayısına bölünmesi.
x//y        # x sayısının y sayısına bölünmesiyle elde edilen tam kısmın bulunması.
x%y         # x sayısının y sayısına bölünmesiyle elde edilen kalan kısmın bulunması.
-x          # x sayısının negatif değeri
abs(x)      # x sayısın mutlak değeri
divmod(x,y) # x ile y nin bölümünden elde edilen tam ve kalan kısımların iki tam sayıdan oluşan tuple halinde döndürülmesi.
pow(x,y)    # x in y üssünün alınması. (x**y) ile aynı sonucu verir.
pow(x,y,z)  # pow(x,y)%z değeri
round(x,z)  # x in y haneye yuvarlanması
bin(x)      # On tabanlı x sayısının iki tabanına (binary) dönüştürülmüş olarak gösterilmesi(String)
hex(x)      # On tabanlı x sayısının onaltılık tabanına (hexadecimal) dönüştürülmüş olarak gösterilmesi(String)
int(x)      # x nesnesinin tam sayıya dönüştürülmesi.(yuvarlama işlemi yapılmaz)
#int(s,taban)    # String biçimindeki s değerini tam sayıya çevirir. Taban belirtilmemişse 2 ile 26 arasında bir tam sayı olmaldır.Yoksa hata mesajı üretir.
oct(x)      # On tabanlı x sayısının sekizlik tabanına (octal) dönüştürülmüş olarak gösterilmesi(String)
str(x)      # On tabanlı sayının string haline dönüştürülmüş halini üretir.
# Bütün operatörler ve fonksiyonlarlar teker teker denenip çıktıları gözlenmelidir


"""
Boolean ifadeler:
-Mantıksal değerler sadece 2 yerleşik seçeneğe sahiptir True ve False.
-Bool ifadeler genellikle mantıksal değerlendirmeler sırasında kıyaslama yapmak ve işlemleri yönlendirmek amacıyla kullanılır.
-Özel durumlarda aritmetil işlemler içinde kullanılırlar
"""++
durum=True


"""
Kayan Noktalı Sayılar:
- 14.53 , 0.0  , 5.71 gibi sayılar kayan noktalı(floating point) sayılar olarak tanımlanır.
-Bu sayılarda veri tipi float olarak tanımlanır. küsüratlı bölümün hassaslık derecesi 16 hanedir.
-Küsarat kısmında hassasiyetlik önemli ise decimal kullanarak 28 basamaklı bir hassasiyet elde edilebilir.
-Bu sayılarda işlemler "math" modülünde tanımlıdır.(Kullanılacaksa import etmek gerek)
"""
pi=3.14
import decimal
pi=decimal.Decimal(3.1415926535897932384626433832795028841971693993751058209749445923)#Örnek decimal sayı tanımı


"""
Kompleks Sayılar
- İki bölümnlü sayılardır. Bir bölümü gerçek , diğer bölümü ise sanal kayan noktalı sayılardan oluşur.
"""
ks=14+5.3j