import random
#exo1:
var1=random.randint(1,11)
var2=random.randint(1,11)
var3=random.randint(1,11)
var4=random.randint(1,11)
liste=[var1,var2,var3,var4]
"""
liste.sort()
print("element plus grand de la liste:\n",liste,"est",liste[-1])
"""
maxi=0
for elt in liste:
    if elt>=maxi:
        maxi=elt
print(maxi,"est le sup de",liste)

