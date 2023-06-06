from time import sleep
listNums = []
list = []

def criaList():
    num = 1
    while num != 0:
        num = int(input("Digite aqui o número inteiro diferente de zero para adicionar a lista: "))
        if num != 0:
            listNums.append(num)
        if num == 0:
            print(f'A lista criada é: {listNums}')
            remove_repetidos(listNums)


def remove_repetidos(listNums):
    print("Analisando itens repetidos...")
    sleep(3)
    for i in listNums:
        if i not in list:
            list.append(i)
    print(f'A lista atualizada e sem repetições é: {list}')

criaList()