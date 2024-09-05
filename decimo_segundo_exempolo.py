"""
CONTAGEM REGRESSIVA
"""
while True:
    numero = int(input("Digite um número para iniciar a contagem regressiva: ")) # Está falando para colocar um número para iniciar a contagem.
    
    while numero >= 0: # Quando for maior que 0.
        print(numero) # Mostre o número.
        numero -= 1 # Na ordem decrescente.
    
    continuar = input("Quer fazer outra contagem regressiva? (s/n): ")
    if continuar.lower() == 'n': # Se digitar a letra n.
        break # O programa para.