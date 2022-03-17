"""
    Protótipo inicial jogo Zombie Dice
    ----
    Nome: Eduardo da Silva Gomes do Nascimento
    Curso: Análise e Desenvolvimento de Sistemas
"""

# Importando random para o uso da função randint()
import random

# Zombie Dice Início
print('Zombie Dice - PUC PR\nSeja bem-vindo ao jogo!')

# Inicializaçao do número dos jogadores
numJogadores = 0

# Se tiver mais de 2 jogadores, o jogo continua, se não for um número válido, o expect é acionado e o loop volta para o input dentro do try
while (numJogadores < 2):
    try:
        numJogadores = int(input('Informe a quantidade de jogadores.\n'))
        if (numJogadores < 2):
            print('Você precisa de pelo menos 2 jogadores!\n')
    except ValueError:
        print('Digite um número válido...')

# Nomeando os jogadores
listaJogadores = []
for i in range(numJogadores):
    nome = input('Informe o nome do jogador {}: \n'.format(str(i+1)))
    listaJogadores.append(nome)

print('Lista de jogadores: {}\n'.format(listaJogadores))

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

# Iniciando o jogo
print('--- INICIANDO JOGO ---')

jogadorAtual = 0
dadosSorteados = []
tiros = 0
passos = 0
cerebros = 0
corDado = ''

# Loop infinito do jogo
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
    
    # Sorteando as faces em que os dados pararam
    print('As faces sorteadas foram:\n')

    for dadoSorteado in dadosSorteados:
        numFaceDado = random.randint(0, 5)

        # contabilizando os pontos dependendo do lado das faces dos dados
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
    
    # Se o jogador quiser continuar a jogar dados, digitar s (as lista de dados sorteados zera e o jogo continua) se não será a vez do próximo jogador.
    continuarTurno = input('AVISO: Você deseja continuar jogando dados?? (s -> sim / n -> não)')

    if (continuarTurno == 'n'):
        jogadorAtual += 1
        dadosSorteados = []
        tiros = 0
        passos = 0
        cerebros = 0

        # Se os dois jogadores não quiseram mais jogar dados e o tamanho da lista de jogadores chegar ao fim, o jogo acaba.
        if (jogadorAtual == len(listaJogadores)):
            print('Fim do jogo protótipo.')
            break
    else:
        print('Iniciando mais um rodada do turno atual...')
        dadosSorteados = []