def main():
    frase = input()
    resposta = convert(frase)
    print(resposta)
#acima a gente criou a função main, que coleta o input e cria uma resposta convertendo o smiley. 
"""abaixo a gente criou a segunda função, para isso, precisei criar duas variaveis frase1 e frase2
utilizando a mudança. nota: no momento que você cria a frase2, atente-se em mudar de frase1 e não 
de frase"""
def convert(frase):
    frase1 = frase.replace(":)", "🙂")
    frase2 = frase1.replace(":(","🙁")

    return frase2

main()

#ok, sempre deixando esse comment final. Esse exercicio é pra que você crie um codigo 
#que converta :) e :( em emojis correspondentes. 
