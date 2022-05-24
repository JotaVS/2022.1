#Autor: João Victor de Souza

from BST import BST
bst = BST()
texto = "A alegria é uma galeria de estímulos Na  catinga  uma  cantiga  muito  escutada é o silêncio do deserto"
palavras = texto.split()
palavrasUtilizadas = []
for n in palavras:
    chaveOrdenada = "".join(sorted(n.upper()))
    if n not in palavrasUtilizadas:
        if bst.find(chaveOrdenada) == False:
            bst.put(chaveOrdenada, [n])
        else:
            if bst.find(chaveOrdenada) == True:
                novoValor = bst.get(chaveOrdenada)
                novoValor.append(n)
                bst.put(chaveOrdenada, novoValor)
    palavrasUtilizadas.append(n)
for m in bst.values():
    if len(m) >= 2:
        print(m)
