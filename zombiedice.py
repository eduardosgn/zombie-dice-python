# Importando random
import random

# Zombie Dice Início
print('Zombie Dice - Protótipo Semana 04 - PUC PR\nSeja bem-vindo ao jogo!')

# #Inicializaçao do número dos jogadores
numJogadores = 0

# #Se tiver mais de 2 jogadores, o jogo continua
while (numJogadores < 2):
    numJogadores = int(input('Informe a quantidade de jogadores.\n'))
    if (numJogadores < 2):
        print('Você precisa de pelo menos 2 jogadores!\n')

# # Nomeando os jogadores
listaJogadores = []

for i in range(numJogadores):
    nome = input('Informe o nome do jogador {}: \n'.format(str(i+1)))
    listaJogadores.append(nome)

print('Lista de jogadores: {}\n\n'.format(listaJogadores))

# Criando dados
dadoVerde = 'CPCTPC'
dadoAmarelo = 'TPCTPC'
dadoVermelho = 'TPTCPT'

# Criando lista com a quantidade de dados
listaDados = []

for i in range(6):
    listaDados.append(dadoVerde)
for i in range(4):
    listaDados.append(dadoAmarelo)
for i in range(3):
    listaDados.append(dadoVermelho)

#Iniciando o jogo
print('--- INICIANDO JOGO ---')

jogadorAtual = 0
dadosSorteados = []
tiros = 0
passos = 0
cerebros = 0
corDado = ''

# Loop infinito
while True:
    print('Turno do jogador {}:'.format(listaJogadores[jogadorAtual]))

    # Soteando os dados a serem pegos
    for i in range(3):
        numSorteado = random.randint(0, 12)
        dadoSorteado = listaDados[numSorteado]

        if (dadoSorteado == 'CPCTPC'):
            corDado = 'Verde'
        elif (dadoSorteado == 'TPCTPC'):
            corDado = 'Amarelo'
        else:
            corDado = 'Vermelho'
        
        print('Dado sorteado: {}\n'.format(corDado))

        dadosSorteados.append(dadoSorteado)
    
    # Dado jogado e sorteando as faces em que eles pararam
    print('As faces sorteadas foram:\n')

    for dadoSorteado in dadosSorteados:
        numFaceDado = random.randint(0, 5)

        if (dadoSorteado[numFaceDado] == 'C'):
            print('- CÉREBRO - Você comeu um cérebro!')
            cerebros += 1
        elif (dadoSorteado[numFaceDado] == 'T'):
            print('- TIRO - Você levou um tiro!')
            tiros += 1
        else:
            print('- PASSO - Um humano escapou!')
            passos += 1
    
    print('\nSCORE ATUAL:')
    print('Cérebros: {}'.format(cerebros))
    print('Tiros: {}'.format(tiros))
    print('Humanos a salvo: {}\n'.format(passos))
    
    continuarTurno = input('AVISO: Você deseja continuar jogando dados?? (s -> sim / n -> não)')

    if (continuarTurno == 'n'):
        jogadorAtual += 1
        dadosSorteados = []
        tiros = 0
        passos = 0
        cerebros = 0

        if (jogadorAtual == len(listaJogadores)):
            print('Fim do jogo protótipo.')
            break
    else:
        print('Iniciando mais um rodada do turno atual...')
        dadosSorteados = []