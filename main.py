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
        print("""\nVocê se encontra caminhando para sua casa ao anoitecer, depois de sua jornada de trabalho 6x1, pegando um ônibus cheio do Dantas Barreto/Igarassu que te deixa exausto.""")
        print("\nQual o seu nome?")
        name = input(">> ")
        print("\nQual o seu trabalho?")
        job = input(">> ")
        print(f"""\nApós o seu longo dia de trabalho trabalhando como {job}, {name} se encontra cansado, desencantado com a vida, afadigado com sua rotina de ver os mesmos cenários e pessoas todo santo dia, como também uma grande fome. Somente quando nada parece te apaziguar, você espia nos cantos dos seus olhos as luzes de um restaurante qualquer.""")
        print(f"""\nMas como esse restaurante chamou sua atenção você decide olhar para o que o cozinheiro está cozinhando, e percebe que se trata da seu prato favorito: """)
        food = input(">> ")
        print(f"""\nAgora, com uma vontade tremenda de saciar sua fome, como também comer de um delicioso prato de {food} você decide olhar para o preço da sua iguaria predileta, quando nota que ela custa: """)
        price = int(input(">> "))
        print(f'''\n"Caramba, {price}!", você exclama após olhar a bagatela do prato, "será que eu tenho a grana para comer esse prato?". {name} começa a pegar sua carteira freneticamente, ao notar que sua carteiro possuia nada mais, nada menos que: ''')
        money = int(input(">> "))
        if (price <= money):
            print(f'''\nFelizmente, {name} encontra {money} na sua carteira, o suficiente para saciar sua fome e voltar para casa feliz e de barriga cheia!''')
            print(end)
            break
        else:
            print(f'''\n{name} infelizmente, percebe que tinha {money}, o que não era o suficiente para comer {food}, seu prato favorito, e vai tristonho para casa''')
            print(end)
            break
            
story()