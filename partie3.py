def alter():
    import math,random
    #exo1:
    def exo1():
        var1=random.randint(1,11)
        var2=random.randint(1,11)
        var3=random.randint(1,11)
        var4=random.randint(1,11)
        liste=[var1,var2,var3,var4]
        maxi=0
        index=0
        for ind,elt in enumerate(liste):
            if elt>=maxi:
                maxi=elt
                index=ind
        print(maxi,"est le sup de",liste,
        "a la position",index+1)
    #exo2:
    def exo2():
        try:
            age=int(input("taper votre age:"))
            if age<=0:
                raise ValueError
            elif age>=21:
                print("autorisé")
            if  age%2==0:
                print("votre age est pair")
            if math.sqrt(age).is_integer():
                print("votre age est un nombre carré")
        except ValueError:
            print("taper votre age en chiffre entier positif")
    #exo3:
    def exo3():
        nombre_caché=random.randint(0,10)
        nombre_deviné=-1
        try:
            while nombre_caché!=nombre_deviné:
                if 0<=nombre_deviné<nombre_caché:
                    print("trop petit")
                    nombre_deviné=int(input("entrez un chiffre a nouveau: "))
                elif 0<=nombre_caché<nombre_deviné:
                    print("trop grand")
                    nombre_deviné=int(input("entrez un chiffre a nouveau: "))
                else:
                    nombre_deviné=int(input("entrez un chiffre entre 0 et 10: "))
            
            print("gagnez !")
        except ValueError:
            print("entrez un nombre entier ")
    #exo4:
    def exo4():
       for i in range(1,101):
           print(i)
    #exo5:      
    def exo5():
        for i in range(1,101):
            if(i%2==0):
                print(i)
    #exo6:
    def exo6():
        l=float(input("entrez longueur en mettre: "))
        w=float(input("entrez largeur en mettre: "))
        d=float(input("entrez longueur en mettre: "))
        de=float(input("entrez debit: "))
        def temps_remp(l,w,d,de):
           return l*w*d/de
        print("le temps remplissage:",temps_remp(l,w,d,de),"minutes")
    #exo7:
    def exo7():
        def aire(rayon):
            return math.pi*math.pi*rayon
        def peri(rayon):
            return math.pi*2*rayon
        r=float(input("entrez le rayon:" ))
        print("la surface",round(aire(r),2),"perimetre",round(peri(r),2))
    #exo8:
    def exo8():
        a=int(input("entrez un nombre la taille de la pyramide"))
        pyramide="*"
        for taille in range(1,a):
            print(pyramide*taille)
    #exo9:
    def exo9():
        for n in range(1,101):
            if n%3==0 and  n%5 + n%3!=0:
                print(n,":FIZZ")
            elif n%5==0 and  n%5 + n%3!=0:
                print(n,":BUZZ")
            elif n%5 + n%3==0:
                print(n,":FIZZBUZZ")
            else:
                print(n)


    try:
        dico={"1":exo1,"2":exo2,"3":exo3,"4":exo4,"5":exo5,"6":exo6,
        "7":exo7,"8":exo8,"9":exo9}
        dico[input("enter le numero de l'exo a exucte ")]()
    except KeyError:
        print("entrez soit 1,2,3....")
alter()