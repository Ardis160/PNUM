import math

def bad_sum():
    step = 0.1
    a = 0
    b = 1
    while a != b:
      print(f"Aktuální hodnota:{a}")
      a += step
      if a > 1.1: # podmínka,aby to vůbec někdy skončilo
        break
    print(f"Aktuální hodnota:{a}")

def fix_sum():
    step = 0.1
    a = 0
    b = 1
    EPS = 1e-5
    while math.fabs(b - a) >= EPS:  # tato podmínka je klíčová
        print(f"Aktuální hodnota:{a}")
        a += step
    print(f"Aktuální hodnota:{a}")


bad_sum()
fix_sum()