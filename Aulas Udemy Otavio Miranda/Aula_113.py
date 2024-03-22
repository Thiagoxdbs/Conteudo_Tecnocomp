def mult(*args):
    args = list(*args)
    resultado = 0
    for num in args:
        if num == args[0]:
            resultado += num
            continue
        resultado *= num
    return resultado

def imp_par(numero):
    impar_ou_par = "Par" if numero % 2 == 0 else "Impar"
    return impar_ou_par

numero = 1,2,3,4,5
resultado_multi = mult(numero)
print(resultado_multi)

imp_par_resultado = imp_par(resultado_multi)
print(imp_par_resultado)

