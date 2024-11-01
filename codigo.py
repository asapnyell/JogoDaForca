import random

print('BEM VINDO AO JOGO DA FORCA')
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

    palavra = random.choice(palavras)
    letras_advinhadas = []
    tentativas = 6

    while tentativas >0:
        print("Palavra:", exibir_progresso(palavra, letras_advinhadas))
        print(f"Tentativas restantes: {tentativas}")

        if tentativas == 1:
            tentativa_palavra = input("Última tentativa! Você quer tentar adivinhar a palavra? (sim / nao): ").lower()
            while tentativa_palavra not in ('sim', 'nao'):
                 tentativa_palavra = input("Por favor, responda com 'sim' ou 'não': ").lower()

            if tentativa_palavra == 'sim':
                palpite = input("Digite a palavra: ")
                if palpite == palavra:
                    print("\nParabéns! Você adivinhou a palavra:", palavra)
                    break
                else:
                    print("Palpite incorreto! A palavra era:", palavra) # Penaliza a tentativa se o palpite estiver errado
                    break
            
        letra = input("Digite uma letra: ").lower()
        print("*"*30)
        if len(letra) != 1 or not letra.isalpha():

            print("Por favor, digite apenas uma letra")
            continue
        if letra in letras_advinhadas:
            print("Você ja adivinhou essa letra. Tente outra")
            continue
        letras_advinhadas.append(letra)

        if letra not in palavra:
            tentativas -= 1

        # Verifica se todas as letras foram advinhadas
        if all(letra in letras_advinhadas for letra in palavra):
            print("\nParabéns! Você advinhou a palavra:", palavra)
            break
    else:
        print("\nVocê perdeu! A palavra era:", palavra)


jogar()