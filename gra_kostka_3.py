# module import:
from random import randint

#variables definicion:
print("""Witaj w mojej grze:

gra polega na wylosowaniu liczby większej lub wównej 4.
W innym wypadku przegrywasz
""")

gracz1_nick=input("podaj nick dla gracza nr1: ")

gracz2_nick=input("podaj nick dla gracza nr2: ")


kostka1 = randint(1, 6)
kostka2 = randint(1, 6)
kostka3 = randint(1, 6)
kostka4 = randint(1, 6)

print (f"""Wylosowano:
{gracz1_nick}: {kostka1}
{gracz1_nick}: {kostka2}
{gracz2_nick}: {kostka3}
{gracz2_nick}: {kostka4}
""")  

if kostka1 * kostka2 < kostka3 * kostka4:
    print(f"{gracz2_nick} wygrał")
elif kostka1 * kostka2 ==  kostka3 * kostka4:
    print("REMIS!!!")
else:
    print(f"{gracz1_nick} wygrał")


