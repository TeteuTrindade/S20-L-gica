"""
CALCULANDO A MÉDIA DAS NOTAS
"""

soma = 0
contagem = 0

while True:
    nota = float(input("Digite uma nota (ou -1 para terminar): "))
    if nota == -1: # Se digitar -1 o programa encerra e calcula a média.
        break
    soma += nota # Soma 0 + o número digitado pelo usuário.
    contagem += 1 # Conta a quantidade de notas para calcular a média.

if contagem > 0: # A contagem só funciona com uma nota maior que zero.
    media = soma / contagem # A variável media vai fazer a divisão da soma das notas pela quantidade das notas.
    print(f"A média das notas é: {media:.2f}") # Arredondando resultado para até 2 casas decimais após a vírgula.
else:
    print("Nenhuma nota foi inserida.") 