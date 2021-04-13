"""
value = True
while value:
    parola = input("Lütfen bir parola belirleyiniz:")
    if not parola:
        print("Bu alan boş bırakılamaz")
    elif len(parola) not in range(3, 9):
        print("Parolanız 3 karakterden az 8 karaktarden fazla olamaz")
    else:
        print("Parolanız başarıyla oluşturuldu!")
        value = False
"""
while True: # sonsuz bir döngü oluşturduk
  parola = input("paralo belirleyiniz") # kullanıcıdan parola istedik
  if not parola: # boş bırakmaya çalışırsa uyarı verdik 
      print("boş geçilemez")
  elif len(parola) in range(3, 9): # 3 ve 8 karakter arasındaysa yeni parolanız diyip parolasını yazdırdık
      print("yeni parolanız", parola)
      break

  else: # parola 8'den uzun 3'den kısaysa hata verdirip tekrar başa döndürdük 
      print("parolanız 8 karakterden uzun ya da 3 karakterden kısa olmamalı")