import random

cardapio = {
    "chocolate": 5.00,
    "baunilha": 4.50,
    "moranngo": 3.00,
    "flocos": 9.00

}

brindes = ["Canudo", "Copo personalizado", "Gelo", "Badge"]

def mostrar_cardapio():
    print("-- CARDAPIO --")
    for sabor, preco in cardapio.items():
        print(f"{sabor.title()}, R$ {preco}")

def fazer_pedido():
    total = 0
    pedido = []
    while True:
        sabor = input ("\nEscolha o sabor (digite 'fechar' para sair): ").lower()
        if sabor == "fechar":
            break
        elif sabor in cardapio:
            total += cardapio[sabor]
            pedido.append(sabor)
            print(f"{sabor.title()} adicionado!")
        else:
            print("esse sabor nao esta no cardapio")
    return pedido, total

mostrar_cardapio()
pedido, total = fazer_pedido()

print(f"\nSeu pedido: {pedido}")
print(f"Total: R$ {total:.2f}")

if total > 15:
    print(f"Voce ganhou um brinde: {random.choice(brindes)}")
