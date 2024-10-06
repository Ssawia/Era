


nome = input("Digite o nome: ")
total = 0
while True:

    print("================Menu==============")
    print("1 Hot dog-----------------R$ 11,20")
    print("2 Hamburguer--------------R$ 16,60")
    print("3 Cheeseburguer-----------R$ 22,00")
    print("4 Refrigerante em lata----R$ 8,00")
    print("5 Batatas fritas----------R$ 32,50")
    print("6 Misto quente------------R$ 13,00")
    print("==================================")

    
    cod = int(input("Codigo do Produto: "))

    if cod == 1:
        total += 11.20
    elif cod == 2:
        total += 16.60
    elif cod == 3:
        total += 22.00
    elif cod == 4:
        total += 8.0
    elif cod == 5:
        total += 32.50
    elif cod == 6:
        total += 13.00
    

    msg = input("Continuar s/n: ")

    if msg.lower() != 's':
        break

print(f"Nome: {nome} Total: {total}")
