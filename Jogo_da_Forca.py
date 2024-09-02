# Importando pacotes utilizados.
import random
import re
import unidecode
import os

# Mensagem de boas-vindas e instruções.
inicio=input('Olá, seja bem vindo! Você está jogando o Jogo da Forca, digite qualquer tecla para começar a jogar\n')

# Pool de palavras
frutas = ['U v a', 'B a n a n a', 'P ê r a', 'M a ç ã', 'L a r a n j a', 'M e l a n c i a', 'M e l ã o', 'M a m ã o', 'L i m ã o', 'T o m a t e', 'A b a c a x i', 'M o r a n g o', 'C e r e j a', 'A m o r a', 'M a r a c u j á', 'J a b u t i c a b a']
cores = ['A z u l', 'V e r m e l h o', 'R o s a', 'V e r d e', 'L a r a n j a', 'R o x o', 'P r e t o', 'M a r r o m', 'C i n z a', 'A m a r e l o', 'B r a n c o', 'L i l á s', 'B e g e', 'C i a n o']
partes_do_corpo = ['C a b e ç a', 'B r a ç o', 'P e r n a', 'M ã o', 'P é', 'O l h o', 'O r e l h a', 'N a r i z', 'B o c a', 'P e s c o ç o', 'O m b r o', 'J o e l h o', 'A n t e b r a ç o', 'P a n t u r r i l h a', 'E s c á p u l a', 'E s t e r n o c l e i d o m a s t o i d e o', 'M e t a c a r p o', 'C l a v í c u l a', 'E s t e r n o']
paises = ['B r a s i l', 'A r g e n t i n a', 'C h i l e', 'P e r u', 'C o l ô m b i a', 'U r u g u a i', 'P a r a g u a i', 'B o l í v i a', 'E q u a d o r', 'V e n e z u e l a', 'M é x i c o', 'C a n a d á', 'E s t a d o s  U n i d o s', 'F r a n ç a', 'A l e m a n h a', 'A u s t r á l i a', 'Á f r i c a  d o  S u l']

# Função para aleatoriedade da escolha das palavras.
def aleatorio(x):
    a = random.choice(x)
    return a

# Escolha de dificuldade para o jogo, altera o número de tentativas para adivinhar.
chances = 0
dificuldade = input('''Insira o número correspondente da dificuldade que gostaria de jogar:\n
1. Fácil
2. Intermediário
3. Difícil
4. Desafiador\n
''')
while True: 
    if dificuldade.isdigit():
        dificuldade = int(dificuldade)
        if dificuldade in [1,2,3,4]:
            if dificuldade == 1:
                chances = 30
            elif dificuldade == 2:
                chances = 22
            elif dificuldade == 3:
                chances = 16
            elif dificuldade == 4:
                chances = 11
            break
    dificuldade = input('digite um numero corretamente: \n')
if dificuldade == 1:
    print('A dificuldade escolhida foi: Fácil\n')
elif dificuldade == 2:
    print('A dificuldade escolhida foi: Intermediário\n')
elif dificuldade == 2:
    print('A dificuldade escolhida foi: Difícil\n')
elif dificuldade == 2:
    print('A dificuldade escolhida foi: Desafiador\n')

print('Você terá o seguinte número de chances: %s\n' %(chances))

# Escolha aleatória da palavra.
pool = [frutas, cores, partes_do_corpo, paises]
grupo = aleatorio(pool)
palavra = aleatorio(grupo)
# Normalização para comparação da entrada que o usuário inserir com o "gabarito".
if "  " in palavra:
    palavra = palavra.replace("  ", ".")

palavra_norm = unidecode.unidecode(palavra)
palavra_norm = palavra_norm.lower()

# Mostrando dica ao usuário.
if grupo == frutas:
    print('Dica: A palavra é uma fruta\n')
elif grupo == cores:
    print('Dica: A palavra é uma cor\n')
elif grupo == partes_do_corpo:
    print('Dica: A palavra é uma parte do corpo humano\n')
elif grupo == paises:
    print('Dica: A palavra é um país\n')

# Trocando as letras do gabarito por "_"
adivinhar = re.sub(r'[A-Za-zÀ-ÿ]', '_', palavra)

# Função que recebe a entrada do usuário (letra ou palavra completa) e compara com o gabarito, fazendo a troca de "_" por 
# letra caso o chute esteja correspondendo com o gabarito.
i=0
letras_erradas = []
def troca_letra(x):    
    global adivinhar
    global i
    global lista_adivinhar
    
    lista_palavra = list(palavra)
    lista_palavra_norm = list(palavra_norm)
    lista_adivinhar = list(adivinhar)
    tentativa_errada = True

    for a in lista_palavra_norm:
        if a == tentativa:
            lista_adivinhar[i] = lista_palavra[i]
            tentativa_errada = False  # Marcar que a tentativa está correta
        i=i+1
    if tentativa_errada:  # Apenas adicionar à lista de erradas se a tentativa estiver errada
        letras_erradas.append(tentativa)
        print(" ".join(map(str,letras_erradas)))
    adivinhar = ''.join(lista_adivinhar)
    i=0
    return adivinhar

# Loop responsável por manter a dinamica do jogo acontecendo, pedindo entradas ao usuário até que as tentativas cheguem a zero
# ou o usuário acerte o gabarito.
while chances > 0:
    print('\nTentativas restantes: ', chances)
    print(adivinhar.replace(".", "  "))
    tentativa = input('\nDigite uma letra: ').lower()
    tentativa = tentativa.strip()
    tentativa = unidecode.unidecode(tentativa)
    troca_letra(tentativa)
    if len(tentativa) <=1:
        if "_" not in adivinhar:
            print("você venceu!\nA palavra era:", palavra.replace(" ","").replace(".", " "))
            break
    else:
        if tentativa == palavra_norm.replace(" ","").replace(".", " "):
            print('tentou adivinhar e acertou! A palavra era:', palavra.replace(" ","").replace(".", " "))
            break
        else:
            chances = 0
    chances = chances-1
    if chances <= 0:
        print("Você perdeu!\nA palavra era:", palavra.replace(" ","").replace(".", " "))