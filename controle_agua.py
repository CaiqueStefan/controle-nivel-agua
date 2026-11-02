from colorama import Fore, Style
from random import randint

niveis = [
    "Nível 1: Muito baixo (CRÍTICO)",
    "Nível 2: Baixo",
    "Nível 3: Médio",
    "Nível 4: Alto",
    "Nível 5: Muito alto (ALERTA)",
]


def definir_cor(nivel):
    cores = {
        1: Fore.RED,
        2: Fore.YELLOW,
        3: Fore.GREEN,
        4: Fore.CYAN,
        5: Fore.BLUE,
    }
    return cores.get(nivel, Fore.WHITE) 


def exibir_situacao(nivel):
    if 1 <= nivel <= len(niveis):
        cor = definir_cor(nivel)
        mensagem = niveis[nivel - 1]
        print(f"{cor}{mensagem}{Style.RESET_ALL}")


def ler_sensor():
    return randint(1, 5)


# Programa principal
print("=== Monitoramento do Reservatório ===\n")
print("Níveis de água:")

# Exibe todos os níveis para demonstrar as cores
for nivel in range(1, 6):
    exibir_situacao(nivel)

# Leitura simulada do sensor (muda a cada execução)
print()
leitura = ler_sensor()
print("Obtendo leitura do sensor, aguarde...\n")
print("Leitura do sensor recebida.")
print("Situação atual:")
exibir_situacao(leitura)

# Restaura o estilo padrão do terminal
print(Style.RESET_ALL)
