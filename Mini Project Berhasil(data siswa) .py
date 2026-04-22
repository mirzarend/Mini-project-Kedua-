kalimat = input("masukkan kata acak :")

def analisis_kalimat(kata) :
  hurufBesar = kata.upper()
  hurufKecil = kata.lower()
  kapital = kata.title()
  mencariHuruf = "a" in kata
  
  hasil = (hurufBesar,hurufKecil,kapital, mencariHuruf)
  return hasil

hasil = analisis_kalimat(kalimat)
print(f"Huruf Besar = {hasil[0]}")
print(f"Huruf Kecil = {hasil[1]}")
print(f"Kapital Tiap Kata = {hasil[2]}")
print(f"Apakah ada huruf a di kalimat?= {"Ya" if hasil[3] else "tidak"}")
  