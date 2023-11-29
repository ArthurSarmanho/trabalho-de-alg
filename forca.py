import random #Escolhas aleatórias
def carregar_palavras(): #carrega as palavras a partir do arquivo de dados que criei para armazenar as respostas da forca
 with open("palavras.txt", "r", encoding="utf-8") as arquivo:
  palavras = arquivo.readlines()
 return [palavra.strip().lower() for palavra in palavras]
def escolher_palavra(palavras): #escolhe uma palavra aleatória
 return random.choice(palavras)
def jogar_forca(palavra): #joga
    palavra_escondida = ["_" if letra.isalpha() else letra for letra in palavra]#letras da palavra escondida, substitui as letras por '_' e mantém outros caracteres
    letras_erradas = []#letras erradas que foram fornecidas pelo usuário
    tentativas = 6
    while tentativas > 0:
        letra_usuario = input("\nType a letter: ").lower()#verifica se o usuário teclou uma letra
        if letra_usuario.isalpha() and len(letra_usuario) == 1:
            if letra_usuario in palavra:#se a letra fornecida constar na palavra, então vai atualizar a palavra e mostrar a posição das letras
             for i in range(len(palavra)):
                if palavra[i] == letra_usuario:
                        palavra_escondida[i] = letra_usuario
            else:
                letras_erradas.append(letra_usuario)
                tentativas -= 1#reduz o número de tentativas sempre que o jogador errar a letra
            print("Word: ", " ".join(palavra_escondida))#printa o estado da palavra, posição das letras, letras que não constam e tentativas restantes
            print("Wrong letters: ", " ".join(letras_erradas))
            print(f"Remaining attempts: {tentativas}")
            if "_" not in palavra_escondida: #verifica se o jogador ganhou :D
                print("\nCONGRATULATIONS! YOU WIN!")
                break
        else:
            print("Please enter a valid letter.")
    if tentativas == 0: #se o número de tentativas chegar em 0, mostra a mensagem de fim de jogo :(
        print("\nGame over! The word was:", palavra)
if __name__ == "__main__":
    print("Welcome to the HANGMAN GAME!")
    while True:
        palavras = carregar_palavras()
        palavra_secreta = escolher_palavra(palavras)
        print("Tip: The word has", len(palavra_secreta), "letters.")
        jogar_forca(palavra_secreta)
        continuar_jogo = input("\nDo you want to play again? (y/n): ").lower() #uma mensagem perguntando se o jogador deseja jogar novamente ou não
        if continuar_jogo != 'y':
            print("Thank you for playing the Hangman Game! :D")
            break