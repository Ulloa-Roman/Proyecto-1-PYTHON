#Debemos calcular el pago de una persona empleada en nuestra empresa. El cálculo debe hacerse por la cantidad de horas trabajadas, y se le debe pedir al usuario la cantidad de horas y cuánto vale cada hora.
#se abona un plus fijo de guardería a todo empleado/a con infantes a su cargo
# se paga un 10% de incentivo a todo empleado/a que haya trabajado 30 horas o más y no reciba el plus por guardería.

#CASO A: Empleado/a con menos de 30 horas y sin infantes a cargo.
#CASO B: Empleado/a con 30 horas o más y sin infantes a cargo.
#CASO C: Empleado/a con menos de 30 horas y con infantes a cargo.
#CASO D: Empleado/a con 30 horas o más y con infantes a cargo.


def calculo_pago():
    horas=int(input("Ingrese la cantidad de horas trabajadas: "))
    infantes=input("¿tiene infantes a cargo?(responda con si o con no): ")
    valor_horas=int(input("Ingrese el valor de la hora: "))
    plus_fijo=int(100)
    pago_a=horas*valor_horas
    pago_b=(int(10*100))+pago_a
    pago_c=pago_a+plus_fijo
    pago_d=pago_b+plus_fijo
    
    if horas<30 and infantes=="no":
        return pago_a
    elif horas>=30 and infantes=="no":
        return pago_b
    if horas<30 and infantes== "si":
        return pago_c
    elif horas>=30 and infantes=="si":
        return pago_d
    
print (calculo_pago())
    