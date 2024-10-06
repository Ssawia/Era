cont = True

run = True


while run:
    name = input('Digite o nome: ')
    total = 0

    while cont:
        cod = int(input('Digite o ID: '))

        match cod:
            case 1:
                print("Hot Dog R$ 11,20")
                total += 11.20
            case 2:
                print("Hamburguer R$ 16.60")
                total += 16.60
            case 3:
                print("Cheeseburguer R$ 22,00")
                total += 22.00
            case 4:
                print('Refrigerante em lata R$ 8,0')
                total += 8.00
            case 5:
                print("Batatas fritas R$ 32,50")
                total += 32.50
            case 6:
                print('Misto Quente R$ 13,00')
                total += 13.00


        msg = input("Quer continuar ? S N : ")
        if msg.lower() != 's':
            cont = False
            print(f"Nome: {name} | Total da Compra: {total}")


    msg = input("Próximo S/N: ")
    if msg.lower() != 's':
        run = False


    