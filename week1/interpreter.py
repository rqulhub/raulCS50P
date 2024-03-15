expression = input("Expression: ")
x1, y, z1 = expression.split()
x = float(x1)
z = float(z1)

match y:
    case "+":
        conta = x + z
        print(conta)
    case "-":
        conta = x - z
        print(conta)
    case "*":
        conta = x * z
        print(conta)
    case "/":
        conta = x / z
        print(conta)
