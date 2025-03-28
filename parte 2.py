'''
Ideias: 
Pessoa A encontra restaurante B, que vende comida C,
pessoa A tem que ter dinheiro D para comprar comida C,
se tiver, come a comida e sai do restaurante, senão, é
chutado para fora
'''

def story():
    end = "\nFIM! \n História feita por Leandro Cordeiro e Editada por Kaio Silva"
    while (True):
        print("""\nVocê se encontra caminhando para sua casa ao anoitecer muito exausto.""")
        print("\nQual o seu nome?")
        name = input(">> ")
        print("\nQual o seu trabalho?")
        job = input(">> ")
        print(f"""\nApós o seu longo dia de trabalho trabalhando como {job}, {name} se encontra cansado, quando espia um restaurante.""")
        print(f"""\no restaurante chamou a atenção de {name} e percebe que se trata da seu prato favorito: """)
        food = input(">> ")
        print(f"""\nAgora, com uma vontade tremenda de comer um delicioso prato de {food} você olhar para o preço da da iguaria e nota que ela custa: """)
        price = int(input(">> "))
        print(f'''\n"Caramba, {price}! Será que eu tenho a grana para comer esse prato?". {name} começa a pegar sua carteira e nota que sua carteiro tinha: ''')
        money = int(input(">> "))
        if (price <= money):
            print(f'''\nFelizmente, {name} encontra {money} na sua carteira, o suficiente e volta para sua casa feliz e de barriga cheia!''')
            print(end)
        
        else:
            print(f'''\n{name} infelizmente, percebe que não tinha o suficiente para comer {food} e vai tristonho para casa''')
            print(end)

        #Edição por Kaio Konká™

        print(f'\nChegando em casa, {name} se depara com sua cama desarrumada e seu chão sujo')
        print('\nSerá que eu devo limpar meu chão?" *sim ou não')     
        answer = input(">> ") 
        if (answer) == 'sim':
            print('\nVocê decide limpar o chão como uma boa pessoa e se sente feliz.')
            
        else:
            print('\nVocê se sente extremamente cansado e decide nao limpar o chão, mas se sente um pouco triste.')
        
        print('\nSerá que eu devo arrumar minha cama?" *sim ou não')     
        answer2 = input(">> ") 
        if (answer2) == 'sim':
            print('\nLogo você arruma a sua cama e se deita para descansar após um cansativo dia, na esperança de ter um bom sono.')
            print('\nSua eperança valeu a pena, você dormiu um ótimo sono e acorda preparado para um novo dia')
            break
        else:
            print('\nVocê decide não arrumar a sua cama e se deita para descansar após um cansativo dia, na esperança de ter um bom sono.')
            print('\nInfelizmente suas esperanças não foram correspondidas. Você acorda com um cansaço tremendo para um novo dia')
            break
story()