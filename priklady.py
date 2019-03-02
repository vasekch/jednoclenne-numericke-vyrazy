from random import randint


a = 1
b = 1

while True:
  print('-' * 50)
  varianta = randint(1, 3)

  if varianta == 1:
      # example 74 * 8
      a = randint(10, 99)
      b = randint(1,9)

  elif varianta == 2:
      # example 345 * 2
      a = randint(100, 999)
      b = randint(1,9)

  elif varianta == 3:
      # example (23 + 18) * 19
      a = '({0} + {1})'.format(randint(10, 99), randint(10, 99))
      b = randint(1,99)

  else:
    print("ERROR: Neznama varianta", varianta)

  priklad = '{0} * {1}'.format(a, b)
  print(priklad)
  vysledek = eval(priklad)
  vysledky = []
  while len(vysledky) < 4:
      vys = vysledek + randint(-3, 3) * 10
      if vys not in vysledky:
          vysledky.append(vys)

  # vetri spravny vysledek do variant, pokud tam jeste neni
  if vysledek not in vysledky:
      vysledky[randint(0,3)] = vysledek

  print('  a) {0}   b) {1}   c) {2}   d) {3}      x) skoncit'.format(*vysledky))

  vstup = input('Zadej vstup: ')
  while vstup not in ('a', 'b', 'c', 'd', 'x'):
      print('Neznamy vstup, prosim zadej "a", "b", "c", "d" nebo "x"')
      vstup = input('Zadej vstup: ')

  zadano = None
  if vstup == 'x':
      print('Diky cau!')
      exit(0)
  elif vstup == 'a':
      zadano = vysledky[0]
  elif vstup == 'b':
      zadano = vysledky[1]
  elif vstup == 'c':
      zadano = vysledky[2]
  elif vstup == 'd':
      zadano = vysledky[3]

  # vyhodnoceni
  if zadano == vysledek:
      print('Spravne, jen tak dal! :)')
  else:
      print('Spante, priste lip pocitej. :\'(')
