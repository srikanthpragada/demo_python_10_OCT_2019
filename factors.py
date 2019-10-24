# Take a number on command line and display factors

import sys

if len(sys.argv) < 2:
    print("Sorry! Number is missing!")
    sys.exit(1)  # stop program


for v in sys.argv[1:]:
  print(f"\nFactors of {v:5} : ", end=' ')
  num = int(v)
  for i in range(2, num//2 + 1):
    if num % i == 0:
        print(i, end = ' ')

