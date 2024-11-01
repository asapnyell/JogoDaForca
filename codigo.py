print('Bem Vindo ao jogo da forca')
print('*'*30)

def exibir_progresso(palavra, letras_adivinhadas):
    # Exibir a palavra com os caracteres adivinhados e "_" para os não adivinhados
    progresso = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            progresso += letra + ' '
        else:
            progresso += '_ '
    return progresso

def jogar():
    palavras = ['granbery', 'espacial', 'estrela', 'caneta', 'borracha', 'forca']
    print("Escolha um número entre 0 e", len(palavras) - 1, "para selecionar a palavra:")

    indice = int(input("Digite o numero da palavra escolhida: "))
    print("*"*30)
    while indice < 0 or indice >= len(palavras):
        print("Índice inválido. Escolha um número entre 0 e", len(palavras) - 1)
        indice = int(input("Digite o numero para escolher uma palavra: "))

    palavra = palavras[indice]
    letras_advinhadas = []
    tentativas = 6

    while tentativas >0:
        print("Palavra:", exibir_progresso(palavra, letras_advinhadas))
        print(f"Tentativas restantes: {tentativas}")

        if tentativas == 1:
            tentativa_palavra = input("Última tentativa! Você quer tentar adivinhar a palavra? (sim/nao): ").lower()
            if tentativa_palavra == 'sim':
                palpite = input("Digite a palavra: ")
                if palpite == palavra:
                    print("\nParabéns! Você adivinhou a palavra:", palavra)
                    break
                else:
                    print("Palpite incorreto! A palavra era:", palavra)
                    tentativas -= 1  # Penaliza a tentativa se o palpite estiver errado
                    break
            else:
                print("Por favor, responda com 'sim' ou 'nao'.")

        letra = input("Digite uma letra: ")
        print("*"*30)
        if len(letra) != 1:
            print("Por favor, digite apenas uma letra")
            continue
        if letra in letras_advinhadas:
            print("Você ja adivinhou essa letra. Tente outra")
            continue
        letras_advinhadas.append(letra)

        if letra in palavra or letra not in palavra:
            tentativas -= 1

        # Verifica se todas as letras foram advinhadas
        if all(letra in letras_advinhadas for letra in palavra):
            print("\nParabéns! Você advinhou a palavra:", palavra)
            break
    else:
        print("\nVocê perdeu! A palavra era:", palavra)


jogar()