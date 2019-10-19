#coding:utf8
def alter():
    import math,time,re
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
        def matrix(morpheus):
            for i in range(0,morpheus):
                for j in range(0,morpheus):
                    time.sleep(0.3)
                    if(i==j):
                        print(1)
                    else:
                        print(0)
                print("\n\"_ _ _ _ _ _ _\"\n")
        matrix(4)
     
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
    #exo4:
    def exo4():
        def facto(n):
            if n==0:
                return 1
            else:
                return n*facto(n-1)
        print("factorielle:",facto(int(input("entrez un nombre entier: "))))
    #exo5:
    def exo5():
        def rgex(texte):
            if not isinstance(texte,str):
                raise ValueError
            try:
                return re.sub(r"-",r"_",texte)
            except ValueError:
              print("message erreur")
        print(rgex(input("tapez votre texte: ")))
    
    try:
        dico={"1":exo1,"2":exo2,"3":exo3,"4":exo4,"5":exo5}
        dico[input("enter le numero de l'exo a exucte ")]()
    except KeyError:
        print("entrez soit 1,2,3....")

alter()
    

               