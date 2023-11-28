#!/usr/bin/env python3

"""Um script para calcular tempo de aulas de cursos online

Como usar:

Adicione as informações brutas sem formatação na string dados, não precisa retirar
os títulos/descrições das aulas o script vai processar as informações passadas

Ex:
dados = '''
Fundamentos de redes - 13:33
Arquivos importantes - 08:44
Configuração de IP, máscara e rota - Não persistente - 09:59
Configuração de IP, máscara e rota - 04:40
Ferramentas de redes - parte 1 (nc) - 07:35
Ferramentas de redes - parte 2 (ss) - 06:53
Ferramentas de redes - parte 3 (nmtui) - 03:22
Ferramentas de redes - parte 4 (outros) - 08:32 
'''

Execução:
  python3 calcula-aulas.py
  ou
  ./calcula-aulas.py
"""

from datetime import datetime, timedelta

def calcula_tempo_aulas(dados):
    # Separar as linhas dos dados
    aulas_separadas = dados.strip().split('\n')

    # Inicializar a variável de soma
    soma = timedelta()

    # Iterar sobre as linhas e extrair os minutos de cada linha
    for linha in aulas_separadas:
        # Dividir a linha para obter o tempo (último elemento)
        #tempo_str = linha.split('-')[-1].strip()

        #minuto = aula.split('-')[1] # meu código
        tempo_str = linha.split('-')[-1].strip()

        # Converter o tempo para um objeto datetime
        tempo = datetime.strptime(tempo_str, "%M:%S")

        # Adicionar o tempo ao total
        soma += timedelta(hours=tempo.hour, minutes=tempo.minute, seconds=tempo.second)

    #print("-----")
    #print(soma)
    #print("-----")

    # Exibir o resultado formatado
    horas, segundos = divmod(soma.total_seconds(), 3600)
    minutos, segundos = divmod(segundos, 60)

    # Exibir o resultado formatado
    print(f'Total de tempo: {int(horas)} horas, {int(minutos)} minutos, {int(segundos)} segundos')
    print()
    print(f'Total de tempo: {int(horas)}h {int(minutos)}m {int(segundos)}s')

dados = '''

''' 
calcula_tempo_aulas(dados=dados)
