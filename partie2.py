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