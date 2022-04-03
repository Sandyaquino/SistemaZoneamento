import pandas as pd




def print_hi(name):
    print(f'Olá, {name}')

    with open("UCS_746992_2021.txt", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if "#Contratos#########" not in line:
                f.write(line)
        f.truncate()

    lista_de_enderecos = []
    ref_arquivo = pd.read_table("UCS_746992_2021.txt", sep='#')
    dimensao = ref_arquivo.shape
    numero_de_linhas = dimensao[0]

    for i in range(0, numero_de_linhas):
        lista_de_enderecos.append(ref_arquivo.iloc[i, 4])

    tamanho_da_lista = len(lista_de_enderecos)
    for i in range(0, tamanho_da_lista):
        if ("1") or ("2") or ("3") or ("4") or ("5") or ("6") or ("7") or ("8") or ("9") in lista_de_enderecos[i]:
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("1", "")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("2", "")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("3", "")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("4", "")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("5", "")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("6", "")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("7", "")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("8", "")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("9", "")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("0", "")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace(",", "")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("#", "")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("  ", "")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("PO", "Povoado")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("ASSENT", "Assentamento")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("FZ", "Fazenda")
            lista_de_enderecos[i] = lista_de_enderecos[i].title()

            if lista_de_enderecos[i][-1] == " ":
                lista_de_enderecos[i] = lista_de_enderecos[i].replace(str(lista_de_enderecos[i]),
                                                                      lista_de_enderecos[i][:-1])
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("Dos", "dos")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("Das", "das")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("Do", "do")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("Da", "da")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("De", "de")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("Ii", "II")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("Iii", "III")
            lista_de_enderecos[i] = lista_de_enderecos[i].replace("Vi", "VI")

        lista_de_enderecos_ = (sorted(set(lista_de_enderecos)))


    for j in range(0, len(lista_de_enderecos_)):
        try:
            if lista_de_enderecos_[j] in lista_de_enderecos_[j-1]:
                lista_de_enderecos_.pop(j)
        except:
            pass

    def join_list(lista_de_enderecos_):
        if len(lista_de_enderecos_) == 1:
            return '{}.'.format(lista_de_enderecos_[0])  # adicionar o ultimo com 'e' e retornar
        else:
            str = ', '.join(lista_de_enderecos_[:-1])  # gerar uma string com os items separados por virgula, com excecao do ultimo
            return '{} e {}.'.format(str, lista_de_enderecos_[-1])  # adicionar o ultimo com 'e' e retornar

    print("A lista de endereços é: " + str(join_list(lista_de_enderecos_)))

if __name__ == '__main__':
    print_hi('Sandy')
