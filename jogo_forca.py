secreto = input('Digite uma palavra: ')
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Não vale trapacear!')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra {letra} existe na palavra secreta!')
    else:
        print(f'A letra {letra} NÃO existe na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print('Você GANHOU!')
        break
    else:
        print(secreto_temporario)

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
