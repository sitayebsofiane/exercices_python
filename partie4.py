#coding:utf8
def alter():
    import math
    #exo1:
    def exo1():
        display1="# "
        display2=" #"
        result=""
        for i in range(0,8):
            if(i%2!=0):
                result+=display1*4+"\n"
            else:
                result+=display2*4+"\n"

        print(result)
    #exo2:
    def exo2():
       
        for i in range(1,5):
            for j in range(0+i,4+i):
                if(i<j):
                    print(0)
                else:
                    print(1)
            print("_ _ _ _ _ _")
    #exo3:
    def exo3():
        def paire(nombre):
            try:
                if not nombre.is_integer():
                    nombre=round(nombre)
                return nombre%2==0
            except ValueError:
                print("erreur d'entré")
        print(paire(float(input("entrez un nombre entier "))))
    try:
        dico={"1":exo1,"2":exo2,"3":exo3}
        dico[input("enter le numero de l'exo a exucte ")]()
    except KeyError:
        print("entrez soit 1,2,3....")

alter()
    

               