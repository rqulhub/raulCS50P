def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

''' o mais complicadinho até então, em resumo, eles te dão boa parte da questão
precisamos criar essas duas funções. 
nessa primeira utilizamos a variavel dnumber alocar o replace do input do usuario
com esse input, removemos o $ e depois transformamos ele em float no return.
'''
def dollars_to_float(d):
    dnumber = d.replace("$","")
    return float(dnumber)
# basicamente a mesma coisa do que o de cima, a diferença é que antes de retornar
# cria-se uma nova variavel com a divisão do floar que acabamos de criar. 
def percent_to_float(p):
    pnumber = p.replace("%","")
    pporcento = float(pnumber) / 100
    return pporcento


main()
