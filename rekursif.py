print("mencari deret fibonancci dengan menggunakan rekursif") 
def fibonacci (n):
  if n < 1:
    return [n]

  listSebelumN = fibonacci(n - 1)
  angka1 = listSebelumN[-2] if len(listSebelumN) > 2 else 0
  angka2 = listSebelumN[-1] if len(listSebelumN) > 2 else 1

  print('listSebelumN', listSebelumN)
  print(f'angka1: {angka1}, angka2: {angka2}')

 
  return listSebelumN + [angka1 + angka2] 
panjang = int(input('Masukkan panjang deret:'))
print(fibonacci(panjang - 1))
