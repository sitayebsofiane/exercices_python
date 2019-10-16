#coding:utf8

#exo1:
#display "hello world" in terminal
print("Hello world")
#display "hello world" in terminal with variable
bruno="Hello world"
print(bruno)
#exo2:
#display result of arithmitiques operations
print("res_mulication:",3*3,"res_addition:",4+9+78,"res_substraction:",12-7,"res_power:",5e4)
try:
    print("division:",12/0)
except ZeroDivisionError:
    print("impossible de deviser par zero")
#exo3:
#progrm interacted with user
nom = input("comminiquer votre nom: ")
print("bienvenue",nom)
#exo4:
#display
name = "Gossart"
surname = "Thomas"
dis=name+"  "+surname
print(dis)
#exo5:
#check type of variable
myNumber = "123"
myNumber = int(myNumber)
if(isinstance(myNumber,int)):
    print(myNumber,"est correctement modifié en un nombre entier")
else:
    print(myNumber,"est toujour une chaine de caracter !")
#exo6:
#upper and lower case
mot = input("entrez un mot ")
print("Transformation en maj",mot.upper(),",Transformation en min",mot.lower())