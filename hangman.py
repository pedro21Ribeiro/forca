#jogo da forca
import random
palavras = ["macaco", "rato", "elefante", "hipopotamo"]
maxi = len(palavras) -1

def hangman():
    randNum = random.randrange(0,maxi)
    pEscolhida = palavras[randNum]
    numLetras = len(pEscolhida)
    letrasCorretas = list(pEscolhida)
    tentativas = 0
    acertos = 0
    letrasTentadas = []
    palavraMontada = []
    j = 0
    while j <= numLetras:
        palavraMontada.append("-")
    while tentativias <=6 and acertos <numLetras:
        letra = input("Digite uma letra:  ")
        charNum = len(list(letra))
        if charNum > 1:
            print("Isso foi mais de uma letra favor digitar somente uma letra \n")
        elif letra in letrasTentadas:
            print("Essa letra já foi usada\n")
        elif letra.isalpha():
            for i in letrasCorretas:
                if not i.isaplha:
                    if letra == i:
                        palavraMontada.append(letra)
                        print("parabens essa letra estava correta \n")
                        acertos = acertos + 1
                    else:
                        palavraMontada.append("-")
                        print("que pena letra errada\n")
                        tentativas = tentativas + 1
                        print(tentativas)
            letrasTentadas.append(letra)
        else:
            print("O input não é uma letra\n")
    if tentativas == 6:
        print("infelizmente voce perdeu, a palavra era" + pEscolhida)
    else:
        print("Parabéns voce acertou a palavra, "+ pEscolhida)
hangman()
