"""
ESCOLHENDO A OPÇÃO
"""

while True:
    print("\nMenu:")
    print("1. Pizza")
    print("2. Hamburguer")
    print("3. Coxinha")
    print("0. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '0':
        print("Saindo...")
        break
    elif escolha == '1':
        print("Você escolheu a Pizza!")
    elif escolha == '2':
        print("Você escolheu o Hamburguer!")
    elif escolha == '3':
        print("Você escolheu a Coxinha!")
    else:
        print("Opção inválida! Tente novamente.")