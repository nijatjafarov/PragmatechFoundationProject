tarix = input("Bugunun tarixini daxil edin: ")
tarixList = tarix.split(".")

gun = int(tarixList[0])
ay = int(tarixList[1])
il = int(tarixList[2])

aylarinGunleri = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def tarixHesablama(gun, ay, il):
  if il % 4 != 0 and ay == 2 and gun == 28:
    gun = 1
  elif gun == 31 and ay == 12:
    gun, ay = 1, 1
    il += 1
  elif ay > 12 or ay < 1 or gun > aylarinGunleri[ay - 1]:
    return "Ozunden tarix uydurma"
  elif gun == aylarinGunleri[ay - 1]:
    gun = 1
    ay += 1
  else:
    gun += 1

  return str(gun) + "." + str(ay) + "." + str(il)


print(tarixHesablama(gun, ay, il))
