# kendi oluşturduğumuz modülü import ederiz.
import converterofTemperature

# from converterofTemperature import celciusToFahrenheit, fahrenheitToCelcius
#böyle import yaparsak kullandığımız yerde modül adını yazmadan direkt fonksiyonları kullanabiliriz.

# (-50,+101) arası celcius değerleri fahrenheite çevir, terminale yaz.
# (0,+201) arası fahrenheit değerleri celciusa çevir, terminale yaz.
for celcius in range(-50,101,5):
    print(f"{celcius:>3} celsius = {converterofTemperature.celciusToFahrenheit(celcius):5.6} fahrenheit")
print("\n")
for fahrenheit in range(0,201,5):
    print(f"{fahrenheit:>3} fahrenheit = {converterofTemperature.fahrenheitToCelcius(fahrenheit):5.3} celcius")
