import math
""" Juros Simples, Montante Simples, Juros Compostos, Montante Composto, Desconto Simples """

opcao = 1

def jurosSimples():
    opcaoFuncao = 1
    while opcaoFuncao != 5:
        print("1- Juros")
        print('2- Capital')
        print('3- Tempo (em meses)')
        print('4- Taxa de juros (a.m)')
        print('5- Sair')

        opcaoFuncao = int(input('Escolha a opção que deseja calcular em juros simples: '))

        if opcaoFuncao == 1:
            print('-----Juros-----')
            capital = float(input('Digite o capital: '))
            tempo = float(input('Digite o tempo em meses: '))
            taxa = float(input('Digite a taxa de juros (a.m): '))/100
            juros = capital * tempo * taxa
            print(f'O juros é de R${juros:.2f}')
            break
            
        elif opcaoFuncao == 2:
            print('-----Capital-----')
            juros = float(input('Digite os juros: '))
            tempo = float(input('Digite o tempo em meses: '))
            taxa = float(input('Digite a taxa de juros (a.m): '))/100
            capital = juros / (tempo * taxa)
            print(f'O capital é de R${capital:.2f}')
            break

        elif opcaoFuncao == 3:
            print('-----Tempo (em meses)-----')
            juros = float(input('Digite os juros: '))
            capital = float(input('Digite o capital: '))
            taxa = float(input('Digite a taxa de juros (a.m): '))/100
            tempo = juros / (capital * taxa)
            print(f'O tempo é de {tempo:.2f} meses')
            break

        elif opcaoFuncao == 4:
            print('-----Taxa de juros (a.m)-----')
            juros = float(input('Digite os juros: '))
            capital = float(input('Digite o capital: '))
            tempo = float(input('Digite o tempo em meses: '))
            taxa = (juros / (capital * tempo))*100
            print(f'A taxa de juros é de {taxa:.2f}% a.m.')
            break

        elif opcaoFuncao == 5:
            print('Saindo... 🚀')
            break

        else:
            print('Opção inválida!')

def montanteSimples():
    capital = float(input('Digite o capital: '))
    tempo = float(input('Digite o tempo em meses: '))
    taxa = float(input('Digite a taxa de juros (a.m): '))/100
    juros = capital * tempo * taxa
    montante = capital + juros
    print(f'O montante é de R${montante:.2f}')
    
def jurosCompostos():
    capital = float(input('Digite o capital: '))
    tempo = float(input('Digite o tempo em meses: '))
    taxa = float(input('Digite a taxa de juros (a.m): '))/100
    montante = capital * (1 + taxa)**tempo
    juros = montante - capital
    print(f'O juros é de R${juros:.2f}')

def montanteComposto():
    opcaoFuncao = 1
    while opcaoFuncao != 5:
        print("1- Montante")
        print('2- Capital')
        print('3- Tempo (em meses)')
        print('4- Taxa de juros (a.m)')
        print('5- Sair')

        opcaoFuncao = int(input('Escolha a opção que deseja calcular em montante composto: '))

        if opcaoFuncao == 1:
            print('-----Montante-----')
            capital = float(input('Digite o capital: '))
            tempo = float(input('Digite o tempo em meses: '))
            taxa = float(input('Digite a taxa de juros (a.m): '))/100
            montante = capital * (1 + taxa)**tempo
            print(f'O montante é de R${montante:.2f}')
            break
            
        elif opcaoFuncao == 2:
            print('-----Capital-----')
            montante = float(input('Digite o montante: '))
            tempo = float(input('Digite o tempo em meses: '))
            taxa = float(input('Digite a taxa de juros (a.m): '))/100
            capital = montante / ((taxa + 1) ** tempo)
            print(f'O capital é de R${capital:.2f}')
            break

        elif opcaoFuncao == 3:
            print('-----Tempo (em meses)-----')
            montante = float(input('Digite o montante: '))
            capital = float(input('Digite o capital: '))
            taxa = float(input('Digite a taxa de juros (a.m): '))/100
            tempo = math.log(montante / capital) / math.log(1+taxa)
            print(f'O tempo é de {tempo:.2f} meses')
            break

        elif opcaoFuncao == 4:
            print('-----Taxa de juros (a.m)-----')
            montante = float(input('Digite o montante: '))
            capital = float(input('Digite o capital: '))
            tempo = float(input('Digite o tempo em meses: '))
            taxa = ((montante / capital) ** (1/tempo)) - 1
            print(f'A taxa de juros é de {(taxa * 100):.2f}% a.m.')
            break

        elif opcaoFuncao == 5:
            print('Saindo... 🚀')
            break

        else:
            print('Opção inválida!')

def descontoSimples():
    opcaoFuncao = 1
    while opcaoFuncao != 6:
        print("1- Desconto")
        print('2- Valor atual')
        print('3- Valor principal')
        print('4- Tempo (em meses)')
        print('5- Taxa de juros (a.m)')
        print('6- Sair')

        opcaoFuncao = int(input('Escolha a opção que deseja calcular em desconto simples: '))

        if opcaoFuncao == 1:
            print('-----Desconto-----')
            vp = float(input('Digite o valor principal: '))
            tempo = float(input('Digite o tempo (em meses): '))
            taxa = float(input('Digite a taxa de juros (a.m): '))/100
            desconto = vp * tempo * taxa
            print(f'O desconto é de R${desconto:.2f}')
            break
            
        elif opcaoFuncao == 2:
            print('-----Valor atual-----')
            vp = float(input('Digite o valor principal: '))
            tempo = float(input('Digite o tempo (em meses): '))
            taxa = float(input('Digite a taxa de juros (a.m): '))/100
            va = vp * (1 - (taxa * tempo))
            print(f'O valor atual é de R${va:.2f}')
            break

        elif opcaoFuncao == 3:
            print('-----Valor principal-----')
            va = float(input('Digite o valor atual: '))
            tempo = float(input('Digite o tempo em meses: '))
            taxa = float(input('Digite a taxa de juros (a.m): '))/100
            vp = va / (1 - taxa * tempo)
            print(f'O valor principal é de {vp:.2f} meses')
            break

        elif opcaoFuncao == 4:
            print('-----Tempo (em meses)-----')
            va = float(input('Digite o valor atual: '))
            vp = float(input('Digite o valor principal: '))
            taxa = float(input('Digite a taxa de juros (a.m): '))/100
            tempo = (va - vp) / (vp * (taxa * -1))
            print(f'O tempo é de {tempo:.2f} meses')
            break

        elif opcaoFuncao == 5:
            print('-----Taxa de juros (a.m)-----')
            va = float(input('Digite o valor atual: '))
            vp = float(input('Digite o valor principal: '))
            tempo = float(input('Digite o tempo em meses: '))
            taxa = (va - vp) / (vp * (tempo * -1))
            print(f'A taxa de juros é de {(taxa*100):.2f}% a.m.')
            break

        elif opcaoFuncao == 6:
            print('Saindo... 🚀')
            break

        else:
            print('Opção inválida!')

while opcao != 6:
    print('='*10)
    print("1- Juros Simples")
    print('2- Montante Simples')
    print('3- Juros Composto')
    print('4- Montante Composto')
    print('5- Desconto Simples')
    print('6- Sair')

    opcao = int(input('Escolha a opção que deseja calcular: '))

    if opcao == 1:
        print('-----Juros Simples-----')
        jurosSimples()
        
    elif opcao == 2:
        print('-----Montante Simples-----')
        montanteSimples()

    elif opcao == 3:
        print('-----Juros Compostos-----')
        jurosCompostos()

    elif opcao == 4:
        print('-----Montante Composto-----')
        montanteComposto()

    elif opcao == 5:
        print('-----Desconto Simples-----')
        descontoSimples()

    elif opcao == 6:
        print('Saindo... 🚀')

    else:
        print('Opção inválida!')