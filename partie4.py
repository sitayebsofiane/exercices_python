#coding:utf8
def alter():
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

    try:
        dico={"1":exo1}
        dico[input("enter le numero de l'exo a exucte ")]()
    except KeyError:
        print("entrez soit 1,2,3....")

alter()
    

               