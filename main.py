

def acompanhamentoFeijoada():

    valid = False
    valor = 0
    while not valid:
        print("Selecione o acompanhamento: ")
        print('''
        0 - Não dejo mais acompanhamentos ( encerrar pedido ) ...... 0,00
        1 - 200g de arroz .......................................... 5,00
        2 - 150g de farofa especial ................................ 6,00
        3 - 100g de couve cozida ................................... 7,00
        4 - 1 laranja descascada ................................... 3,00
        ''')

        try:
            escolha = int(input("Sua escolha: "))

            #definindo o valor do multipicador de acordo com a escolha            
            if escolha == 0:
                valid = True
            elif escolha == 1:
                valor += 5
            elif escolha == 2:
                valor += 6
            elif escolha == 3:
                valor += 7
            elif escolha == 4:
                valor += 3

        except ValueError:
            print("Escolha inválida.")
        else:
            pass

    return valor


#valida entrada com valor inteiro
def validaInteiro():
    valid = False
    while not valid:
        try:
            x = int(input())
        except ValueError:
            print("Digite um valor válido")
        else:
            valid = True

    return x

def opcaoFeijoada():
    opcoes = ['B', 'P', 'S']

    print('Digite a opão desejada: ')
    print(
        '''
        B - Básica (FEIJÂO + PAIOL + COSTELINHA)
        P - Premium (FEIJÃO + PAIOL + COSTELINHA + PARTES DE PORCO)
        S - Suprema (FEIJÃO + PAIOL + COSTELINHA + PARTES DO PORCO + CHARQUE + CALABRESA + BACON)
        '''
    )

    print('Escolha: ')
    valid = False
    
    #valida escolha
    while not valid:
        escolha = input().upper()
        
        if escolha in opcoes:
            valid = True
        else:
            print("Digite uma opção válida.")

    if escolha == 'B':
        valor = 1
    elif escolha == 'P':
        valor = 1.25
    else:
        valor = 1.5

    return valor
    

def volumeFeijoada():
    print('Digite a quantidade desejada em ml:')
    valid = False
    while not valid: 

        volume = validaInteiro()
        print('volume: ', volume)
        if volume < 300:
            print('Volume inválido. Digite um valor entre 300 e 5000')
        elif volume > 5000:
            print('VOlume inválido. Digite um valor entre 300 e 5000')    
        else:
            print(f'Você optou por {volume}ml de feijoada.')
            valid = True

    volume *= 0.08
    return volume
 

def main():
    print("#" * 25)
    print("""\nFEIJOADA E CIA\n""")
    print("#" * 25)
    volume = volumeFeijoada()
    
    print('#' * 25)
    print("""\nOPCAO FEIJOADA\n""")
    print("#" * 25)

    opcao = opcaoFeijoada()
    acompanhamento = acompanhamentoFeijoada()
    
    total = (volume * opcao) + acompanhamento

    print("#" * 25)
    print(f'''
    TOTAL: {total}

    volume: {volume}
    opcao: {opcao}
    acompanhamento: {acompanhamento}
    ''')
    print("#" * 25)

main()