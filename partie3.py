def alter():
    import math,random
    #exo1:
    def exo1():
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
   
    try:
        dico={"1":exo1,"2":exo2}
        dico[input("enter le numero de l'exo a exucte ")]()
    except KeyError:
        print("entrez soit 1,2,3....")
alter()