#coding:utf8
def alter():
    import math,time,re,datetime
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
    #exo6:
    def exo6():
        liste=["persil","tomate","café","biére","viande"]
        print(liste)
        print("element premiere position",liste[0])
        print("element derniere position",liste[-1])
        print("element medium position",liste[int((len(liste)-1)/2)])
    #exo7:
    def exo7():
        timestamp=time.mktime(datetime.datetime.
        strptime("01/01/1985", "%d/%m/%Y").timetuple())
        liste=["si-tayeb","sofiane",34,time.localtime(timestamp)]

        def tableau(*tab):
            for i in tab:
                print(i) 
        tableau(liste) 
    try:
        dico={"1":exo1,"2":exo2,"3":exo3,"4":exo4,"5":exo5,"6":exo6,"7":exo7}
        dico[input("enter le numero de l'exo a exucte ")]()
    except KeyError:
        print("entrez soit 1,2,3....")

alter()
    

               