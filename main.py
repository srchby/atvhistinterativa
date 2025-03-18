'''
Ideias: 
Pessoa A encontra restaurante B, que vende comida C,
pessoa A tem que ter dinheiro D para comprar comida C,
se tiver, come a comida e sai do restaurante, senão, é
chutado para fora
'''

def story():
    end = "\nFIM! \n História feita por Leandro Cordeiro"
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
            break
        else:
            print(f'''\n{name} infelizmente, percebe que não tinha o suficiente para comer {food} e vai tristonho para casa''')
            print(end)
            break
            
story()