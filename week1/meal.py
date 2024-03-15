def main():
    resposta = input("What time is it: ")
    cHoras = convert(resposta)

    if cHoras >= 7 and cHoras <= 8:
        print("breakfast time")
    elif cHoras >= 12 and cHoras <= 13:
        print("lunch time")
    elif cHoras >= 18 and cHoras <= 19:
        print("dinner time")

def convert(cHoras):
    horas, minutos = cHoras.split(":")
    novosMinutos = float(minutos) / 60
    return float(horas) + novosMinutos

if __name__ == "__main__":
    main()
