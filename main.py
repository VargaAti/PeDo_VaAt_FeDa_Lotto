import random as rn
print("""

      """)

user = []
for i in range(5):
    user.append(int(input("Adj meg egy számot! ")))

gep = []
for i in range(5):
    gep.append(rn.randint(0, 100))



print(f"A te számjaid: {user}")
print(f"Nyerő számok: {gep}")
print(f"Eltalált számok: {talalt}")
