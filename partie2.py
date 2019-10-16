#coding:utf8

#exo1:
var1=""
var2=""
#cheking var1,var2 if empty
def verifVar(*var):
    res=""
    for el in var:
        res +=el
    return res==""
print(verifVar(var1,var2))
#exo2:
import time
try:
    actuel_year=int(input("entrez l'année actuel: "))
    if(actuel_year != int(time.strftime("%Y"))):
        print("l'année actuel est :",time.strftime("%Y"))
    actuel_year=int(time.strftime("%Y"))
    death_year=int(input("entrez votre année de naissaice: "))
    age=actuel_year-death_year
    print("votre age est ",age)
    print("le cumul des age: ",age+int(input("age de la personne a coté: ")))
except ValueError:
    time.sleep(1)
    print("vous avez mal resigner les année")
#exo3

prix1=70
prix2=59
prix3=20
total= lambda total:total-total*20/100
print("total est : ",total(prix1+prix2+prix3))

#exo4

print("resultat",float(input("entrez le premier nombre a aditionner "))
                +
float(input("entrez le deuxieme nombre a aditionner ")))

#exo5
import math
prenom=input("entrez le prenom ").upper()
nom=input("entrez le nom ").upper()
#affiche la premiere et la derniere lettre de son prenom en majuscule
print(prenom[0],prenom[-1])
#affiche la premiere et la derniere lettre de son nom en majuscule
print(nom[0],nom[-1])
print(prenom[0]+prenom[-1]+nom[0]+nom[-1])
print("l'age divisé par 33 et arrondi entier sup ",math.ceil(float(input("entrez votre age "))/33))

