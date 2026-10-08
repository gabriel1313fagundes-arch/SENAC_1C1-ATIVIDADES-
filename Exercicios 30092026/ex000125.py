opcao = -1

while opcao !=0:
    print('1- consultar saldo')
    print('2- depositar')
    print ('3-sacar')
    print ('0- sair')

    opcao = int(input('Escolha:'))

    if opcao ==1:
       print ('consultando saldo...')
    elif opcao == 2:
        print('realizando depósito')
    elif opcao ==3:
        print('realizando saque...')
    elif opcao ==0:
       print('Encerrando...')
    else:
        print ('opção inválida')