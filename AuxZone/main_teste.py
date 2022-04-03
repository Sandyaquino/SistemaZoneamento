# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd

def print_hi(name):
    print(f'Hi, {name}')
    ref_arquivo = open("arquivo.txt", "r")

    teste = pd.read_table("arquivo.txt", sep='#')
    print(teste.columns.values[1])
    lista_de_enderecos = []
    contador = 0
    contador_de_linhas = 0
    for linha in ref_arquivo:
        contador_de_linhas = contador_de_linhas + 1
        tamanho_da_string = len(linha)
        #print(tamanho_da_string)
        contador_de_sustenido = 0
        for contador in range(0, tamanho_da_string):
            if linha[contador] == "#":
                contador_de_sustenido = contador_de_sustenido + 1
                if contador_de_sustenido == 4:
                    contador_aux_1 = contador
                    print("O endereço da linha " +  str(contador_de_linhas) + " começa na string  " + str(contador_aux_1))
                    #print(linha[contador + 1:contador + 9])
                if contador_de_sustenido == 5:
                    contador_aux = contador
                    print(" O endereço acaba na string " + str(contador_aux) )
                    print(" nesse caso o endereço tem " + str(contador_aux -contador_aux_1 - 1) + " strings")
                    #a = contador_aux -contador_aux_1 - 1
                    #print(contador_aux)
                    #print("dddd " + str(a))
                    #endereco = linha[contador_aux_1:contador_aux]
                    #print(str(contador_aux-contador_aux_1))
                    #print(endereco)
                    endereco = linha[contador_aux_1:contador_aux]
                    #lista_de_enderecos.append(endereco)
                    print(endereco)

                    if ("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" ) in endereco:
                        endereco = endereco.replace("1", "")
                        endereco = endereco.replace("2", "")
                        endereco = endereco.replace("3", "")
                        endereco = endereco.replace("4", "")
                        endereco = endereco.replace("5", "")
                        endereco = endereco.replace("6", "")
                        endereco = endereco.replace("7", "")
                        endereco = endereco.replace("8", "")
                        endereco = endereco.replace("9", "")
                        endereco = endereco.replace("0", "")
                        endereco = endereco.replace(",", "")
                        endereco = endereco.replace("#", "")
                        endereco = endereco.replace("  ", "")
                        endereco = endereco.replace("PO", "Povoado")
                        endereco = endereco.title()
                        print("Adcionei a lista de endereços o endereço " + str(endereco))
                    lista_de_enderecos.append(endereco)

        #for i in range(0,len(lista_de_enderecos)):
        #    if ("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" ) in lista_de_enderecos[i]:
        #        lista_de_enderecos[i] = lista_de_enderecos[i].replace("1", "")
        #        lista_de_enderecos[i] = lista_de_enderecos[i].replace("2", "")
        #        lista_de_enderecos[i] = lista_de_enderecos[i].replace("3", "")
        #        lista_de_enderecos[i] = lista_de_enderecos[i].replace("4", "")
        #        lista_de_enderecos[i] = lista_de_enderecos[i].replace("5", "")
        #        lista_de_enderecos[i] = lista_de_enderecos[i].replace("6", "")
        #        lista_de_enderecos[i] = lista_de_enderecos[i].replace("7", "")
        #        lista_de_enderecos[i] = lista_de_enderecos[i].replace("8", "")
        #        lista_de_enderecos[i] = lista_de_enderecos[i].replace("9", "")
        #        lista_de_enderecos[i] = lista_de_enderecos[i].replace("0", "")
        #        lista_de_enderecos[i] = lista_de_enderecos[i].replace(",", "")
        #        lista_de_enderecos[i] = lista_de_enderecos[i].replace("#", "")
        #        lista_de_enderecos[i] = lista_de_enderecos[i].replace("  ", "")
        #        lista_de_enderecos[i] = lista_de_enderecos[i].replace("PO", "Povoado")
         #       lista_de_enderecos[i] = lista_de_enderecos[i].title()
        #print(contador_de_linhas)
    print(lista_de_enderecos)
    print(len(lista_de_enderecos))
    print(contador_de_linhas)


if __name__ == '__main__':
    print_hi('PyCharm')
